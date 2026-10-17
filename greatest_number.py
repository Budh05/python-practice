# Find the greatest of four numbers

numbers = []

for i in range(4):
    n = int(input(f"Enter number {i + 1}: "))
    numbers.append(n)

greatest = max(numbers)

print("The greatest number is:", greatest)