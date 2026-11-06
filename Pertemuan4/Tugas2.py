import matplotlib.pyplot as plt
import numpy as np
import time

def bresenham_line(x1, y1, x2, y2):
    pixels = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    x, y = x1, y1
    if dx > dy:
        p = 2 * dy - dx
        for _ in range(dx + 1):
            pixels.append((x, y))
            if p >= 0:
                y += sy
                p += 2 * dy - 2 * dx
            else:
                p += 2 * dy
            x += sx
    else:
        p = 2 * dx - dy
        for _ in range(dy + 1):
            pixels.append((x, y))
            if p >= 0:
                x += sx
                p += 2 * dx - 2 * dy
            else:
                p += 2 * dx
            y += sy
    return pixels

# Contoh penggunaan
x1, y1 = 2, 1
x2, y2 = 5, 8

pixels = bresenham_line(x1, y1, x2, y2)

print("Koordinat pixel:", pixels)

# Visualisasi hasil
x_vals, y_vals = zip(*pixels)

plt.figure(figsize=(5, 7))
plt.plot([x1, x2], [y1, y2], 'b-', label='Garis ideal')
plt.scatter(
    x_vals, y_vals,
    c='red', s=100, marker='s',
    label='Pixel hasil Bresenham'
)

plt.xticks(range(0, 15))
plt.yticks(range(0, 15))
plt.grid(True, linestyle='--', alpha=0.5)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title(
    f'Implementasi Bresenham: Garis ({x1},{y1}) ke ({x2},{y2})'
)
plt.axis('equal')
plt.show()