# Name     : M. Yiwanu Marhudan
# NIM      : 2611533003
# Question 6

full_name = "M. Yiwanu Marhudan"
nim = "2610511023"

clean = full_name.strip()
space = clean.find(" ")

if space == -1:
    first_name = clean
else:
    first_name = clean[:space]

username = first_name.lower() + nim[-3:]

print(username)