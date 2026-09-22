# Program ini menggunakan fungsi input()

umur_3003 = int(input("Masukkan umur Anda: "))
sim_3003 = input("Apakah Anda memiliki SIM c (y/t): ")[0]

if umur_3003 >= 17 and sim_3003 == 'y':
    print("Anda sudah dewasa dan boleh bawa motor")

if umur_3003 >= 17 and sim_3003 != 'y':
    print("Anda sudah dewasa tapi tidak boleh bawa motor")

if umur_3003 < 17 and sim_3003 != 'y':
    print("Anda belum cukup umur bawa motor")

if umur_3003 < 17 and sim_3003 == 'y':
    print("Anda belum cukup umur punya SIM")