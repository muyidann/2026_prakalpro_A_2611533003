print("=== SISTEM TRANSAKSI TOKO ===")

nama_3003 = input("Masukkan Nama Pelanggan : ")
status_3003 = input("Masukkan Status Pelanggan (member/nonmember) : ").lower()
total_belanja_3003 = float(input("Masukkan Total Belanja : Rp"))
jumlah_barang_3003 = int(input("Masukkan Jumlah Barang : "))
kode_promo_3003 = input("Masukkan Kode Promo : ").upper()

syarat_belanja_3003 = total_belanja_3003 >= 200000
syarat_barang_3003 = jumlah_barang_3003 >= 3
status_member_3003 = status_3003 == "member"

daftar_promo_3003 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

promo_tersedia_3003 = kode_promo_3003 in daftar_promo_3003
promo_tidak_tersedia_3003 = kode_promo_3003 not in daftar_promo_3003

diskon_member_3003 = status_member_3003 and syarat_belanja_3003

promo_didapatkan_3003 = promo_tersedia_3003 and (syarat_belanja_3003 or syarat_barang_3003)

bukan_member_3003 = not status_member_3003

if diskon_member_3003:
    persentase_diskon_3003 = 0.10
else:
    persentase_diskon_3003 = 0.05 if syarat_belanja_3003 else 0

besar_diskon_3003 = total_belanja_3003 * persentase_diskon_3003

total_pembayaran_3003 = total_belanja_3003 - besar_diskon_3003

if jumlah_barang_3003 > 0:
    rata_rata_barang_3003 = total_belanja_3003 / jumlah_barang_3003
else:
    rata_rata_barang_3003 = 0

sisa_pembagian_3003 = int(total_belanja_3003) % jumlah_barang_3003 if jumlah_barang_3003 > 0 else 0


poin_3003 = 0
if status_member_3003:
    poin_3003 += int(total_pembayaran_3003 // 10000)

jumlah_barang_tersisa_3003 = jumlah_barang_3003
if promo_didapatkan_3003:
    jumlah_barang_tersisa_3003 -= 1

kode_1_3003 = ["HEMAT10"]
kode_2_3003 = ["HEMAT10"]

nilai_sama_3003 = kode_1_3003 == kode_2_3003
objek_sama_3003 = kode_1_3003 is kode_2_3003
objek_berbeda_3003 = kode_1_3003 is not kode_2_3003


kode_member_3003 = 1 if status_member_3003 else 0
kode_belanja_3003 = 2 if syarat_belanja_3003 else 0
kode_barang_3003 = 4 if syarat_barang_3003 else 0
kode_promo_3003 = 8 if promo_tersedia_3003 else 0

# Operator OR (|)
kode_status_3003 = (
    kode_member_3003
    | kode_belanja_3003
    | kode_barang_3003
    | kode_promo_3003
)

cek_member_3003 = kode_status_3003 & 1
cek_belanja_3003 = kode_status_3003 & 2
cek_barang_3003 = kode_status_3003 & 4
cek_promo_3003 = kode_status_3003 & 8

kode_referensi_3003 = 11
perbandingan_status_3003 = kode_status_3003 ^ kode_referensi_3003

kode_shift_3003 = kode_status_3003 << 1


member_access_3003 = bool(cek_member_3003)
promo_access_3003 = bool(cek_promo_3003)
free_shipping_access_3003 = syarat_belanja_3003 and syarat_barang_3003


print("\n=== DATA PELANGGAN ===")
print("Nama Pelanggan       :", nama_3003)
print("Status Pelanggan     :", status_3003)
print("Total Belanja        : Rp", total_belanja_3003)
print("Jumlah Barang        :", jumlah_barang_3003)
print("Kode Promo           :", kode_promo_3003)


print("\n=== HASIL VALIDASI ===")
print("Belanja >= Rp200000  :", syarat_belanja_3003)
print("Jumlah Barang >= 3   :", syarat_barang_3003)
print("Status Member        :", status_member_3003)
print("Kode Promo Tersedia  :", promo_tersedia_3003)
print("Mendapatkan Diskon   :", diskon_member_3003)
print("Mendapatkan Promo    :", promo_didapatkan_3003)


print("\n=== HASIL PERHITUNGAN ===")
print("Besarnya Diskon      : Rp", besar_diskon_3003)
print("Total Pembayaran     : Rp", total_pembayaran_3003)
print("Rata-rata Harga      : Rp", rata_rata_barang_3003)
print("Sisa Pembagian       :", sisa_pembagian_3003)


print("\n=== HAK AKSES PELANGGAN ===")
print("Kode Hak Akses       :", format(kode_status_3003, "04b"))
print("Member Access        :", member_access_3003)
print("Promo Access         :", promo_access_3003)
print("Free Shipping Access :", free_shipping_access_3003)
print("Poin Pelanggan       :", poin_3003)


print("\n=== OPERATOR IDENTITAS ===")
print("kode_1 == kode_2     :", nilai_sama_3003)
print("kode_1 is kode_2     :", objek_sama_3003)
print("kode_1 is not kode_2 :", objek_berbeda_3003)


print("\n=== OPERASI BITWISE ===")
print("Kode Status Transaksi")
print("0001 | 0010 | 0100 | 1000")

print("Kode Biner           :", format(kode_status_3003, "04b"))
print("Kode Desimal         :", kode_status_3003)

print("\n=== PEMERIKSAAN STATUS ===")

print("\nCek Member")
print(format(kode_status_3003, "04b"), "& 0001")
print("Hasil Biner         :", format(cek_member_3003, "04b"))
print("Hasil Desimal       :", cek_member_3003)

print("\nCek Belanja")
print(format(kode_status_3003, "04b"), "& 0010")
print("Hasil Biner         :", format(cek_belanja_3003, "04b"))
print("Hasil Desimal       :", cek_belanja_3003)

print("\nCek Jumlah Barang")
print(format(kode_status_3003, "04b"), "& 0100")
print("Hasil Biner         :", format(cek_barang_3003, "04b"))
print("Hasil Desimal       :", cek_barang_3003)

print("\nCek Promo")
print(format(kode_status_3003, "04b"), "& 1000")
print("Hasil Biner         :", format(cek_promo_3003, "04b"))
print("Hasil Desimal       :", cek_promo_3003)

print("\n=== PERBANDINGAN STATUS (XOR) ===")
print("Kode Transaksi      :", format(kode_status_3003, "04b"))
print("Kode Referensi      :", format(kode_referensi_3003, "04b"))
print(format(kode_status_3003, "04b"), "^",
      format(kode_referensi_3003, "04b"))
print("Hasil Biner         :", format(perbandingan_status_3003, "04b"))
print("Hasil Desimal       :", perbandingan_status_3003)

print("\n=== SHIFT ===")
print(format(kode_status_3003, "04b"), "<< 1")
print("Hasil Biner         :", format(kode_shift_3003, "b"))
print("Hasil Desimal       :", kode_shift_3003)

print("\n=== SELESAI ===")