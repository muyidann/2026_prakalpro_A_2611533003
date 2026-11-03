height = int(input("Enter the height of the triangle: "))
for row in range(1, height + 1):
    for column in range(1, row + 1):
        print(column, end=" ")
    print()