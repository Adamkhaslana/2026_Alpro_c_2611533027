# buat file dengan nama nested_for2_NIM.py
# buat program untuk perulangan dalam pyhton
# nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# program ini menggunakan fungsi input()

batas_3027 = int(input("masukkan nilai batas: "))
for i_3027 in range(1, batas_3027 + 1):
    for j_3027 in range(batas_3027 + 1):
        print("*", end=" ")
    print() # pindah ke baris berikutnya