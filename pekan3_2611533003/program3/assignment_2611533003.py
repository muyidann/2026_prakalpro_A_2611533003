angka1_3003 = int(input("angka-1: "))
angka2_3003 = int(input("angka-2: "))

print("\nNilai awal angka1_3003 =", angka1_3003)
print("Nilai awal angka2_3003 =", angka2_3003)

# Assignment biasa
hasil_3003 = angka1_3003
print("\nAssignment biasa (=)")
print("hasil =", hasil_3003)

# Assignment penambahan
hasil_3003 = angka1_3003
hasil_3003 += angka2_3003
print("\nAssignment penambahan (+=)")
print("hasil =", hasil_3003)

# Assignment pengurangan
hasil_3003 = angka1_3003
hasil_3003 -= angka2_3003
print("\nAssignment pengurangan (-=)")
print("hasil =", hasil_3003)

# Assignment perkalian
hasil_3003 = angka1_3003
hasil_3003 *= angka2_3003
print("\nAssignment perkalian (*=)")
print("hasil =", hasil_3003)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_3003 != 0:
    hasil_3003 = angka1_3003
    hasil_3003 /= angka2_3003
    print("\nAssignment pembagian (/=)")
    print("hasil =", hasil_3003)

    #Operator tambahan
    hasil_3003 = angka1_3003
    hasil_3003 //= angka2_3003
    print("\nAssignment pembagian bulat (//=)")
    print("hasil =", hasil_3003)
    hasil_3003 = angka1_3003
    hasil_3003 %= angka2_3003
    print("\nAssignment sisa bagi (%=)")
    print("hasil =", hasil_3003)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assignment perpangkatan
hasil_3003 = angka1_3003
hasil_3003 **= angka2_3003
print("\nAssignment perpangkatan (**=)")
print("hasil =", hasil_3003)