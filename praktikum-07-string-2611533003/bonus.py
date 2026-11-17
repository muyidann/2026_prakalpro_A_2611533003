# Name     : M. Yiwanu Marhudan
# NIM      : 2611533003
# Question bonus

sentence = input("Masukkan kalimat: ")
clean = sentence.replace(" ", "").lower()

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")