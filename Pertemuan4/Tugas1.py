import numpy as np
import matplotlib.pyplot as plt
import time

def dda_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))
    x_inc = dx / steps
    y_inc = dy / steps
    x, y = x1, y1
    pixels = []
    for _ in range(steps + 1):
        pixels.append((round(x), round(y)))
        x += x_inc
        y += y_inc
    return pixels


# Contoh penggunaan
x1, y1 = 2, 1
x2, y2 = 5, 8
pixels = dda_line(x1, y1, x2, y2)
print("Koordinat pixel:", pixels)

# Visualisasi hasil
x_vals, y_vals = zip(*pixels)
plt.figure(figsize=(5, 5))
plt.plot([x1, x2], [y1, y2], 'b-', label='Garis ideal')
plt.scatter(x_vals, y_vals, c='red', s=100, marker='s',
            label='Pixel hasil DDA')
plt.xticks(range(0,8))
plt.yticks(range(0, 10))
plt.grid(True, linestyle='--', alpha=0.5)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title(f'Implementasi DDA: Garis ({x1},{y1}) ke ({x2},{y2})')
plt.show()