import yfinance as yf
import pandas as pd
from datetime import datetime

# List of companies to scrape data for
companies = ['AAPL', 'BRK-A', 'META', 'MSFT', 'NVDA', 'TSLA']

# Get current timestamp
now = datetime.now()

# Open or create the CSV file in append mode
with open('/tmp/stock_data.csv', 'a') as f:
    for company in companies:
        try:
            # Download stock data
            data = yf.download(company, start='2023-01-01', end=now.strftime('%Y-%m-%d'))

            # Add timestamp and company columns
            data['timestamp'] = now
            data['company'] = company

            # Write data to CSV
            data.to_csv(f, header=f.tell()==0)
            
        except Exception as e:
            print(f"An error occurred while fetching data for {company}: {e}")

print("Data fetching completed.")

