def analyze_review(review):

    text = review.lower()

    themes = []
    pain_points = []
    suggested_features = []

    # Customer Support
    if any(word in text for word in [
        "support",
        "customer care",
        "chatbot",
        "human agent",
        "help centre",
        "help center",
        "complaint",
        "agent"
    ]):
        themes.append("Customer Support")
        pain_points.append(
            "Difficult to reach effective human support"
        )
        suggested_features.append(
            "One-tap human support escalation"
        )

    # Delivery / ETA
    if any(word in text for word in [
        "late",
        "delay",
        "delayed",
        "delivery",
        "eta",
        "waiting",
        "cold food",
        "minutes",
        "hours"
    ]):
        themes.append("Delivery / ETA")
        pain_points.append(
            "Inaccurate delivery estimates or delayed orders"
        )
        suggested_features.append(
            "Accurate live ETA + delay alerts"
        )

    # Cancellation / Refund
    if any(word in text for word in [
        "cancel",
        "cancelled",
        "cancellation",
        "refund",
        "refunded",
        "money back"
    ]):
        themes.append("Cancellation / Refund")
        pain_points.append(
            "Unclear cancellation or refund status"
        )
        suggested_features.append(
            "Cancellation & refund tracker"
        )

    # Payment
    if any(word in text for word in [
        "payment",
        "upi",
        "paid",
        "deducted",
        "transaction",
        "failed",
        "processing"
    ]):
        themes.append("Payment")
        pain_points.append(
            "Unclear payment or transaction status"
        )
        suggested_features.append(
            "Real-time payment status"
        )

    # Food / Order Quality
    if any(word in text for word in [
        "missing",
        "wrong item",
        "wrong order",
        "cold food",
        "food quality",
        "damaged",
        "packaging",
        "incorrect"
    ]):
        themes.append("Food / Order Quality")
        pain_points.append(
            "Problems with missing, wrong, cold or poor-quality orders"
        )
        suggested_features.append(
            "Order issue reporting"
        )

    # Pricing / Fees
    if any(word in text for word in [
        "price",
        "pricing",
        "fee",
        "fees",
        "expensive",
        "tax",
        "platform fee",
        "delivery charge",
        "cost"
    ]):
        themes.append("Pricing / Fees")
        pain_points.append(
            "Limited clarity around total price and fees"
        )
        suggested_features.append(
            "Transparent fee breakdown"
        )

    if not themes:
        themes.append("Other")

    return {
        "themes": themes,
        "pain_points": pain_points,
        "suggested_features": suggested_features
    }