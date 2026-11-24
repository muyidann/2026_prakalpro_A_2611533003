
LAST_DIGIT = 3
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []

for i in range(7):
    expense = int(input(f"Day {i + 1}: "))
    expenses.append(expense)

total = 0
highest = expenses[0]
highest_day = 1
days_above_limit = 0

for i in range(len(expenses)):
    total += expenses[i]

    if expenses[i] > highest:
        highest = expenses[i]
        highest_day = i + 1

    if expenses[i] > daily_limit:
        days_above_limit += 1

average = total / len(expenses)

print("Daily limit:", daily_limit)
print("Total:", total)
print(f"Average: {average:.1f}")
print(f"Highest: day {highest_day} ({highest})")
print("Days above limit:", days_above_limit)