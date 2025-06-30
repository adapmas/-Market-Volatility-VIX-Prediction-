import yfinance as yf
import pandas as pd

def get_data():
    tickers = {
        'VIX': '^VIX',
        'S&P500': '^GSPC',
        'Gold': 'GC=F',
        'Oil': 'CL=F'
    }

    data = []
    for name, ticker in tickers.items():
        df = yf.download(ticker, start='2015-01-01', end='2024-12-31')
        df = df[['Close']].rename(columns={'Close': name})
        data.append(df)


    combined = pd.concat(data, axis=1, join='inner')
    combined.dropna(inplace=True)

    combined.to_csv('./data/merged_data.csv')
    print("✅ Data saved to 'data/merged_data.csv'")
    return combined

if __name__ == "__main__":
    df = get_data()
    print(df.head())
