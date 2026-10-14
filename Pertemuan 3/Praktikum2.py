import matplotlib.pyplot as plt

# 1. Titik-titik poligon (tambah segi enam dan segi delapan)
segitiga   = [(1, 1), (4, 1), (2.5, 4)]
persegi    = [(6, 1), (8, 1), (8, 3), (6, 3)]
segi_lima  = [(1, 5), (2, 7), (4, 7), (5, 5), (3, 4)]
segi_enam  = [(8.5, 6.5), (7.75, 7.8), (6.25, 7.8),
              (5.5, 6.5), (6.25, 5.2), (7.75, 5.2)]
segi_delapan = [(13, 6), (12.41, 7.41), (11, 8), (9.59, 7.41),
                (9, 6), (9.59, 4.59), (11, 4), (12.41, 4.59)]

# Pisahkan koordinat x dan y
def get_xy(titik):
    x = [p[0] for p in titik]
    y = [p[1] for p in titik]
    return x, y

# Fungsi menggambar poligon
def gambar_poligon(titik, nama, warna, marker='o', lebar_garis=2,
                   garis=True, isian=True, label_koordinat=True):
    x, y = get_xy(titik)

    # 2. Isian saja / garis saja (atur dengan True/False)
    if isian:
        plt.fill(x, y, color=warna, alpha=0.3)
    if garis:
        # 3. Warna, ketebalan garis, dan jenis marker bisa diubah
        plt.plot(x + [x[0]], y + [y[0]], color=warna,
                 linestyle='-', linewidth=lebar_garis, marker=marker)

    # 4. Label koordinat di setiap titik
    if label_koordinat:
        for (xi, yi) in titik:
            plt.annotate(f'({xi}, {yi})', (xi, yi),
                         xytext=(4, 6), textcoords='offset points',
                         fontsize=8, color=warna)

    # Nama bentuk di atas poligon
    cx = sum(x) / len(x)
    plt.text(cx, max(y) + 0.5, nama, ha='center',
             fontsize=11, fontweight='bold', color=warna)

# Buat figur
plt.figure(figsize=(10, 7))

# Gambar semua bentuk (setiap bentuk punya warna, tebal, marker berbeda)
gambar_poligon(segitiga,     'Segitiga',    'red',     marker='o', lebar_garis=2)
gambar_poligon(persegi,      'Persegi',     'blue',    marker='s', lebar_garis=3)
gambar_poligon(segi_lima,    'Segi Lima',   'green',   marker='^', lebar_garis=2)
gambar_poligon(segi_enam,    'Segi Enam',   'purple',  marker='D', lebar_garis=2.5,
               isian=False)                       # garis saja
gambar_poligon(segi_delapan, 'Segi Delapan', 'orange', marker='*', lebar_garis=1.5,
               garis=False, label_koordinat=False)  # isian saja

# Atur tampilan
plt.xlim(0, 14)
plt.ylim(0, 10)
plt.xticks(range(0, 15, 1))
plt.yticks(range(0, 11, 1))
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Visualisasi Poligon dengan Python')
plt.grid(True, linestyle='--', alpha=0.7)

# 5. Simpan ke PNG (sebelum plt.show())
plt.savefig('poligon.png', dpi=300, bbox_inches='tight')
plt.show()