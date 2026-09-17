# Buat file dengan nama logika_NIM.py
# Nama variabel ditambah 4 digit NIM terakhir contoh: a1_1234
# program ini mengguankan fungsi input()
# program operator logika dalam python

# memasukan nilai boolean 
# Input tidak peka terhadap huruf besar dan kecil 
a1_3027 = input("Input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2_3027 = input("Input nilai boolean-2 (true/false): ").strip().lower() == "true"

print("\nA1 =", a1_3027)
print("A2 =", a2_3027)

# Konjungsi: bernilai True jika keduanya True
hasil_3027 = a1_3027 and a2_3027
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil_3027)

# Disjungsi: bernilai True jika salah satunya True
hasil_3027 = a1_3027 or a2_3027
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil_3027)

# Negasi A1: membalik nilai A1
hasil_3027 = not a1_3027
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil_3027)

# Negasi A2: membalik nilai A2
hasil_3027 = not a2_3027
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil_3027)

# XOR: bernilai True jika kedua nilai berbeda
hasil_2001 = a1_3027 != a2_3027
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil_3027)