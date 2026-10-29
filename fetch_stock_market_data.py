import requests
import pandas as pd
import os
import time
from dotenv import load_dotenv


try:
    load_dotenv()
    API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
except Exception as e:
    print(e)

def fetch_data_from_api(symbol : str):
    url = "https://www.alphavantage.co/query"
    params= {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : symbol,
    "outputsize" : "compact",
    "apikey" : API_KEY
    }

    response = requests.get(url, params=params, timeout=10)
    if response.status_code == 200:
        meta_data = response.json()
    else:
        raise Exception("Data has not been fetched from API.\n Please try again")
    return meta_data

def extract_data(tickers : list[str]):
    all_df = []
    for ticker in tickers:
        try:
            fetch_data = fetch_data_from_api(ticker)
            if "Time Series (Daily)" in fetch_data:
                data = pd.DataFrame.from_dict(fetch_data["Time Series (Daily)"], orient= "index")
                # Clean column names (e.g., '1. open' -> 'open')
                data.columns = [col.split(" ")[1] for col in data.columns]

                # Reset index to make Date a column
                data.reset_index(inplace=True)
                data.rename(columns={"index": "date"}, inplace=True)
                data["ticker"] = ticker
                print(data.head())
                all_df.append(data)
                time.sleep(15)
            else:
                print(fetch_data)
        except Exception as e:
            print(e)
    

    if all_df:
        all_tickers_df = pd.concat(all_df, ignore_index=True)
        return all_tickers_df
    else:
        return None


if __name__ == "__main__":
    
    tickers = ["AAPL", "MSFT", "NVDA", "GOOGL","AMZN"]
    api_fetched_df = extract_data(tickers)
    if api_fetched_df is not None:
        api_fetched_df.to_csv("stock_data.csv", index=False)
    else:
        print("No data is fetched.")  


    
 

