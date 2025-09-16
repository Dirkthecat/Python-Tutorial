def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
count = int(input("number of terms in Fibonacci sequence:"))
if count <= 0:
    print("Error, indicate positive integer.")
else:
    for i in range(count):
        print(fibonacci(i))