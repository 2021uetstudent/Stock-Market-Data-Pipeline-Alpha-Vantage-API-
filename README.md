# Stock Market Data Pipeline (Alpha Vantage API)

A small Python data pipeline that fetches daily stock price history for multiple companies from the [Alpha Vantage API](https://www.alphavantage.co/), cleans the response, and saves everything into a single CSV file that is ready for analysis.

## What It Does

1. Sends a request to the Alpha Vantage `TIME_SERIES_DAILY` endpoint for each ticker
2. Checks every response and handles errors, so one failed call does not stop the whole run
3. Cleans the raw JSON (for example, renames columns like `1. open` to `open`)
4. Adds a `ticker` column so each row can be traced back to its company
5. Combines all companies into one Pandas DataFrame
6. Exports the result to `stock_data.csv`

## Companies Covered

| Ticker | Company |
|--------|---------|
| AAPL   | Apple |
| MSFT   | Microsoft |
| NVDA   | NVIDIA |
| GOOGL  | Google (Alphabet) |
| AMZN   | Amazon |

You can change the list in the `tickers` variable at the bottom of the script.

## Tech Stack

- **Python 3.9+**
- **Requests** for calling the API
- **Pandas** for cleaning and combining data
- **python-dotenv** for keeping the API key out of the code

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 2. Install dependencies

```bash
pip install requests pandas python-dotenv
```

### 3. Get a free API key

Create a free key at [alphavantage.co/support/#api-key](https://www.alphavantage.co/support/#api-key).

### 4. Create a `.env` file

In the project folder, create a file named `.env` and add your key:

```
ALPHA_VANTAGE_API_KEY=your_api_key_here
```

> **Important:** Add `.env` to your `.gitignore` so your key is never pushed to GitHub.

### 5. Run the script

```bash
python fetch_stock_data.py
```

When it finishes, you will find `stock_data.csv` in the project folder.

## Output

`stock_data.csv` contains one row per company per trading day:

| date | open | high | low | close | volume | ticker |
|------|------|------|-----|-------|--------|--------|
| 2026-10-28 | ... | ... | ... | ... | ... | AAPL |

By default the script uses `outputsize=compact`, which returns roughly the **last 100 trading days** for each ticker. Change it to `full` for the complete history.

## Rate Limits

The free Alpha Vantage plan limits how many requests you can make per minute and per day. The script pauses between requests to stay within these limits. If you see a message about the call frequency instead of data, wait a minute and run it again.

## Project Structure

```
.
├── fetch_stock_data.py   # Main script
├── stock_data.csv        # Output (created after running)
└── README.md
```

## What I Learned

- API data never arrives analysis-ready, so cleaning it is a big part of the work
- Free APIs have rate limits, and your code needs to be designed around them
- API keys belong in environment variables, never in the source code
- Error handling matters: one bad response should not break the whole pipeline

## Next Steps

- [ ] Convert price and volume columns to numeric types and `date` to datetime
- [ ] Build a dashboard comparing the five stocks (price trends, volatility, returns)
- [ ] Use the OpenAI API to generate a short written summary of each stock's trend
- [ ] Store the data in a SQL database instead of a CSV


## Disclaimer

This project is for learning purposes only. It is not financial advice.
