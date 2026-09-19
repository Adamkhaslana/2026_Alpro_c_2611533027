print ("\n=== SISTEM TRANSAKSI TOKO ===")

nama_3027 = input("Masukkan Nama Pelanggan: ")
status_3027 = input("Masukkan Status Pelanggan (member/nonmember): ")
total_belanja_3027 = int(input("Masukkan Total Belanja : "))
jumlah_barang_3027 = int(input("Masukkan Jumlah Barang : "))
promo_3027 = input("Masukkan Kode Promo : ")

 #========================================
 #  ======DATA TRANSAKSI======
 # =======================================


print("\n=== DATA TRANSAKSI ===")
print("Nama Pelanggan                     : ",nama_3027)
print("Status Pelanggan (member/nonmember): ", status_3027)
print(f"Total Belanja                      :  Rp{total_belanja_3027}")
print("Jumlah Barang                      : ", jumlah_barang_3027)
print("Kode Promo                         : ", promo_3027)

#=========================================
#=========HASIL VALIDASI================
#=========================================

kode_promo_3011 = ["HIDUP IF", "HIDUP FTI", "JALAN SEHAT"]

syarat_total_3027 = total_belanja_3027 >=200000
syarat_jumlah_barang_3027 = jumlah_barang_3027 >=3
valid_status_3027 = status_3027 == "member"
valid_promo_3027 = promo_3027 in kode_promo_3011 


print("\n=== HASIL VALIDASI ===")
print(f"Belanja >= Rp200000                : {syarat_total_3027}") 
print(f"Jumlah Barang >= 3                 : {syarat_jumlah_barang_3027}")
print(f"Status Member                      : {valid_status_3027}")
print(f"Kode Promo Tersedia                : {valid_promo_3027}")
print(f"Mendapatkan Diskon                 : {syarat_jumlah_barang_3027 or syarat_total_3027}")
print(f"Mendapatkan Promo                  : {valid_promo_3027}")

#=========================================
#  =====HASIL PERHITUNGAN============
#=========================================

print("\n=== HASIL PERHITUNGAN ===")
print(f"Diskon                             : Rp{int(0.15 * total_belanja_3027)}")
print(f"Total Pembayaran                   : Rp{int(total_belanja_3027 - 0.15 * total_belanja_3027)}")
print(f"Rata-rata Harga Barang             : Rp{int((total_belanja_3027 - 0.15 * total_belanja_3027) // jumlah_barang_3027)}")

#=========================================
#=========HAK AKSES PELANGGAN===========
#=========================================
 
print("\n=== HAK AKSES PELANGGAN ===")
print("Kode Hak Akses                     : ...")
print(f"Member Access                      : {status_3027 == "member"}")
print(f"Promo Access                       : {promo_3027 in kode_promo_3011}")
print("Free Shipping Access               : ...")

#=========================================
#=========OPERASI BITWISE===============
#=========================================


print("\n=== OPERASI BITWISE ===")

print("\n=== Kode Status Transaksi ===")

#KODE STATUS
#0001 = member
#0010 = total belanja >= Rp 200000
#0100 = jumlah barang >= 3
#1000 = promo

#menggunakan OR (|)
kode_transaksi_3027 =  int(valid_status_3027) << 0 | int(syarat_total_3027) << 1 | int(syarat_jumlah_barang_3027) << 2 | int(valid_promo_3027) << 3
kode_referensi_3027 = int(valid_status_3027) << 0 | int(syarat_total_3027) << 1 | int(valid_promo_3027) << 3

print(f"{format(int(valid_status_3027) << 0, "04b")} | {format(int(syarat_total_3027) << 1, "04b")} | {format(int(syarat_jumlah_barang_3027) << 2, "04b")} | {format(int(valid_promo_3027) << 3, "04b")}")
print(f"Kode Biner   : {format(kode_transaksi_3027, "04b")}") 
print(f"Kode Desimal : {kode_transaksi_3027}")

#====================================
#========PEMERIKSAAN STATUS=========
#====================================

print("\n=== Pemeriksaan Status ===")


print("\nCek Member")

#menggunakan and (&)

print(f"{format(kode_transaksi_3027, "04b")} & {format(int(valid_status_3027) << 0, "04b")}")
print(f"Hasil Biner   : {format((kode_transaksi_3027) & int(valid_status_3027) << 0, "04b")}")
print(f"Hasil Desimal : {(kode_transaksi_3027) & int(valid_status_3027) << 0}") 

print("\nCek Promo")

print(f"{format(kode_transaksi_3027, "04b")} & {format(int(valid_promo_3027) << 3, "04b")}")
print(f"Hasil Biner   : {format((kode_transaksi_3027) & int(valid_promo_3027) << 3, "04b")}")
print(f"Hasil Desimal  : {(kode_transaksi_3027) & int(valid_promo_3027) << 3}")

#====================================
#======PERBANDINGAN STATUS==========
#============================================

print("\n=== Perbandingan Status ===")

 # menggunakan XOR (^)

print(f"Kode Transaksi : {format(kode_transaksi_3027, "04b")}")
print(f"Kode Referensi : {format(kode_referensi_3027, "04b")}")
print(f"{format(kode_transaksi_3027, "04b")} ^ {format(kode_referensi_3027, "04b")}")
print(f"Hasil Biner    : {format((kode_transaksi_3027) ^ (kode_referensi_3027))}")
print(f"Hasil Desimal  : {(kode_transaksi_3027) ^ (kode_referensi_3027)}")

#=====================================
#=======SHIFT GESER KIRI=============
#=====================================


print("\n=== Shift ===")

#bitwise kiri/ shift kiri (<<)

print(f"{format(kode_transaksi_3027,"04b")} << 1")
print(f"Hasil Biner   : {format((kode_transaksi_3027) << 1,"04b")}")
print(f"Hasil Desimal : {(kode_transaksi_3027) << 1}") 
print("=== SELESAI ===")