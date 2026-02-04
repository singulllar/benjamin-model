"""
Benjamin v-1.1
Simple Stock Price Predictor with Accuracy Visualization

Idea:
- Use past prices
- Calculate average daily change
- Predict future prices
- Compare predictions with real prices
- Visualize results in the terminal
"""

# ===============================
# Step 1: Calculate average daily change
# ===============================
def average_daily_change(prices):
    total_change = 0
    count = 0

    for i in range(1, len(prices)):
        change = prices[i] - prices[i - 1]
        total_change += change
        count += 1

    return total_change / count


# ===============================
# Step 2: Predict future prices
# ===============================
def predict_future_prices(prices, days_into_future):
    avg_change = average_daily_change(prices)

    future_prices = []
    last_price = prices[-1]

    for _ in range(days_into_future):
        next_price = last_price + avg_change
        next_price = round(next_price, 2)
        future_prices.append(next_price)
        last_price = next_price

    return future_prices


# ===============================
# Step 3: Calculate prediction error
# ===============================
def calculate_average_error(predicted_prices, actual_prices):
    total_error = 0
    count = 0

    for i in range(len(predicted_prices)):
        error = abs(predicted_prices[i] - actual_prices[i])
        total_error += error
        count += 1

    return total_error / count


# ===============================
# Step 4: Terminal visualization
# ===============================
def print_header():
    print("=" * 55)
    print("      📈 BENJAMIN v-1.1 — STOCK PREDICTOR 📉")
    print("        Simple Average-Based Model")
    print("=" * 55)


def print_prediction_table(actual, predicted):
    print("\nDay | Actual Price | Predicted Price | Error")
    print("-" * 45)

    for i in range(len(actual)):
        error = abs(predicted[i] - actual[i])
        print(
            f"{i+1:>3} | "
            f"{actual[i]:>12} | "
            f"{predicted[i]:>15} | "
            f"{round(error, 2):>5}"
        )


def print_error_bars(actual, predicted):
    print("\nPrediction Error Visualization")
    print("(Each █ ≈ $1 error)")
    print("-" * 45)

    for i in range(len(actual)):
        error = abs(predicted[i] - actual[i])
        bars = "█" * int(error)
        print(f"Day {i+1}: {bars} ({round(error, 2)})")


# ===============================
# Step 5: Run the program
# ===============================
if __name__ == "__main__":

    # Example dataset (fake stock prices)
    all_prices = [100, 102, 101, 105, 107, 110, 112, 111, 113, 115]

    # Split data
    past_prices = all_prices[:5]
    actual_future_prices = all_prices[5:]

    days_to_predict = 5

    # Make predictions
    predicted_prices = predict_future_prices(
        past_prices,
        days_to_predict
    )

    # Calculate accuracy
    average_error = calculate_average_error(
        predicted_prices,
        actual_future_prices
    )

    # Display results
    print_header()

    print("\nPast prices:", past_prices)
    print("Actual future prices:", actual_future_prices)
    print("Predicted prices:", predicted_prices)

    print_prediction_table(actual_future_prices, predicted_prices)
    print_error_bars(actual_future_prices, predicted_prices)

    print("\n" + "=" * 55)
    print(f"Average Prediction Error: ${round(average_error, 2)}")
    print("Lower is better 📉")
    print("=" * 55)
