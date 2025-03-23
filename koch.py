import numpy as np
import matplotlib.pyplot as plt

def koch_segment(p1, p2, depth):
    if depth == 0:
        return [p1, p2]
    
    # Calculate points for the new triangle
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    
    # Divide segment into thirds
    a = p1 + np.array([dx, dy]) / 3
    c = p1 + np.array([dx, dy]) * 2 / 3
    
    # Middle point of the "bump" (rotated 60 degrees)
    angle = np.pi / 3  # 60 degrees
    b_x = a[0] + (c[0] - a[0]) * np.cos(angle) - (c[1] - a[1]) * np.sin(angle)
    b_y = a[1] + (c[0] - a[0]) * np.sin(angle) + (c[1] - a[1]) * np.cos(angle)
    b = np.array([b_x, b_y])
    
    # Recursively apply to each segment
    return (koch_segment(p1, a, depth - 1)[:-1] + 
            koch_segment(a, b, depth - 1)[:-1] + 
            koch_segment(b, c, depth - 1)[:-1] + 
            koch_segment(c, p2, depth - 1))

# Starting triangle vertices
side = 1.0
height = side * np.sqrt(3) / 2
vertices = np.array([[0, 0], [side / 2, height], [side, 0], [0, 0]])

# Generate the snowflake
depth = 4  # Higher depth = more detail (4-5 is good for clarity)
points = []
for i in range(3):
    segment = koch_segment(vertices[i], vertices[i + 1], depth)
    points.extend(segment)

# Convert to array for plotting
points = np.array(points)

# Plot the snowflake
plt.plot(points[:, 0], points[:, 1], 'b-')  # 'b-' for blue line
plt.gca().set_aspect('equal')  # Keep proportions
plt.axis('off')  # Clean image
plt.savefig('koch_snowflake.png', dpi=300, bbox_inches='tight')
plt.show()