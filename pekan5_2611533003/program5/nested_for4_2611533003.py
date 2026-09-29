tinggi_3003 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_3003 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_3003 = tinggi_3003
    c_3003 = a_3003
    lebar_3003 = (2 * tinggi_3003) - 2

    for i_3003 in range(1, tinggi_3003 + 1):
        b_3003 = c_3003 + 1

        for j_3003 in range(1, lebar_3003 + 1):

            #Baris atas dan bawah
            if i_3003 == 1 or i_3003 == tinggi_3003:
                 if j_3003 == 1 or j_3003 == lebar_3003:
                    print("#", end="")
                 else:
                    print("=", end="")
            #Baris isi
            else:
                if j_3003 == 1 or j_3003 == lebar_3003:
                    print("|", end="")
                else:
                    if j_3003 == c_3003:
                        print("<", end="")
                    elif j_3003 == b_3003:
                        print(">", end="")
                    elif j_3003 == (lebar_3003 - c_3003):
                        print("<", end="")
                    elif j_3003 == (lebar_3003 - c_3003 + 1):
                        print(">", end="")
                    elif j_3003 > b_3003 and j_3003 < (lebar_3003 - c_3003):
                        print(".", end="")
                    else:
                        print(" ", end="")
        print()

        # Logika asli Java
        a_3003 -= 2

        if a_3003 <= 0:
            c_3003 = (-a_3003) + 2
        else:
            c_3003 = a_3003
