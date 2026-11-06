import os
import matplotlib.pyplot as plt

# Daftar titik (vertex) tiga jenis poligon
segitiga  = [(1, 1), (4, 1), (2.5, 4)]
persegi   = [(5, 1), (8, 1), (8, 4), (5, 4)]
segi_lima = [(1, 5), (4, 5), (5, 7), (2.5, 8.5), (0.5, 7)]

# Fungsi menggambar satu poligon (garis + isian warna)
def gambar_poligon(vertex, warna, nama):
    x = [p[0] for p in vertex + [vertex[0]]]
    y = [p[1] for p in vertex + [vertex[0]]]
    plt.plot(x, y, color=warna, marker='o', lw=2)    # garis poligon
    plt.fill(x, y, color=warna, alpha=0.4)           # isi area dengan warna
    cx = sum(p[0] for p in vertex) / len(vertex)
    cy = sum(p[1] for p in vertex) / len(vertex)
    plt.text(cx, cy, nama, ha='center', va='center', fontweight='bold')

plt.figure(figsize=(7, 7))

gambar_poligon(segitiga,  'red',   'Segitiga')
gambar_poligon(persegi,   'blue',  'Persegi Panjang')
gambar_poligon(segi_lima, 'green', 'Segi Lima')

plt.xlim(0, 9)
plt.ylim(0, 9)
plt.grid(True, linestyle='--', alpha=0.7)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Tugas Praktikum: Tiga Jenis Poligon')
plt.xlabel('X')
plt.ylabel('Y')

# Simpan PNG di folder yang sama dengan file .py (folder praktikum)
folder = os.path.dirname(os.path.abspath(__file__))
plt.savefig(os.path.join(folder, 'hasilpoligon2.png'), dpi=300, bbox_inches='tight')
plt.show()