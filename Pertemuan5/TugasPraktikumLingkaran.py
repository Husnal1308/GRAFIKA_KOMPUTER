import os
import matplotlib.pyplot as plt

def midpoint_circle(xc, yc, r):
    x, y = 0, r
    d = 1 - r
    points = []
    while x <= y:
        for px, py in [( x,  y), ( y,  x), (-x,  y), (-y,  x),
                       ( x, -y), ( y, -x), (-x, -y), (-y, -x)]:
            points.append((xc + px, yc + py))
        if d < 0:
            d = d + 2 * x + 3
        else:
            d = d + 2 * (x - y) + 5
            y -= 1
        x += 1
    return list(set(points))      # hapus titik duplikat

# Gambar lingkaran (r = 8)
r = 8
pts = midpoint_circle(0, 0, r)
x, y = zip(*pts)

plt.figure(figsize=(6, 6))
plt.scatter(x, y, s=60, c='red')
plt.gca().set_aspect('equal', adjustable='box')                          # skala X dan Y sama, agar bulat sempurna
plt.xlim(-r - 2, r + 2)
plt.ylim(-r - 2, r + 2)
plt.xticks(range(-r - 2, r + 3, 2))
plt.yticks(range(-r - 2, r + 3, 2))
plt.grid(True, linestyle='--', alpha=0.7)
plt.title(f'Lingkaran (r = {r}) - Midpoint Algorithm')
plt.xlabel('X')
plt.ylabel('Y')

# Simpan PNG di folder yang sama dengan file .py (folder praktikum)
folder = os.path.dirname(os.path.abspath(__file__))
plt.savefig(os.path.join(folder, 'hasillingkaran'), dpi=300, bbox_inches='tight')
plt.show()