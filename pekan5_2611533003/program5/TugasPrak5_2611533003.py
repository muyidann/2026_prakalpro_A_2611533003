tinggi_3003 = int(input("Masukkan tinggi segitiga: "))

for i_3003 in range(1, tinggi_3003 + 1):
    print(" " * (tinggi_3003 - i_3003), end="")
    
    for j_3003 in range(i_3003):
        print("*", end=" ")
    
    print()