tinggi_3027 = int(input("Masukkan tinggi segitiga: "))

for i_3027 in range(1, tinggi_3027 + 1):
    for j_3027 in range(tinggi_3027 - i_3027):
        print(" ", end="")
    for a_3027 in range(i_3027):
        print("*", end=" ")
    print()