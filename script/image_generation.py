import numpy as np
from PIL import Image

# Image size
width = 800
height = 800

# Create empty array (RGB)
image_array = np.zeros((height, width, 3), dtype=np.uint8)

for y in range(height):
    for x in range(width):
        r = (x % 256)
        g = (y % 256)
        b = ((x * y) % 256)

        image_array[y, x] = [r, g, b]

# Convert array to image
img = Image.fromarray(image_array)

# Save image
img.save("colorful_art.png")

print("🎨 Image generated: colorful_art.png")
