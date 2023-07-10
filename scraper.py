import yfinance as yf
import pandas as pd
import datetime

def scrape_data():
    # define the companies we want to scrape
    tickers = ["AAPL", "BRK-A", "META", "MSFT", "NVDA", "TSLA"]
    data = pd.DataFrame()

    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            # get the historical market data
            hist = stock.history(period="1d") # Fetching data for 1 day
            hist['Ticker'] = ticker  # add this column because it doesn't exist in the original data
            data = data.append(hist)
        except Exception as e:
            print(f"An error occurred while fetching data for {ticker}: {str(e)}")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data['Timestamp'] = timestamp  # add a consistent timestamp to the data
    return data

def save_to_csv():
    data = scrape_data()
    # save the data to a csv file
    data.to_csv('stock_data.csv', mode='a')  # 'a' mode will append the data

if __name__ == "__main__":
    save_to_csv()
