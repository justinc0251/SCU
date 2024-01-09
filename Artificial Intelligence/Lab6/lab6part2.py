# Justin Chung, Aster Li, Jonathan Fong
# COEN 166 Lab 6 Part 2

import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Reshape
from tensorflow.keras.models import Model
from tensorflow.keras.datasets import fashion_mnist
import numpy as np
import matplotlib.pyplot as plt

# Load Fashion MNIST dataset
(x_train, _), (x_test, _) = fashion_mnist.load_data()

# Normalize the images to be in the range of [0, 1]
x_train, x_test = x_train / 255.0, x_test / 255.0

# Get the dimensions of the images
m, n = x_train.shape[1], x_train.shape[2]

# Function to create the neural network model
def create_model(P):
    # Input layer: Flatten image to 1D vector
    input_img = Input(shape=(m*n,))

    # Compressed layer with P nodes and ReLU activation
    encoded = Dense(P, activation='relu')(input_img)

    # Expansion layer with m*n*2 nodes and ReLU activation
    expanded = Dense(m*n*2, activation='relu')(encoded)

    # Output layer with m*n nodes and Sigmoid activation
    decoded = Dense(m*n, activation='sigmoid')(expanded)

    # Reshape the output to 2D image
    decoded = Reshape((m, n))(decoded)

    # Define the autoencoder model
    autoencoder = Model(input_img, decoded)

    # Compile the model with Adam optimizer and mean squared error loss
    autoencoder.compile(optimizer='adam', loss='mean_squared_error')
    return autoencoder

# List of P values to train the model with
P_values = [10, 50, 200]

# Dictionary to store the trained models
models = {}

# Train the model for each value of P
for P in P_values:
    print(f"Training model with P = {P}")
    autoencoder = create_model(P)

    # Fit the model on the training data
    autoencoder.fit(
        x_train.reshape(-1, m * n),  # Flatten input images
        x_train,                     # Use 2D images as targets
        epochs=10,
        batch_size=64,
        shuffle=True,
        validation_data=(x_test.reshape(-1, m * n), x_test)  # Use 2D images for validation targets
    )
    models[P] = autoencoder

# Function to calculate Peak Signal-to-Noise Ratio (PSNR)
def calculate_psnr(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if mse == 0:  # Prevent division by zero
        return 100
    MAX_I = 1.0  # Maximum pixel intensity in the normalized images
    return 10 * np.log10((MAX_I * MAX_I)/ (mse))

# Dictionary to store average PSNR for each model
average_psnr = {}

# Calculate the average PSNR for each P value
for P in P_values:
    psnr_list = []

    # Predict the decompressed images from the model
    decoded_imgs = models[P].predict(x_test.reshape(-1, m*n))

    # Calculate PSNR for each test image
    for i in range(len(x_test)):
        psnr = calculate_psnr(x_test[i], decoded_imgs[i])
        psnr_list.append(psnr)

    # Calculate and store the average PSNR
    average_psnr[P] = np.mean(psnr_list)

# Print the average PSNR values
print(average_psnr)

# Select the first 10 test images
first_10_test_images = x_test[:10]

# Decompress the images using the trained models
decompressed_images = {}
for P in P_values:
    decompressed_images[P] = models[P].predict(first_10_test_images.reshape(-1, m*n)).reshape(-1, m, n)

# Plotting the images
fig, axes = plt.subplots(4, 10, figsize=(20, 8))  # 4 rows, 10 columns

# Plot original images
for i, ax in enumerate(axes[0]):
    ax.imshow(first_10_test_images[i], cmap='gray')
    ax.axis('off')
    if i == 0:
        ax.set_title("Original")

# Plot decompressed images for each P
for row, P in enumerate(P_values, start=1):
    for i, ax in enumerate(axes[row]):
        ax.imshow(decompressed_images[P][i], cmap='gray')
        ax.axis('off')
        if i == 0:
            ax.set_title(f"P = {P}")

plt.tight_layout()
plt.show()

