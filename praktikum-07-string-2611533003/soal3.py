# Name     : M. Yiwanu Marhudan
# NIM      : 2611533003
# Question 3

# A
text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])

# B
text = "M. Yiwanu Marhudan"
count = 0
for char in text.lower():
    if char in "aiueo":
        count += 1
print("Vowels:", count)