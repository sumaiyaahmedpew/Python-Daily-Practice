# problem_24 Image Filter Simulation
import numpy as np

def brighten(img, value=50):
    return np.clip(img + value, 0, 255)

def darken(img, value=50):
    return np.clip(img - value, 0, 255)

def transpose_filter(img):
    return img.T

# Example Run
image = np.array([[300, 120, 150],
                  [200, 220, 240],
                  [50,  80,  90]])

print("Original:\n", image)
print("\nBrightened:\n", brighten(image))
print("\nDarkened:\n", darken(image))
print("\nTransposed:\n", transpose_filter(image))
