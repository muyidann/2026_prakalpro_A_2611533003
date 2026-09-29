batas_3003 = int(input("Masukkan nilai batas: "))
for line_3003 in range(1, batas_3003 + 1):
    for j in range(1, (-1 * line_3003 + batas_3003) + 1):
        print(".", end="")
    print(line_3003)