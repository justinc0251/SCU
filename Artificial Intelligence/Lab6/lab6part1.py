# Justin Chung, Aster Li, Jonathan Fong
# COEN 166 Lab 6 Part 2

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Load Fashion MNIST dataset
fashion_mnist = keras.datasets.fashion_mnist
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

# Normalize the pixel values
x_train, x_test = x_train / 255.0, x_test / 255.0

# Flatten the image to a vector for the input layer
x_train_flat = x_train.reshape(x_train.shape[0], -1)
x_test_flat = x_test.reshape(x_test.shape[0], -1)

# Build a two-layer neural network
model = keras.Sequential([
    layers.Dense(512, activation='relu', input_shape=(x_train_flat.shape[1],)),
    layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train_flat, y_train, epochs=5, batch_size=32)

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test_flat, y_test, verbose=2)

# Predictions
prediction = model.predict(x_test_flat)
predict_class = np.argmax(prediction, axis=1)

# Confusion matrix
cm = confusion_matrix(y_test, predict_class)

# Plot confusion matrix
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.ylabel('True Label')
plt.xlabel('Predicted Label')
plt.show()

# Plot one image from each class
uniquelabels = np.unique(y_train)
fig, axes = plt.subplots(1, len(uniquelabels), figsize=(12, 12))
for i, label in enumerate(uniquelabels):
    # Find first image of each class
    idx = np.where(y_train == label)[0][0]
    axes[i].imshow(x_train[idx], cmap='gray')
    axes[i].set_title(f'Class {label}')
    axes[i].axis('off')

plt.show()

