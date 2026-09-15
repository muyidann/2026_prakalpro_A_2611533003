angka1_3003 = int(input("angka-1: "))
angka2_3003 = int(input("angka-2: "))

#Penjumlahan
hasil_3003 = angka1_3003 + angka2_3003
print("\nOperator penjumlahan")
print("hasil =", hasil_3003)

#Pengurangan
hasil_3003 = angka1_3003 - angka2_3003
print("\nOperator pengurangan")
print("hasil =", hasil_3003)

#Perkalian
hasil_3003 = angka1_3003 * angka2_3003
print("\nOperator perkalian")
print("hasil =", hasil_3003)

#Pembagian, pembagian bulat, dan sisa bagi
if angka2_3003 != 0:
    hasil_3003 = angka1_3003 / angka2_3003
    print("\nOperator pembagian")
    print("hasil =", hasil_3003)

    hasil_3003 = angka1_3003 // angka2_3003
    print("\nOperator pembagian bulat")
    print("hasil =", hasil_3003)

    hasil_3003 = angka1_3003 % angka2_3003
    print("\nOperator sisa bagi")
    print("hasil =", hasil_3003)
else:
    print("Angka kedua tidak boleh bernilai 0.")

#Pangkat
hasil_3003 = angka1_3003 ** angka2_3003
print("\nOperator pangkat")
print("hasil =", hasil_3003)