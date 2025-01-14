# -*- coding: utf-8 -*-
"""PTAC PROJECT STOC.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1u00eux5pgyg1h9UDkbyfUk9TMroZ7UuH

TATA STEEL
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

# Load DATA
df = pd.read_csv('/content/TATASTEEL.csv')

# Preprocess  data
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Split the data features (X) target (y)
X = df['Date'].values.astype(int) // 10**9
y = df['Close'].values

# linear regression model
model = LinearRegression()
model.fit(X.reshape(-1, 1), y)

# Calculate the date
current_date = datetime.now().date()
next_month = current_date + timedelta(days=20)
# Set the prediction period for one month
prediction_dates = pd.date_range(start=current_date, end=next_month, freq='D')

# Convert the prediction dates to numeric format
prediction_dates_numeric = prediction_dates.astype(int) // 10**9

# Make the stock price prediction
predicted_prices = model.predict(prediction_dates_numeric.values.reshape(-1, 1))

# Create a DataFrame for the predicted prices
prediction_df = pd.DataFrame({'Date': prediction_dates, 'Predicted Price': predicted_prices})

# Print the predicted stock prices for the next month
print("Predicted Tesla stock prices for the next month:")
print(prediction_df)

# Plot the historical and predicted stock prices
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Close'], label='Historical')
plt.plot(prediction_df['Date'], prediction_df['Predicted Price'], marker='o', color='red', label='Predicted')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('Tata steel Stock Price Prediction for One Month')
plt.legend()
plt.show()



"""TESLA"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

# Load DATA
df = pd.read_csv('/content/tesla.csv')

# Preprocess data
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Split the data features (X) target (y)
X = df['Date'].values.astype(int) // 10**9
y = df['Close'].values

# Linear regression model
model = LinearRegression()
model.fit(X.reshape(-1, 1), y)

# Calculate the date
current_date = datetime.now().date()
next_month = current_date + timedelta(days=30)

# Set the prediction period for one month
prediction_dates = pd.date_range(start=current_date, end=next_month, freq='D')

# Convert the prediction dates to numeric format
prediction_dates_numeric = prediction_dates.astype(int) // 10**9

# Make the stock price prediction
predicted_prices = model.predict(prediction_dates_numeric.values.reshape(-1, 1))

# Create a DataFrame for the predicted prices
prediction_df = pd.DataFrame({'Date': prediction_dates, 'Predicted Price': predicted_prices})

# Print the predicted stock prices for the next month
print("Predicted Tesla stock prices for the next month:")
print(prediction_df)

# Plot the historical and predicted stock prices
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Close'], label='Historical')
plt.plot(prediction_df['Date'], prediction_df['Predicted Price'], marker='o', color='red', label='Predicted')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('Tesla Stock Price Prediction for One Month from Today')
plt.legend()
plt.show()