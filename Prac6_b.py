import numpy as np
import matplotlib.pyplot as plt

def translate(tx, ty):
    return np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])

def rotate(theta):
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    return np.array([
        [cos_theta, -sin_theta, 0],
        [sin_theta, cos_theta, 0],
        [0, 0, 1]
    ])

def scale(sx, sy):
    return np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])

def shear(kx, ky):
    return np.array([
        [1, kx, 0],
        [ky, 1, 0],
        [0, 0, 1]
    ])

# Define a square
square = np.array([
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1],
    [0, 0, 1]
])

# Apply transformations
translation_matrix = translate(2, 2)
rotation_matrix = rotate(np.pi/4)  # 45 degrees
scaling_matrix = scale(1.5, 1)
shearing_matrix = shear(0.5, 0)

translated_square = np.dot(square, translation_matrix.T)
rotated_square = np.dot(square, rotation_matrix.T)
scaled_square = np.dot(square, scaling_matrix.T)
sheared_square = np.dot(square, shearing_matrix.T)

# Get the maximum and minimum values of x and y coordinates
x_min = min(np.min(square[:, 0]), np.min(translated_square[:, 0]), np.min(rotated_square[:, 0]), np.min(scaled_square[:, 0]), np.min(sheared_square[:, 0]))
x_max = max(np.max(square[:, 0]), np.max(translated_square[:, 0]), np.max(rotated_square[:, 0]), np.max(scaled_square[:, 0]), np.max(sheared_square[:, 0]))
y_min = min(np.min(square[:, 1]), np.min(translated_square[:, 1]), np.min(rotated_square[:, 1]), np.min(scaled_square[:, 1]), np.min(sheared_square[:, 1]))
y_max = max(np.max(square[:, 1]), np.max(translated_square[:, 1]), np.max(rotated_square[:, 1]), np.max(scaled_square[:, 1]), np.max(sheared_square[:, 1]))

# Plot original and transformed squares
plt.figure(figsize=(12, 6))

plt.subplot(1, 5, 1)
plt.plot(square[:, 0], square[:, 1], '-o')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.title('Original Square')

plt.subplot(1, 5, 2)
plt.plot(translated_square[:, 0], translated_square[:, 1], '-o')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.title('Translated Square')

plt.subplot(1, 5, 3)
plt.plot(rotated_square[:, 0], rotated_square[:, 1], '-o')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.title('Rotated Square')

plt.subplot(1, 5, 4)
plt.plot(scaled_square[:, 0], scaled_square[:, 1], '-o')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.title('Scaled Square')

plt.subplot(1, 5, 5)
plt.plot(sheared_square[:, 0], sheared_square[:, 1], '-o')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.title('Sheared Square')

plt.tight_layout()
plt.show()


