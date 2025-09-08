start_year = int(input("Enter birth/start year:  "))
end_year = int(input("Enter the current year:  "))
age = end_year - start_year
if age < 0:
    print("Age cannot be negative.")
else:
    print(f"The age is {age} years.")
