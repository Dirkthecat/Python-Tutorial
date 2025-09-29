def read_grades(grade_tracker):
    grades = []
    try:
        with open(grade_tracker) as file:
            for line in file:
                try:
                    grades.append(float(line.strip()))
                except ValueError:
                    pass
        return grades
    except FileNotFoundError:
        print(f"Error: The file {grade_tracker} not found.")
        return []
    except PermissionError:
        print(f"Error: Permission denied when trying to read the file {grade_tracker}.")
        return []
    
def write_grades(grade_tracker, grades):
    try:
        with open(grade_tracker, "w") as file:
            for grade in grades:
                file.write(f"{grade}\n")
    except IOError:
        print("Error: Unable to save grades to the file.")

def add_grade(grade_tracker):
    try:
        grade = float(input("Enter the grade to add: "))
        if 0 <= grade <= 100:
            grades = read_grades(grade_tracker) 
            grades.append(grade)
            write_grades(grade_tracker, grades)
            print("Grade added.")
        else:
            print("Grade must be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a numeric grade.")

def view_grades(grade_tracker):
    grades = read_grades(grade_tracker)
    if grades:
        print("Grades:")
        for grade in grades:
            print(grade)
    else:
        print("No grades found.")

def calculate_average(grade_tracker):
    grades = read_grades(grade_tracker)
    if grades:
        average = sum(grades) / len(grades)
        print(f"Average Grade: {average:.2f}")
    else:
        print("No grades to calculate average.")

def main():
    grade_tracker = "grades.txt"
    while True:
        print("\nGrade Tracker Menu:")
        print("1. Add Grade")
        print("2. View Grades")
        print("3. Calculate Average")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")
        if choice == '1':
            add_grade(grade_tracker)
        elif choice == '2':
            view_grades(grade_tracker)
        elif choice == '3':
            calculate_average(grade_tracker)
        elif choice == '4':
            print("Exiting Grade Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
