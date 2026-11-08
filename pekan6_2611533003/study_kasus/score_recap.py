PASS_SCORE = 60
EXCELLENT_SCORE = 85

n = int(input("Number of students: "))

while n < 1:
    print("Invalid student count!")
    n = int(input("Number of students: "))

total = 0
passed = 0
excellent_count = 0
highest = 0

for i in range(1, n + 1):
    print(f"\nStudent {i}")

    score = int(input("Enter score: "))

    while score < 0 or score > 100:
        print("Invalid score!")
        score = int(input("Enter score: "))

    total += score

    if score >= PASS_SCORE:
        passed += 1

    if score >= EXCELLENT_SCORE:
        excellent_count += 1

    if score > highest:
        highest = score

average = total / n

print("\n===== CLASS SCORE RECAP =====")
print("Total score:", total)
print("Average score:", round(average, 2))
print("Passed:", passed)
print("Excellent count:", excellent_count)
print("Highest score:", highest)