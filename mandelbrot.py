import numpy as np
import matplotlib.pyplot as plt

# Set image size and boundaries
width, height = 800, 800
x_min, x_max = -2, 1
y_min, y_max = -1.5, 1.5

# Create coordinate grid
x = np.linspace(x_min, x_max, width)
y = np.linspace(y_min, y_max, height)
X, Y = np.meshgrid(x, y)
C = X + 1j * Y  # Complex numbers for each pixel

# Iterate to generate fractal
Z = np.zeros_like(C)
for i in range(100):  # Max iterations
    Z = Z**2 + C
    mask = np.abs(Z) > 4  # Escape condition
    Z[mask] = np.nan  # Mark escaped points

# Create figure with custom background
fig = plt.figure(facecolor='#FEEBE4')  # Dark purple background
ax = plt.axes()
ax.set_facecolor('#2A1A40')  # Match axes background

# Plot
plt.imshow(np.log(np.abs(Z)), cmap='viridis', extent=[x_min, x_max, y_min, y_max])
plt.axis('off')  # No axes for a clean image
plt.savefig('mandelbrot.png', dpi=300, bbox_inches='tight')

# Save with background color
plt.savefig('mandelbrot.png', dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.show()