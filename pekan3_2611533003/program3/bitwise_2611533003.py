print("\n==================================")
print("3. OPERATOR BITWISE")
print("==================================")

angka1_3003 = int(input("Masukkan angka bitwise-1: "))
angka2_3003 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner:")
print("Angka 1:", angka1_3003, "-| biner", bin(angka1_3003))
print("Angka 2:", angka2_3003, "-| biner", bin(angka2_3003))

# Bitwise AND
hasil_3003 = angka1_3003 & angka2_3003
print("\nBitwise AND (&)")
print(angka1_3003, "&", angka2_3003, "=", hasil_3003)
print("Biner hasil =", bin(hasil_3003))
print("Biner hasil (8 bit) =", format(hasil_3003, '08b'))

# Bitwise OR
hasil_3003 = angka1_3003 | angka2_3003
print("\nBitwise OR (|)")
print(angka1_3003, "|", angka2_3003, "=", hasil_3003)
print("Biner hasil =", bin(hasil_3003))
print("Biner hasil (8 bit) =", format(hasil_3003, '08b'))

# Bitwise XOR
hasil_3003 = angka1_3003 ^ angka2_3003
print("\nBitwise XOR (^)")
print(angka1_3003, "^", angka2_3003, "=", hasil_3003)
print("Biner hasil =", bin(hasil_3003))
print("Biner hasil (8 bit) =", format(hasil_3003, '08b'))

# Bitwise NOT
hasil_3003 = ~angka1_3003
print("\nBitwise NOT (~)")
print("~", angka1_3003, "=", hasil_3003)
print("Biner hasil =", bin(hasil_3003))
print("Biner hasil (8 bit) =", format(hasil_3003, '08b'))

# Bitwise geser kiri
jumlah_geser_3003 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_3003 = angka1_3003 << jumlah_geser_3003
print("\nBitwise Geser Kiri (<<)")
print(angka1_3003, "<<", jumlah_geser_3003, "=", hasil_3003)
print("Biner hasil =", bin(hasil_3003))
print("Biner hasil (8 bit) =", format(hasil_3003, '08b'))

# Bitwise geser kanan
hasil_3003 = angka1_3003 >> jumlah_geser_3003
print("\nBitwise Geser Kanan (>>)")
print(angka1_3003, ">>", jumlah_geser_3003, "=", hasil_3003)
print("Biner hasil =", bin(hasil_3003))
print("Biner hasil (8 bit) =", format(hasil_3003, '08b'))