import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define a cube
cube_vertices = np.array([
    [0, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
])

# Define edges to connect vertices of the cube
cube_edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Bottom face
    (4, 5), (5, 6), (6, 7), (7, 4),  # Top face
    (0, 4), (1, 5), (2, 6), (3, 7)   # Connecting edges
]

# Function to plot the cube
def plot_cube(vertices, edges, ax):
    for edge in edges:
        start = vertices[edge[0]]
        end = vertices[edge[1]]
        ax.plot3D([start[0], end[0]], [start[1], end[1]], [start[2], end[2]], color='blue')

# Function to apply transformations (translation, rotation, scaling)
def transform(vertices, transformation_matrix):
    transformed_vertices = np.dot(vertices, transformation_matrix.T)
    return transformed_vertices

# Apply transformations
translation_matrix = np.array([[1, 0, 0, 1],
                                [0, 1, 0, 1],
                                [0, 0, 1, 1],
                                [0, 0, 0, 1]])

rotation_matrix_x = np.array([[1, 0, 0, 0],
                                [0, np.cos(np.pi/4), -np.sin(np.pi/4), 0],
                                [0, np.sin(np.pi/4), np.cos(np.pi/4), 0],
                                [0, 0, 0, 1]])

rotation_matrix_y = np.array([[np.cos(np.pi/4), 0, np.sin(np.pi/4), 0],
                                [0, 1, 0, 0],
                                [-np.sin(np.pi/4), 0, np.cos(np.pi/4), 0],
                                [0, 0, 0, 1]])

rotation_matrix_z = np.array([[np.cos(np.pi/4), -np.sin(np.pi/4), 0, 0],
                                [np.sin(np.pi/4), np.cos(np.pi/4), 0, 0],
                                [0, 0, 1, 0],
                                [0, 0, 0, 1]])

scaling_matrix = np.array([[2, 0, 0, 0],
                            [0, 1.5, 0, 0],
                            [0, 0, 0.5, 0],
                            [0, 0, 0, 1]])

parallel_projection_matrix = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1]
])
perspective_projection_matrix = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, -0.001],
    [0, 0, 0, 1]
])

translated_cube = transform(cube_vertices, translation_matrix)
rotated_x_cube = transform(cube_vertices, rotation_matrix_x)
rotated_y_cube = transform(cube_vertices, rotation_matrix_y)
rotated_z_cube = transform(cube_vertices, rotation_matrix_z)
scaled_cube = transform(cube_vertices, scaling_matrix)
parallel_cube = transform(cube_vertices, parallel_projection_matrix)
perspective_cube = transform(cube_vertices, perspective_projection_matrix)
# Visualize the cube after transformations
fig = plt.figure(figsize=(10, 8))

ax1 = fig.add_subplot(231, projection='3d')
plot_cube(cube_vertices, cube_edges, ax1)
ax1.set_title('original cube')

ax2 = fig.add_subplot(232, projection='3d')
plot_cube(translated_cube, cube_edges, ax2)
ax2.set_title('Translated Cube')

ax3 = fig.add_subplot(233, projection='3d')
plot_cube(rotated_x_cube, cube_edges, ax3)
ax3.set_title('Rotated 45° around X-axis')

ax4 = fig.add_subplot(234, projection='3d')
plot_cube(rotated_y_cube, cube_edges, ax4)
ax4.set_title('Rotated 45° around Y-axis')

ax5 = fig.add_subplot(235, projection='3d')
plot_cube(rotated_z_cube, cube_edges, ax5)
ax5.set_title('Rotated 45° around Z-axis')

ax6 = fig.add_subplot(236, projection='3d')
plot_cube(scaled_cube, cube_edges, ax6)
ax6.set_title('Scaled Cube')
plt.show()

fig = plt.figure(figsize=(10, 8))

ax1 = fig.add_subplot(131, projection='3d')
plot_cube(cube_vertices, cube_edges, ax1)
ax1.set_title('original cube')

ax2 = fig.add_subplot(132, projection='3d')
plot_cube(parallel_cube, cube_edges, ax2)
ax2.set_title('parallel projection')

ax3 = fig.add_subplot(133, projection='3d')
plot_cube(perspective_cube, cube_edges, ax3)
ax3.set_title('perspective projection')

plt.tight_layout()
plt.show()
