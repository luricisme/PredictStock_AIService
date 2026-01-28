def calculate_fear_greed(percent_change: float, volatility: float) -> dict:
    score = 50

    # price momentum
    if percent_change > 2:
        score += 20
    elif percent_change < -2:
        score -= 20

    # volatility
    if volatility > 100:
        score += 10
    elif volatility < 30:
        score -= 10

    score = max(0, min(score, 100))

    label = (
        "Greed" if score > 60
        else "Fear" if score < 40
        else "Neutral"
    )

    return {
        "score": score,
        "label": label
    }
