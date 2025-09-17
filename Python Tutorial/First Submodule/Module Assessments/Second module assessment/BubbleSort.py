def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-1-i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
random_numbers = [99, 5, 23, 37, 86, 52, 17]
print("Random Numbers: ", random_numbers)
bubble(random_numbers)
print("Ascending order: ", random_numbers)