import numpy as np
import matplotlib.pyplot as plt

# Define the three vertices of the starting triangle
vertices = np.array([[0, 0], [1, 0], [0.5, np.sqrt(3)/2]])

# Starting point (anywhere inside the triangle)
point = np.array([0.5, 0.3])

# Array to store all points
points = [point]

# Generate points using the chaos game
for _ in range(10000):  # More iterations = more detail
    vertex = vertices[np.random.randint(0, 3)]  # Pick a random vertex
    point = (point + vertex) / 2  # Move halfway toward it
    points.append(point)

# Convert points to array for plotting
points = np.array(points)

# Plot the fractal
plt.scatter(points[:, 0], points[:, 1], s=1, c='black')  # s=1 makes tiny dots
plt.gca().set_aspect('equal')  # Keep triangle proportional
plt.axis('off')  # No axes for a clean look
plt.savefig('sierpinski.png', dpi=300, bbox_inches='tight')  # Save as image
plt.show()