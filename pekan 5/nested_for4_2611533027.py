# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_3027 = int(input("Masukkan tinggi (bilangan genap, misal 10): "))

if tinggi_3027 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_3027 = tinggi_3027
    c_3027 = a_3027
    lebar_3027 = (2 * tinggi_3027) - 2

    for i_3027 in range(1, tinggi_3027 + 1):
        b_3027 = c_3027 + 1

        for j_3027 in range(1, lebar_3027 + 1):
            # Baris atas dan bawah
            if i_3027 == 1 or i_3027 == tinggi_3027:
                if j_3027 == 1 or j_3027 == lebar_3027:
                    print("#", end="")
                else:
                    print("=", end="")
            # Baris isi
            else:
                if j_3027 == 1 or j_3027 == lebar_3027:
                    print("|", end="")
                else:
                    if j_3027 == c_3027:
                        print("<", end="")
                    elif j_3027 == b_3027:
                        print(">", end="")
                    elif j_3027 == (lebar_3027 - c_3027):
                        print("<", end="")
                    elif j_3027 == (lebar_3027 - c_3027 + 1):
                        print(">", end="")
                    elif j_3027 > b_3027 and j_3027 < (lebar_3027 - c_3027):
                        print(".", end="")
                    else:
                        print(" ", end="")
        print()

        # Logika asli Java
        a_3027 -= 2

        if a_3027 <= 0:
            c_3027 = (-a_3027) + 2
        else:
            c_3027 = a_3027