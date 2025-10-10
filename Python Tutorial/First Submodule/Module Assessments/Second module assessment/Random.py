import random

numbers = [random.randint(1, 100) for _ in range(10)]
print("Unsorted list:", numbers)

for i in range(len(numbers) - 1):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)