# Buat file dengan nama bitwise_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angkal 1234
# Program ini menggunakan fungsi input()

print("\n===================")
print("3. OPERATOR BITWISE")
print("===================")

angka1_3027 = int(input("Masukkan angka bitwise-1: "))
angka2_3027 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1_3027 =", angka1_3027, "| biner", bin(angka1_3027))
print("angka2_3027 =", angka2_3027, "| biner", bin(angka2_3027))

# Bitwise AND
hasil_3027 = angka1_3027 & angka2_3027
print("\nBitwise AND (&)")
print(angka1_3027, "&", angka2_3027, "=", hasil_3027)
print("Biner hasil =", bin(hasil_3027))
print("Biner hasil (8 bit) =", format(hasil_3027, "08b"))

# Bitwise OR
hasil_3027 = angka1_3027 | angka2_3027
print("\nBitwise OR (|)")
print(angka1_3027, "|", angka2_3027, "=", hasil_3027)
print("Biner hasil =", bin(hasil_3027))
print("Biner hasil (8 bit) =", format(hasil_3027, "08b"))

# Bitwise XOR
hasil_3027 = angka1_3027 ^ angka2_3027
print("\nBitwise XOR (^)")
print(angka1_3027, "^", angka2_3027, "=", hasil_3027)
print("Biner hasil =", bin(hasil_3027))
print("Biner hasil (8 bit) =", format(hasil_3027, "08b"))

# Bitwise NOT
hasil_3027 = ~angka1_3027
print("\nBitwise NOT (~)")
print("~", angka1_3027, "=", hasil_3027)
print("Biner hasil =", bin(hasil_3027))
print("Biner hasil (8 bit) =", format(hasil_3027, "08b"))

# Bitwise geser kiri
jumlah_geser_3027 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_3027 = angka1_3027 << jumlah_geser_3027
print("\nBitwise geser kiri (<<)")
print(angka1_3027, "<<", jumlah_geser_3027, "=", hasil_3027)
print("Biner hasil =", bin(hasil_3027))
print("Biner hasil (8 bit) =", format(hasil_3027, "08b"))

# Bitwise geser kanan
hasil_3027 = angka1_3027 >> jumlah_geser_3027
print("\nBitwise geser kanan (>>)")
print(angka1_3027, ">>", jumlah_geser_3027, "=", hasil_3027)
print("Biner hasil =", bin(hasil_3027))
print("Biner hasil (8 bit) =", format(hasil_3027, "08b"))