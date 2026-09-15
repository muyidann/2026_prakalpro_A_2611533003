print("==================================")
print("1. OPERATOR KEANGGOTAAN")
print("==================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_3003 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_3003 = [int(angka.strip()) for angka in input_data_3003.split(",")]

nilai_dicari_3003 = int(input("Masukkan angka yang ingin dicari: "))

# Operator In
hasil_3003 = nilai_dicari_3003 in data_3003
print("\nOperator keanggotaan IN")
print(nilai_dicari_3003, "in", data_3003, "=", hasil_3003)

# Operator Not In
hasil_3003 = nilai_dicari_3003 not in data_3003
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_3003, "not in", data_3003, "=", hasil_3003)

print("\n==================================")
print("2. OPERATOR IDENTITAS")
print("==================================")

# objek1 menggunakan list dari input pengguna
objek1_3003 = data_3003

# objek2 menggunakan list dari input pengguna
objek2_3003 = objek1_3003

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_3003 = data_3003.copy()

print("objek1_3003 =", objek1_3003)
print("objek2_3003 =", objek2_3003)
print("objek3_3003 =", objek3_3003)

# Operator Is
hasil_3003 = objek1_3003 is objek2_3003
print("\nOperator identitas IS")
print("objek1_3003 is objek2_3003 =", hasil_3003)

# Operator Is Not
hasil_3003 = objek1_3003 is not objek3_3003
print("\nOperator identitas IS NOT")
print("objek1_3003 is not objek3_3003 =", hasil_3003)

# Membandingkan identitas dan nilai
print("\nMembandingkan identitas dan nilai:")
print("objek1_3003 is objek3_3003 =", objek1_3003 is objek3_3003)
print("objek1_3003 == objek3_3003 =", objek1_3003 == objek3_3003)