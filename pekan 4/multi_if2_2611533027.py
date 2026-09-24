# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()
# Program menghitung diskon belanja

# Input dari user
total_belanja_3027 = float(input("Masukkan Total Belanja (Rp): "))

# Input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_3027 = input("Apakah Anda Member? (y/t): ").strip().lower()
is_member_3027 = input_member_3027 in ["y", "ya"]

# Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_3027 = input("Apakah Kode Promo Valid (y/t): ").strip().lower()
kode_promo_valid_3027 = input_promo_3027 in ["y", "ya"]

total_diskon_persen_3027 = 0

# Multi-IF terpisah: Setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus
if total_belanja_3027 > 1000000:
    total_diskon_persen_3027 += 10 # Diskon belanja besar

if is_member_3027:
    total_diskon_persen_3027 += 5 # Diskon belanja member

if kode_promo_valid_3027:
    total_diskon_persen_3027 += 15 # Diskon belanja voucher

# Menghitung nominal diskon dan total bayar
nominal_diskon_3027 = total_belanja_3027 * (total_diskon_persen_3027 / 100)
total_bayar_3027 = total_belanja_3027 - nominal_diskon_3027

# Output hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon : {total_diskon_persen_3027}% (Rp {nominal_diskon_3027:,.0f})")
print(f"Total Bayar  : Rp {total_bayar_3027:,.0f}")

print(f"Total Diskon yang Anda Dapatkan: {total_diskon_persen_3027}%")
# Output: Total diskon yang anda dapatkan: 30% jika belanja > 1 juta, member, dan kode promo valid