print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")

n_3003 = int(input("Masukkan ukuran skala jam pasir (N): "))


# BORDER ATAS
print("#", end="")

for jumlah_3003 in range(1):
    for karakter_3003 in range(4 * n_3003 + 5):
        print("=", end="")

print("#")


# FASE 1: JAM PASIR ATAS
for baris_3003 in range(n_3003, 0, -1):

    print("|", end="")
    print(" ", end="")

    # Spasi penyeimbang kiri
    for jumlah_3003 in range(1):
        for spasi_3003 in range(2 * (n_3003 - baris_3003)):
            print(" ", end="")

    # Deret angka mundur
    for jumlah_3003 in range(1):
        for angka_3003 in range(baris_3003, 0, -1):
            print(angka_3003, end=" ")

    # Poros kristal
    print("<*>", end="")

    # Deret angka maju
    for jumlah_3003 in range(1):
        for angka_3003 in range(1, baris_3003 + 1):
            print(" ", end="")
            print(angka_3003, end="")

    # Spasi penyeimbang kanan
    for jumlah_3003 in range(1):
        for spasi_3003 in range(2 * (n_3003 - baris_3003)):
            print(" ", end="")

    print(" ", end="")
    print("|")


# FASE 2: POROS TITIK PUSAT
print("|", end="")

for jumlah_3003 in range(1):
    for spasi_3003 in range(2 * n_3003 + 1):
        print(" ", end="")

print("<*>", end="")

for jumlah_3003 in range(1):
    for spasi_3003 in range(2 * n_3003 + 1):
        print(" ", end="")

print("|")


# FASE 3: JAM PASIR BAWAH
for baris_3003 in range(1, n_3003 + 1):

    print("|", end="")
    print(" ", end="")

    # Spasi penyeimbang kiri
    for jumlah_3003 in range(1):
        for spasi_3003 in range(2 * (n_3003 - baris_3003)):
            print(" ", end="")

    # Deret angka mundur
    for jumlah_3003 in range(1):
        for angka_3003 in range(baris_3003, 0, -1):
            print(angka_3003, end=" ")

    # Poros kristal
    print("<*>", end="")

    # Deret angka maju
    for jumlah_3003 in range(1):
        for angka_3003 in range(1, baris_3003 + 1):
            print(" ", end="")
            print(angka_3003, end="")

    # Spasi penyeimbang kanan
    for jumlah_3003 in range(1):
        for spasi_3003 in range(2 * (n_3003 - baris_3003)):
            print(" ", end="")

    print(" ", end="")
    print("|")


# BORDER BAWAH
print("#", end="")

for jumlah_3003 in range(1):
    for karakter_3003 in range(4 * n_3003 + 5):
        print("=", end="")

print("#")