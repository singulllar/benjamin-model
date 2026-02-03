
def average_daily_change(prices):
    """
    Calculates the average change between days.
    """
    changes = []

    for i in range(1, len(prices)):
        daily_change = prices[i] - prices[i - 1]
        changes.append(daily_change)

    return sum(changes) / len(changes)


def predict_future_prices(prices, days_into_future):
    """
    Predicts future prices using the average daily change.
    """
    avg_change = average_daily_change(prices)

    future_prices = []
    last_price = prices[-1]

    for _ in range(days_into_future):
        next_price = last_price + avg_change
        future_prices.append(round(next_price, 2))
        last_price = next_price

    return future_prices


if __name__ == "__main__":
    # Example historical prices (fake data)
    historical_prices = [100, 102, 101, 105, 107, 110]

    days_to_predict = 5

    predictions = predict_future_prices(
        historical_prices,
        days_to_predict
    )

    print("Historical prices:",historical_prices)
    print(f"Predicted prices: {predictions}")
