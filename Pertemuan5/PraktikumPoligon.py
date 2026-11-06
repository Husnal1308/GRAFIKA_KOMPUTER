import matplotlib.pyplot as plt

# Daftar titik (vertex) poligon (segi-lima)
vertex = [(1, 1), (4, 1), (5, 3), (3, 5), (1, 3)]

# Pisahkan koordinat x dan y
x = [p[0] for p in vertex + [vertex[0]]]
y = [p[1] for p in vertex + [vertex[0]]]

plt.figure(figsize=(6, 5))
plt.plot(x, y, 'b-', marker='o', lw=2)          # garis poligon
plt.fill(x, y, color='lightskyblue', alpha=0.4)  # isi area

plt.xlim(0, 6)
plt.ylim(0, 6)
plt.grid(True)
plt.gca().set_aspect('equal')
plt.title('Poligon (Segi-Lima)')
plt.xlabel('X')
plt.ylabel('Y')
plt.show() 