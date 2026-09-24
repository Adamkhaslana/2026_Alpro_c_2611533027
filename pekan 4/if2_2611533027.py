# Buat program dengan kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# program ini menggunakan fungsi input()

ipk_3027 = float(input("Input IPK Anda ="))

if ipk_3027 > 2.75:
    print("Anda Lulus Sangat Memuaskan Dengan IPK " + str(ipk_3027))
else:
    print("Anda Tidak Lulus")
print("progran Selesai")