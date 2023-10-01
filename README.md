# Real-time IHSG (Indonesia Stock Exchange) Trading Strategy

This Python script demonstrates a real-time trading strategy for the Indonesia Stock Exchange (IHSG) using historical stock price data to calculate a moving average. It helps make trading decisions based on whether the current price is above or below the moving average.

## Prerequisites

Before running the script, make sure you have the following prerequisites installed:

1. [Python](https://www.python.org/downloads/)
2. Required Python libraries (`ihsg`, `moving_average`, and `descriptive`). You can install these libraries using `pip`:

   ```bash
   pip install ihsg moving_average descriptive
   ```

3. Access to IHSG stock price data, which can be obtained through various financial data providers or APIs.

## Usage

1. Import the necessary libraries:

   ```python
   import ihsg
   import moving_average as ma
   import descriptive as ds
   ```

2. Create a function `proc()` to execute the trading strategy. The script continuously monitors IHSG stock price data, calculates a moving average, and makes trading decisions based on the relationship between the current price and the moving average.

3. Customize the trading strategy logic within the `proc()` function to match your specific trading rules and criteria.

4. Set the `interval_minutes` variable to define the time interval at which the script checks the stock price data.

5. The script fetches historical stock price data using the `ihsg` library, calculates a 21-day moving average (`ma21`), and compares the last observed price (`last_price`) with the moving average.

6. Depending on the comparison result, the script prints trading decisions, such as "BUY" or "WAIT," along with the relevant price and moving average values.

7. The script continues to monitor and make trading decisions in real-time, waiting for the specified time interval before checking the data again.

8. Customize the trading strategy, add additional conditions, or integrate it with trading platforms as needed.

## Notes

- This script serves as a basic example and does not include actual trading execution. You should implement trading execution logic and risk management strategies separately if you intend to use this for live trading.
- Ensure you have access to reliable and up-to-date IHSG stock price data.
- Be cautious when using trading strategies and algorithms for financial markets, as they involve risks. Make sure to conduct thorough testing and research before deploying any trading strategy in a live environment.

## License

This script is provided under the [MIT License](LICENSE).
```

You can customize the script and README.md file further to suit your specific trading strategy and requirements.
