# Buat file dengan nama Konstanta_2611533027.py
# program ini menggunakan konstanta untuk menghitung luas lingkaran
# nama variabel ditambah 4 digit nim terakhir contoh: jari_3027

from typing import Final 
PI: Final = 3.14
print("pi: %f" (PI))
jari_3027 = float(input('Masukkan nilai jari-jari : '))
luas_3027 = PI * jari_3027 * jari_3027
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_3027, luas_3027))