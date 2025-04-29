import tensorflow.compat.v1 as tf
from tensorflow.keras import layers, models
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Leer el dataset desde una URL pública
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-min-temperatures.csv'
df = pd.read_csv(url, parse_dates=['Date'], index_col='Date')

# Ver las primeras filas y graficar
print(df.head())
df.plot(figsize=(12,5), title='Temperaturas mínimas diarias')
plt.show()

# Escalar los valores entre 0 y 1
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df[['Temp']])

# Función para crear datos en formato [X -> y]
def create_dataset(data, window_size=7):
    X, y = [], []
    for i in range(len(data) - window_size):
        X.append(data[i:i+window_size])
        y.append(data[i+window_size])
    return np.array(X), np.array(y)

X, y = create_dataset(scaled_data, window_size=7)

# Dividir en train y test
split_index = int(len(X) * 0.8)
X_train, X_test = X[:split_index], X[split_index:]
y_train, y_test = y[:split_index], y[split_index:]

# Modelo secuencial con una capa LSTM
model = models.Sequential([
    layers.LSTM(50, activation='relu', input_shape=(7, 1)),
    layers.Dense(1)
])

# Compilar y entrenar
model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, epochs=10, validation_split=0.1)

# Modelo secuencial con una capa LSTM
model = models.Sequential([
    layers.LSTM(50, activation='relu', input_shape=(7, 1)),
    layers.Dense(1)
])

# Compilar y entrenar
model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, epochs=10, validation_split=0.1)