#memasukkan nilai boolean
a1_3003 = input("Input nilai boolean-1 (True/False): ").strip().lower() == "true"
a2_3003 = input("Input nilai boolean-2 (True/False): ").strip().lower() == "true"

print("\nA1 = ", a1_3003)
print("A2 = ", a2_3003)

# Konjungsi: bernilai True jika keduanya True
hasil_3003 = a1_3003 and a2_3003
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil_3003)

# Disjungsi: bernilai True jika salah satunya True
hasil_3003 = a1_3003 or a2_3003
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil_3003)

# Negasi A1: mambalikan nilai A1
hasil_3003 = not a1_3003
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil_3003)

# Negasi A2: membalikan nilai A2
hasil_3003 = not a2_3003
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil_3003)

# XOR: bernilai True jika Kedua nilai berbeda
hasil_3003 = a1_3003 != a2_3003
print("\nDisjungsi eksklusif (XOR)")
print("A1 XOR A2 =", hasil_3003)