# model.py
from sklearn.linear_model import LinearRegression
import numpy as np

def train_model(df):
    df = df.dropna()
    df['Day'] = np.arange(len(df))

    X = df[['Day']]
    y = df['Close']

    model = LinearRegression()
    model.fit(X, y)

    return model

def predict_future(model, days=5):
    last_day = model.n_features_in_ - 1
    future_days = np.arange(last_day + 1, last_day + 1 + days).reshape(-1, 1)
    return model.predict(future_days)
