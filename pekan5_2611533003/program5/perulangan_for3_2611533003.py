ulang_3003 = int(input("Masukkan jumlah perulangan: "))

jumlah_3003 = 0
for i in range(1, ulang_3003 + 1):
    print(i, end=" ")
    jumlah_3003 = jumlah_3003 + i

    if i < ulang_3003:
        print(" + ", end="")
    else:
        print(" = ", jumlah_3003, end="")
print()
print("Jumlah =", jumlah_3003)