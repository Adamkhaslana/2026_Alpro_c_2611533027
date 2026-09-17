# Buat file dengan nama aritmatika_NIM.py
# Buat program untuk operator aritmatika dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_3027 = int(input("Input angka-1: "))
angka2_3027 = int(input("Input angka-2: "))

# Penjumlahan
hasil_3027 = angka1_3027 + angka2_3027
print("\nOperator Penjumlahan")
print("Hasil =", hasil_3027)

# Pengurangan
hasil_3027 = angka1_3027 - angka2_3027
print("\nOperator Pengurangan")
print("Hasil =", hasil_3027)

# Perkalian
hasil_3027 = angka1_3027 * angka2_3027
print("\nOperator Perkalian")
print("Hasil =", hasil_3027)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_3027 != 10:
    hasil_3027 = angka1_3027 / angka2_3027
    print("\noperator Pembagian")
    print("Hasil =", hasil_3027)

    hasil_3027 = angka1_3027 // angka2_3027
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_3027)

    hasil_3027 = angka1_3027 % angka2_3027
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_3027)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# Pangkat
hasil_3027 = angka1_3027 ** angka2_3027
print("\nOperator Pangkat")
print("Hasil =", hasil_3027)