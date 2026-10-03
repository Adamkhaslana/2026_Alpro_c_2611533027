print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK ===")
n_3027 = int(input("Masukkan ukuran n jam pasir (N): "))

lebar_3027 = 4 * n_3027 + 5   

print("#", end="")
for garis_3027 in range(lebar_3027):
    print("=", end="")
print("#")

for baris_3027 in range(n_3027, 0, -1):
    print("|", end="")
    print(" ", end="")

    for spasi_3027 in range(2 * (n_3027 - baris_3027)):
        print(" ", end="")

    for angka_3027 in range(baris_3027, 0, -1):
        print(angka_3027, end="")
        print(" ", end="")

    print("<*>", end="")

    for angka_3027 in range(1, baris_3027 + 1):
        print(" ", end="")
        print(angka_3027, end="")

    for spasi_3027 in range(2 * (n_3027 - baris_3027)):
        print(" ", end="")

    print(" ", end="")
    print("|", end="")
    print()

print("|", end="")
for spasi_3027 in range(2 * n_3027 + 1):
    print(" ", end="")
print("<*>", end="")
for spasi_3027 in range(2 * n_3027 + 1):
    print(" ", end="")
print("|", end="")
print()

for baris_3027 in range(1, n_3027 + 1):
    print("|", end="")
    print(" ", end="")

    for spasi_3027 in range(2 * (n_3027 - baris_3027)):
        print(" ", end="")

    for angka_3027 in range(baris_3027, 0, -1):
        print(angka_3027, end="")
        print(" ", end="")

    print("<*>", end="")

    for angka_3027 in range(1, baris_3027 + 1):
        print(" ", end="")
        print(angka_3027, end="")

    for spasi_3027 in range(2 * (n_3027 - baris_3027)):
        print(" ", end="")

    print(" ", end="")
    print("|", end="")
    print()

print("#", end="")
for garis_3027 in range(lebar_3027):
    print("=", end="")
print("#")