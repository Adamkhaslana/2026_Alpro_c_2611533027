# ============================================================
# TUGAS 4 ALGORITMA DAN PEMROGRAMAN
# Sistem Loket Terpadu & Audit Transaksi Ekspedisi Wahana
# Nama : Fairuz Ar Rasyd
# NIM  : 2611533027
# ============================================================

print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# Input data pengunjung
nama_pengunjung_3027 = input("Masukkan Nama Pengunjung        : ")
umur_3027 = int(input("Input umur anda                 : "))
sim_3027 = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()
jumlah_tiket_3027 = int(input("Masukkan jumlah tiket           : "))

# If tunggal untuk validasi jumlah tiket
if jumlah_tiket_3027 <= 0:
    print("Peringatan: Kuota tiket tidak valid!")
    print("Program Selesai")
    exit()

# Pilihan paket wahana
print("\nPilihan Paket Wahana (1-5):")
print(" 1. Safari Rimba         (Rp 50,000)")
print(" 2. Arung Jeram          (Rp 75,000)")
print(" 3. Motor ATV Ekstrim    (Rp 120,000)")
print(" 4. Roller Coaster Kilat (Rp 100,000)")
print(" 5. All-Access VIP       (Rp 220,000)")

paket_3027 = int(input("Masukkan nomor paket (1-5) : "))

# Match-case untuk menentukan wahana dan harga
match paket_3027:
    case 1:
        nama_wahana_3027 = "Wahana Safari Rimba"
        harga_satuan_3027 = 50000

    case 2:
        nama_wahana_3027 = "Wahana Arung Jeram"
        harga_satuan_3027 = 75000

    case 3:
        nama_wahana_3027 = "Wahana Motor ATV Ekstrim"
        harga_satuan_3027 = 120000

    case 4:
        nama_wahana_3027 = "Wahana Roller Coaster Kilat"
        harga_satuan_3027 = 100000

    case 5:
        nama_wahana_3027 = "Wahana All-Access VIP"
        harga_satuan_3027 = 220000

    case _:
        print("Paket wahana tidak valid!")
        print("Program Selesai")
        exit()

# Validasi kelayakan pengendara
print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

if paket_3027 == 3:
    if umur_3027 >= 17 and sim_3027 == 'y':
        status_akses_3027 = "Anda sudah dewasa dan boleh mengendarai ATV sendiri."

    elif umur_3027 >= 17 and sim_3027 != 'y':
        status_akses_3027 = "Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur)."

    elif umur_3027 < 17 and sim_3027 == 'y':
        status_akses_3027 = "Identitas tidak valid: Belum cukup umur memiliki SIM."

    else:
        status_akses_3027 = "Anda belum cukup umur dan tidak boleh bawa motor ATV."

else:
    if umur_3027 >= 10:
        status_akses_3027 = "Anda memenuhi syarat umur untuk wahana ini."
    else:
        status_akses_3027 = "Anda belum cukup umur untuk wahana ini."

print("Status Akses:", status_akses_3027)

# Input data diskon
is_member_3027 = input("\nApakah Anda member? (y/t)      : ").strip().lower()
kode_promo_valid_3027 = input("Apakah kode promo valid? (y/t) : ").strip().lower()

# Menghitung subtotal
subtotal_3027 = harga_satuan_3027 * jumlah_tiket_3027

# Total diskon awal
total_diskon_persen_3027 = 0

# Multi-if terpisah untuk diskon akumulatif
if subtotal_3027 >= 200000:
    total_diskon_persen_3027 += 10

if is_member_3027 in ['y', 'ya']:
    total_diskon_persen_3027 += 5

if kode_promo_valid_3027 in ['y', 'ya']:
    total_diskon_persen_3027 += 15

if jumlah_tiket_3027 >= 5:
    total_diskon_persen_3027 += 5

# Menghitung nominal diskon dan total pembayaran
nominal_diskon_3027 = subtotal_3027 * (total_diskon_persen_3027 / 100)
total_bayar_3027 = subtotal_3027 - nominal_diskon_3027

# Evaluasi bonus layanan
if total_bayar_3027 > 300000:
    catatan_layanan_3027 = "Selamat! Anda berhak mendapatkan Souvenir Gratis."
else:
    catatan_layanan_3027 = "Terima kasih telah berkunjung."

# Menampilkan rincian pembayaran
print("\n--- Rincian Pembayaran ---")
print(f"Wahana          : {nama_wahana_3027}")
print(f"Harga Satuan    : Rp {harga_satuan_3027:,.0f}")
print(f"Jumlah Tiket    : {jumlah_tiket_3027}")
print(f"Subtotal Belanja: Rp {subtotal_3027:,.0f}")
print(
    f"Total Diskon    : {total_diskon_persen_3027}% "
    f"(Rp {nominal_diskon_3027:,.0f})"
)
print(f"Total Bayar     : Rp {total_bayar_3027:,.0f}")
print(f"Catatan Layanan : {catatan_layanan_3027}")

print("\nProgram Selesai")