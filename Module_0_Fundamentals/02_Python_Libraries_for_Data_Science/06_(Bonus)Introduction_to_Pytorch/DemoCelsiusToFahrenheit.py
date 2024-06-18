############################################################################################
# Example to convert Celsius (C) to Fahrenheit (F)
# F = C * 1.8 + 32

# Regular programing
# def function(C):
#     F = C * 1.8 + 32
#     return F
############################################################################################

# To install a package as administrator
# pip install tensorflow --user
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' 

import tensorflow as tf
from tensorflow.python.keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

keras = tf.keras
capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

modelo.compile(
    optimizer = tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

print('Starting training...')
historial = modelo.fit(celsius, fahrenheit, epochs=1000, verbose=False)
print('Model trained')

print('Test a prediction for 100°C...')
testCelsius = 100.0
resultado = modelo.predict(x=np.array([testCelsius]))
print('The outcome for: ' + str(testCelsius) + 'is: ' + str(resultado) + ' fahrenheit!')
# El resultado es[[211.74016]] fahrenheit!

print('Variables internas del modelo:')
print(capa.get_weights())

plt.xlabel('# Epoca')
plt.ylabel('Magnitud de perdida')
plt.plot(historial.history['loss'])
plt.show()