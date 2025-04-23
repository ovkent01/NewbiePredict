# main.py
from data import get_stock_data
from model import train_model, predict_future
import matplotlib.pyplot as plt

df = get_stock_data("AAPL")
model = train_model(df)
preds = predict_future(model, days=5)

# 可视化
plt.plot(df['Close'], label="Historical")
plt.plot(range(len(df), len(df)+5), preds, label="Predicted", linestyle='--')
plt.title("Stock Price Prediction")
plt.xlabel("Days")
plt.ylabel("Price")
plt.legend()
plt.show()
