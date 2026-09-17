# Buat file dengan nama lainnya_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan Fungsi input()
# Program operator keanggotaan dan identitas

print("=======================")
print("1. OPERATOR KEANGGOTAAN")
print("=======================")

# Input beberapa data yang dipisahkan dengan koma
input_data_3027 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_3027 = [int(angka_3027.strip()) for angka_3027 in input_data_3027.split(",")]

nilai_dicari_3027 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_3027 = nilai_dicari_3027 in data_3027
print("\nOperator keanggotaan IN")
print(nilai_dicari_3027, "in", data_3027, "=", hasil_3027)

# Operator not in
hasil_3027 = nilai_dicari_3027 not in data_3027
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_3027, "not in", data_3027, "=", hasil_3027)

print("\n=====================")
print("2. OPERATOR IDENTITAS")
print("=====================")

# objek1_3027 menggunakan list dari input pengguna
objek1_3027 = data_3027

# objek2_2001 merujuk pada objek yang sama dengan objek1_3027
objek2_3027 = objek1_3027

# objek3_3027 memiliki isi sama, tetapi merupakan objek baru
objek3_3027 = data_3027.copy()

print("objek1_3027 =", objek1_3027)
print("objek2_3027 =", objek2_3027)
print("objek3_3027 =", objek3_3027)

# Operator is
hasil_3027 = objek1_3027 is objek2_3027
print("\nOperator identitas IS")
print("objek1_3027 is objek2_3027 =", hasil_3027)

# Operator is not
hasil_3027 = objek1_3027 is not objek3_3027
print("\nOperator identitas IS NOT")
print("objek1_3027 is not objek3_3027 =", hasil_3027)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1_3027 is objek3_3027 =", objek1_3027 is objek3_3027)
print("objek1_3027 == objek3_3027 =", objek1_3027 == objek3_3027)