import matplotlib.pyplot as plt

# Fungsi bantu: membuat 4 titik persegi panjang dari 2 sudut
def kotak(x1, y1, x2, y2):
    return [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]

# Fungsi bantu: menggambar poligon (isian + garis tepi)
def poligon(titik, isi, tepi='black', lw=2, z=1):
    x = [p[0] for p in titik]
    y = [p[1] for p in titik]
    plt.fill(x, y, facecolor=isi, edgecolor=tepi, linewidth=lw, zorder=z)

# Fungsi bantu: jendela dengan garis silang di tengah
def jendela(x1, y1, x2, y2):
    poligon(kotak(x1, y1, x2, y2), 'yellow', 'black', 2, z=3)
    xm, ym = (x1 + x2) / 2, (y1 + y2) / 2
    plt.plot([xm, xm], [y1, y2], color='black', linewidth=1.5, zorder=4)
    plt.plot([x1, x2], [ym, ym], color='black', linewidth=1.5, zorder=4)

# 1. Koordinat empat sudut badan rumah
badan = kotak(2, 0, 8, 3.7)

# 2. Tiga titik utama atap (kiri, puncak, kanan), dibuat tebal
atap = [(1.7, 3.5), (5, 7), (8.3, 3.5), (8, 3.7), (5, 6.3), (2, 3.7)]

# 3. Pintu dan jendela
pintu = kotak(4.5, 0, 5.6, 2.4)

plt.figure(figsize=(8, 6))

# Cerobong asap (digambar paling bawah agar tertutup atap)
poligon(kotak(7, 4.5, 7.6, 6.4), 'darkred', 'black', 2, z=1)
poligon(kotak(6.9, 6.4, 7.7, 6.6), 'white', 'black', 2, z=1)

# Badan rumah
poligon(badan, 'white', 'black', 2, z=2)

# Atap
poligon(atap, 'darkred', 'black', 2, z=3)

# Pintu + gagang pintu
poligon(pintu, 'darkred', 'black', 2, z=3)
plt.plot([4.55], [1], 'o', color='yellow', markeredgecolor='black', zorder=4)

# Jendela (3 buah)
jendela(2.8, 1.5, 3.8, 2.7)    # kiri bawah
jendela(6.2, 1.5, 7.2, 2.7)    # kanan bawah
jendela(4.4, 4.1, 5.6, 5.2)    # atas (di bawah atap)

# 5. Ubah koordinat di atas untuk melihat perubahan bentuk
plt.xlim(0, 10)
plt.ylim(0, 8)
plt.xticks(range(0, 11, 1))
plt.yticks(range(0, 9, 1))
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Mini Project: Rumah dari Koordinat')
plt.grid(True, linestyle='--', alpha=0.5, zorder=0)

plt.savefig('rumah.png', dpi=300, bbox_inches='tight')
plt.show()