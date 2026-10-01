# buat file dengan nama nested_for3_NIM.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_3027 = int(input("Masukkan nilai batas: "))
for i_3027 in range(batas_3027 + 1):
    for j_3027 in range(batas_3027 + 1):
        print(i_3027 + j_3027, end=" ")
    print() # pindah ke baris berikutnya