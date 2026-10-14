import matplotlib.pyplot as plt

# Daftar titik: (x, y, label, warna RGB (0-255), ukuran s, marker)
# Posisi, ukuran, dan jumlah titik bebas diubah
titik = [
    (1, 2, 'A', (255, 0, 0),     80,  'o'),   # merah, lingkaran
    (3, 4, 'B', (0, 0, 255),     150, 's'),   # biru, persegi
    (5, 1, 'C', (0, 150, 0),     220, '^'),   # hijau, segitiga
    (4, 3, 'D', (255, 165, 0),   120, 'D'),   # oranye, belah ketupat
    (2, 5, 'E', (128, 0, 128),   300, '*'),   # ungu, bintang
]

# Fungsi konversi RGB 0-255 ke format matplotlib (0-1)
def rgb(warna):
    return tuple(c / 255 for c in warna)

# Pisahkan koordinat x dan y
x = [t[0] for t in titik]
y = [t[1] for t in titik]

plt.figure(figsize=(6, 5))

# Garis penghubung antar titik (digambar dulu, di bawah titik)
plt.plot(x, y, color=(0.4, 0.4, 0.4), linestyle='--',
         linewidth=1.5, zorder=1)

# Gambar tiap titik dengan warna, ukuran, dan marker masing-masing
for (xi, yi, lab, w, ukuran, mk) in titik:
    plt.scatter(xi, yi, color=rgb(w), s=ukuran, marker=mk,
                edgecolors='black', zorder=2)
    plt.annotate(f'{lab}({xi}, {yi})', (xi, yi),
                 xytext=(8, 8), textcoords='offset points',
                 fontsize=12, color=rgb(w))

# Atur tampilan grafik
plt.xlim(0, 6)
plt.ylim(0, 6)
plt.xticks(range(0, 7, 1))
plt.yticks(range(0, 7, 1))
plt.xlabel('x')
plt.ylabel('y')
plt.title('Visualisasi Beberapa Titik pada Bidang Koordinat')
plt.grid(True, linestyle='--', alpha=0.7)

# Simpan gambar (harus SEBELUM plt.show())
plt.savefig('titik_koordinat.png', dpi=300, bbox_inches='tight')
plt.show()