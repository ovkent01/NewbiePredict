# data.py
import yfinance as yf
import pandas as pd

def get_stock_data(ticker="AAPL", period="6mo", interval="1d"):
    stock = yf.Ticker(ticker)
    df = stock.history(period=period, interval=interval)
    df.reset_index(inplace=True)
    return df

# 测试：运行这个文件的时候会打印最新的股票数据
if __name__ == "__main__":
    df = get_stock_data("AAPL")
    print(df.head())
