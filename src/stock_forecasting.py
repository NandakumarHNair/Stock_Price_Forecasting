import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

# Load dataset
df = pd.read_csv('stock_data.csv')  # Replace with your dataset

# Data preprocessing
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Feature engineering
df['Day'] = df.index.day
df['Month'] = df.index.month
df['Year'] = df.index.year

# Define features and target variable
X = df[['Open', 'High', 'Low', 'Volume', 'Day', 'Month', 'Year']]
y = df['Close']

# Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Linear Regression model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_predictions = lr_model.predict(X_test)
lr_mse = mean_squared_error(y_test, lr_predictions)

# Decision Tree model
dt_model = DecisionTreeRegressor(random_state=42)
dt_model.fit(X_train, y_train)
dt_predictions = dt_model.predict(X_test)
dt_mse = mean_squared_error(y_test, dt_predictions)

# Evaluate models
print(f'Linear Regression MSE: {lr_mse}')
print(f'Decision Tree MSE: {dt_mse}')

# Select best model (example based on MSE, adjust as needed)
best_model = lr_model if lr_mse < dt_mse else dt_model
best_predictions = lr_predictions if lr_mse < dt_mse else dt_predictions

# Save the best model predictions
df_results = pd.DataFrame({'Actual': y_test, 'Predicted': best_predictions})
df_results.to_csv('predictions.csv', index=False)
