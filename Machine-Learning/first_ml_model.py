# Oliver Keen
# Based on https://developers.google.com/codelabs/tensorflow-1-helloworld
# first_ml_model.py
# 3/30/2021

import tensorflow as tf # Model uses TensorFlow 1, not TensorFlow 2
import numpy as np # Represents data as lists

# Framework for defining neural network as set of sequential layers
from tensorflow import keras


# Simple neural network: One layer of one neuron, where input shape is one value
model = tf.keras.Sequential(
    [
        keras.layers.Dense(units=1, input_shape=[1])
    ]
)

# Compiles neural net with loss and optimizer functions, where loss measures
# guessed answers against correct answers and optimizer makes another guess
model.compile(loss="mean_squared_error", optimizer="sgd")

# Defines data, where y = 3x + 1
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)

# Trains neural net, learning relationship between X's and Y's via loss and
# optimizer for specified number of epochs
model.fit(xs, ys, epochs=500)

# Predicts y, given x = 10
print(model.predict([10.0]))
