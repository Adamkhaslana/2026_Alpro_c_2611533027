#buat file dengan nama Boolean_2611533027.py
# nama variabel ditambah 4 digit terakhir dari NIM terakhir contoh: nilai_3027
# deklarasi variabel dengan tipe data boolean
is_lulus = True
is_cumlaude = True

# Mengunakan Boolean
nilai = 85
batas_lulus = 75

# Menentukan nilai Boolean dari kondisi
status_kelulusan = nilai >= batas_lulus # Hasilnya akan True

print("=== Check kelulusan ===")
print("Nilai:", nilai)
print("Apakah lulus?:", status_kelulusan)
if is_lulus and is_cumlaude:
    print("Selamat, Anda lulus dengan predikat Cum Laude!")