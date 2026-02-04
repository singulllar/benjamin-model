
# Step 1: Calculate the average daily change
def average_daily_change(prices):
    total_change = 0  # store sum of daily changes
    count = 0         # count how many changes we have

    # Loop through prices starting from the second day
    for i in range(1, len(prices)):
        change = prices[i] - prices[i - 1]  # today - yesterday
        total_change += change              # add to total
        count += 1                          # increment count

    # Divide total change by number of changes to get average
    average_change = total_change / count
    return average_change


# Step 2: Predict future prices using the average daily change
def predict_future_prices(prices, days_into_future):
    avg_change = average_daily_change(prices)  # get average daily change

    future_prices = []          # list to store predicted prices
    last_price = prices[-1]     # start prediction from the last known price

    for _ in range(days_into_future):
        next_price = last_price + avg_change  # add average change
        next_price = round(next_price, 2)    # round to 2 decimals
        future_prices.append(next_price)     # save predicted price
        last_price = next_price              # update last_price for next iteration

    return future_prices

def calculate_average_error(predicted_prices, actual_prices):
    total_error = 0
    count = 0

    for i in range(len(predicted_prices)):
        error = abs(predicted_prices[i] - actual_prices[i])
        total_error += error
        count += 1

    average_error = total_error / count
    return average_error


# Step 3: Example usage
if __name__ == "__main__":
    all_prices = [100, 102, 101, 105, 107, 110, 112, 111, 113, 115]

    past_prices = all_prices[:5]     # first 5 days
    actual_future_prices = all_prices[5:]  # real next 5 days

    days_to_predict = 5

    predicted_prices = predict_future_prices(
        past_prices,
        days_to_predict
    )

    error = calculate_average_error(
        predicted_prices,
        actual_future_prices
    )

    print("Past prices:", past_prices)
    print("Actual future prices:", actual_future_prices)
    print("Predicted prices:", predicted_prices)
    print("Average prediction error:", round(error, 2))