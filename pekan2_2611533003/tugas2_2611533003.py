from typing import Final

BATAS_LULUS: Final = 75.0

print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")

nama_3003 = input("Masukkan Nama Mahasiswa : ")
jenis_kelamin_3003 = input("Masukkan Jenis Kelamin (L/P): ")
umur_3003 = int(input("Masukkan Umur : "))
skor_3003 = float(input("Masukkan Skor Tes Awal : "))

alamat_3003 = """Jl. Kampus Unand,
Kecamatan Pauh,
Kota Padang"""

id_token_3003 = 100 + 3j

lulus_3003 = skor_3003 >= BATAS_LULUS

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print(f"Nama Mahasiswa : {nama_3003} | Tipe: {type(nama_3003)}")
print(f"Jenis Kelamin : {jenis_kelamin_3003} | Tipe: {type(jenis_kelamin_3003)}")
print(f"Alamat Domisili:\n{alamat_3003} | Tipe: {type(alamat_3003)}")
print(f"Umur : {umur_3003} tahun | Tipe: {type(umur_3003)}")
print(f"Skor Tes Awal : {skor_3003} | Tipe: {type(skor_3003)}")
print(f"ID Token Sinyal: {id_token_3003} | Tipe: {type(id_token_3003)}")

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
print(f"Batas Minimum Nilai: {BATAS_LULUS}")
print(f"Apakah Dinyatakan Lulus?: {lulus_3003} | Tipe: {type(lulus_3003)}")
