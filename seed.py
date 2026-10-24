from database import get_db, init_db
from analyzer import analyze_review
import json


reviews = [
    {
        "rating": 1,
        "review": "Order was marked delivered but I never received it. Customer support gave generic responses and did not properly investigate."
    },
    {
        "rating": 1,
        "review": "Order took more than 2 hours, arrived cold, cancellation was not allowed, and I received the wrong item. Support did not resolve the issue."
    },
    {
        "rating": 1,
        "review": "An item was missing from my order. I reported it through the help centre but my refund was denied and the complaint was not handled properly."
    },
    {
        "rating": 1,
        "review": "Payment appeared to fail but the order went through. Cancellation was unclear and I lost money."
    },
    {
        "rating": 1,
        "review": "Payment was processing and then the order was cancelled. Money was deducted or stuck and I could not properly contact support."
    },
    {
        "rating": 1,
        "review": "My order was delayed by about 1 hour 45 minutes even though the app showed 10 minutes. Delivery partners changed and support did not respond."
    },
    {
        "rating": 5,
        "review": "The app is convenient with many restaurants, easy ordering, useful tracking, good packaging, timely delivery and offers."
    },
    {
        "rating": 1,
        "review": "Delivery partners were assigned from far away, causing the food to become cold. Support attempts were unsuccessful."
    },
    {
        "rating": 1,
        "review": "I experienced multiple payment failures and delayed orders. My recent order was cancelled without a clear reason."
    },
    {
        "rating": 1,
        "review": "The chatbot could not resolve my issue and there was no clear way to contact human customer support."
    },
    {
        "rating": 1,
        "review": "I wanted a cancellation warning or cancellation period before confirming an order and the ability to use another person's UPI."
    },
    {
        "rating": 1,
        "review": "Cash on delivery was removed. Food prices, delivery charges, platform fees and taxes make ordering expensive."
    },
    {
        "rating": 1,
        "review": "The chatbot repeatedly gave scripted responses and there was no clear way to reach a human agent."
    },
    {
        "rating": 1,
        "review": "The restaurant accepted the order and then cancelled it because the food was unavailable. The order should not have been accepted."
    },
    {
        "rating": 3,
        "review": "Customer support has improved somewhat, but menu prices and platform fees are high and restaurant availability for Gold membership is limited."
    },
    {
        "rating": 1,
        "review": "Delivery estimates are inaccurate and orders are often late. Food and packaging quality can be poor and app prices are higher than restaurant prices."
    },
    {
        "rating": 1,
        "review": "I selected the wrong address and contacted support immediately, but the order was cancelled without a refund."
    }
]


def seed_database():

    init_db()

    db = get_db()

    # Remove old data so we don't create duplicates
    db.execute("DELETE FROM reviews")

    for item in reviews:

        result = analyze_review(item["review"])

        db.execute("""
            INSERT INTO reviews
            (review, rating, themes, pain_points, suggested_features)
            VALUES (?, ?, ?, ?, ?)
        """, (
            item["review"],
            item["rating"],
            json.dumps(result["themes"]),
            json.dumps(result["pain_points"]),
            json.dumps(result["suggested_features"])
        ))

    db.commit()
    db.close()

    print("17 reviews added successfully!")


if __name__ == "__main__":
    seed_database()