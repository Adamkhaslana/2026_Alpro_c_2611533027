# buat file dengan nama jumlah_genap_NIM.py
# buat program untuk perulangan dalam pyhton
# nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# program ini menggunakan fungsi input()

ulang_3027 = int(input("masukkan nilai batas: "))

jumlah_3027 = 0
for i_3027 in range(1, ulang_3027 + 1):
    if i_3027 % 2 == 0:
        print(i_3027, end=" ")
        jumlah_3027 = jumlah_3027 + i_3027

        if i_3027 < ulang_3027:
            print(" + ", end="")
        else:
            print(" = ", end="")
print()
print("jumlah_3027 = ", jumlah_3027)