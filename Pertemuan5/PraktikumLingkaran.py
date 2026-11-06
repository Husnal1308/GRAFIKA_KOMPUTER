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
    return points

# Gambar lingkaran (r = 5)
pts = midpoint_circle(0, 0, 5)
x, y = zip(*pts)
plt.figure(figsize=(5, 5))
plt.scatter(x, y, s=60, c='red')
plt.axis('equal')
plt.grid(True)
plt.title('Lingkaran (r = 5) - Midpoint Algorithm')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()