import numpy as np
import matplotlib.pyplot as plt

# Number of points (seeds) to plot
num_points = 1000

# Golden angle in radians (approximately 137.5 degrees)
golden_angle = np.pi * (3 - np.sqrt(5))  # This is about 2.399 radians

# Create an array of indices for the points
n = np.arange(num_points)

# Calculate the radius for each point (proportional to the square root of the index)
radius = np.sqrt(n)

# Calculate the angle for each point using the golden angle
theta = n * golden_angle

# Convert polar coordinates (radius, theta) to Cartesian coordinates (x, y)
x = radius * np.cos(theta)
y = radius * np.sin(theta)

# Create the plot
plt.figure(figsize=(8, 8), facecolor='tan')  # Set figure background to light gray
plt.scatter(x, y, s=30, c='black', alpha=0.8)

# Remove axes for a cleaner look
plt.axis('off')

# Ensure the aspect ratio is equal so the spiral looks circular
plt.gca().set_aspect('equal')

# Save the plot
plt.savefig('spiral.png', dpi=300, bbox_inches='tight')
plt.show()