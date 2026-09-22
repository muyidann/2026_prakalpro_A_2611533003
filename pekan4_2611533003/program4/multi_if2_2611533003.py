# Program ini menggunakan fungsi input()
# Program Menghitung Diskon Belanja

# Input dari user
total_belanja_3003 = float(input("Masukkan total belanja (Rp): "))

# Input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_3003 = input("Apakah Anda member? (y/t): ").strip().lower()
is_member = input_member_3003 in ["y", "ya"]

# Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_3003 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_3003 = input_promo_3003 in ["y", "ya"]

total_diskon_persen_3003 = 0

# Multi-IF terpisah: Setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja_3003 > 1000000:
    total_diskon_persen_3003 += 10  # Diskon belanja besar

if is_member:
    total_diskon_persen_3003 += 5  # Diskon member

if kode_promo_valid_3003:
    total_diskon_persen_3003 += 15  # Diskon voucher

# Menghitung nominal diskon dan total bayar
nominal_diskon_3003 = total_belanja_3003 * (total_diskon_persen_3003 / 100)
total_bayar_3003 = total_belanja_3003 - nominal_diskon_3003

# Output hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon  : {total_diskon_persen_3003}% (Rp {nominal_diskon_3003:,.0f})")
print(f"Total Bayar   : Rp {total_bayar_3003:,.0f}")

print(f"Total diskon yang Anda dapatkan: {total_diskon_persen_3003}%")
# Output: Total diskon yang Anda dapatkan: 30% jika belanja > 1 juta, member, dan kode promo valid