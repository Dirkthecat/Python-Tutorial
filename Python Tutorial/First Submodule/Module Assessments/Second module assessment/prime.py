n = int(input("Enter ending value: "))
if n < 2:
    print("There are no prime numbers in this range.")
else:
    print(f"Prime numbers between 2 and {n}:")
    # as per Wikipedia, primality check using trial division tests if n is a multiple of any integer between 2 and the sqrt of n
    # upper bound of range is excluded, therefore must use n + 1
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break #stop loop
        if is_prime:
            print(num, end=" ")