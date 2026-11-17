# Name     : M. Yiwanu Marhudan
# NIM      : 2611533003
# Question 4

phone = "082611533003"
masked = phone[:4] + "*" * (len(phone) - 7) + phone[-3:]
print(masked)