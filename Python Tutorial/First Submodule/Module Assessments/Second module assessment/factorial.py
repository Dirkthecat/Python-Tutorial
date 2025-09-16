def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Calcuate factorial for:"))
if num <= 0:
    print("Error, input positive integer.")
else:
    print(f"The factorial of {num} is {factorial(num)}")