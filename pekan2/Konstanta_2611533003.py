from typing import Final
PI: Final = 3.14
print(" %f" % (PI))
jari_3003 = float(input("Masukkan jari-jari lingkaran: "))
luas_3003 = PI * jari_3003 * jari_3003
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_3003, luas_3003))