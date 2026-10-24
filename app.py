from flask import Flask, jsonify, request
from flask_cors import CORS
import json

from database import get_db, init_db
from analyzer import analyze_review

app = Flask(__name__)
CORS(app)

# Create database when application starts
init_db()


@app.route("/")
def home():
    return jsonify({
        "message": "Product Feedback Analyser Backend is running!"
    })


@app.route("/api/health")
def health():
    return jsonify({
        "status": "ok"
    })


@app.route("/api/reviews", methods=["POST"])
def add_review():

    data = request.get_json()

    review = data.get("review", "")
    rating = data.get("rating")

    if not review:
        return jsonify({
            "error": "Review is required"
        }), 400

    if rating is None:
        return jsonify({
            "error": "Rating is required"
        }), 400

    try:
        rating = int(rating)
    except ValueError:
        return jsonify({
            "error": "Rating must be a number"
        }), 400

    if rating < 1 or rating > 5:
        return jsonify({
            "error": "Rating must be between 1 and 5"
        }), 400

    result = analyze_review(review)

    db = get_db()

    cursor = db.execute("""
        INSERT INTO reviews
        (review, rating, themes, pain_points, suggested_features)
        VALUES (?, ?, ?, ?, ?)
    """, (
        review,
        rating,
        json.dumps(result["themes"]),
        json.dumps(result["pain_points"]),
        json.dumps(result["suggested_features"])
    ))

    db.commit()

    review_id = cursor.lastrowid

    db.close()

    return jsonify({
        "id": review_id,
        "review": review,
        "rating": rating,
        "themes": result["themes"],
        "pain_points": result["pain_points"],
        "suggested_features": result["suggested_features"]
    }), 201


@app.route("/api/reviews", methods=["GET"])
def get_reviews():

    db = get_db()

    rows = db.execute("""
        SELECT *
        FROM reviews
        ORDER BY id DESC
    """).fetchall()

    db.close()

    reviews = []

    for row in rows:
        reviews.append({
            "id": row["id"],
            "review": row["review"],
            "rating": row["rating"],
            "themes": json.loads(row["themes"]),
            "pain_points": json.loads(row["pain_points"]),
            "suggested_features": json.loads(
                row["suggested_features"]
            ),
            "created_at": row["created_at"]
        })

    return jsonify(reviews)


@app.route("/api/analysis", methods=["GET"])
def get_analysis():

    db = get_db()

    rows = db.execute("""
        SELECT themes, pain_points, suggested_features
        FROM reviews
    """).fetchall()

    db.close()

    theme_counts = {}
    pain_point_counts = {}
    feature_counts = {}

    for row in rows:

        themes = json.loads(row["themes"])
        pain_points = json.loads(row["pain_points"])
        features = json.loads(row["suggested_features"])

        for theme in themes:
            theme_counts[theme] = theme_counts.get(theme, 0) + 1

        for pain in pain_points:
            pain_point_counts[pain] = (
                pain_point_counts.get(pain, 0) + 1
            )

        for feature in features:
            feature_counts[feature] = (
                feature_counts.get(feature, 0) + 1
            )

    return jsonify({
        "review_count": len(rows),
        "theme_counts": theme_counts,
        "pain_point_counts": pain_point_counts,
        "feature_counts": feature_counts
    })
@app.route("/api/priorities", methods=["GET"])
def get_priorities():

    db = get_db()

    rows = db.execute("""
        SELECT suggested_features
        FROM reviews
    """).fetchall()

    db.close()

    feature_frequency = {}

    for row in rows:

        features = json.loads(row["suggested_features"])

        for feature in features:
            feature_frequency[feature] = (
                feature_frequency.get(feature, 0) + 1
            )

    feature_details = {
        "One-tap human support escalation": {
            "impact": 5,
            "effort": 2
        },

        "Accurate live ETA + delay alerts": {
            "impact": 5,
            "effort": 3
        },

        "Cancellation & refund tracker": {
            "impact": 5,
            "effort": 4
        },

        "Real-time payment status": {
            "impact": 5,
            "effort": 3
        },

        "Order issue reporting": {
            "impact": 4,
            "effort": 4
        },

        "Transparent fee breakdown": {
            "impact": 3,
            "effort": 2
        }
    }

    priorities = []

    for feature, frequency in feature_frequency.items():

        details = feature_details.get(
            feature,
            {
                "impact": 3,
                "effort": 3
            }
        )

        impact = details["impact"]
        effort = details["effort"]

        priority_score = (
            frequency * impact
        ) / effort

        priorities.append({
            "feature": feature,
            "frequency": frequency,
            "impact": impact,
            "effort": effort,
            "priority_score": round(priority_score, 2)
        })

    priorities.sort(
        key=lambda x: x["priority_score"],
        reverse=True
    )

    return jsonify(priorities)


if __name__ == "__main__":
    app.run(debug=True)