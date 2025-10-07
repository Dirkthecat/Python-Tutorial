class StudentDatabase:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age, course, grade):
        if student_id in self.students:
            print(f"Student with ID {student_id} already exists.")
        else:
            self.students[student_id] = {
                "Name": name,
                "Age": age,
                "Courses": {course: grade},
            }
            print(f"Student {name} added successfully.")

    def add_Course(self, student_id, course, grade):
        if student_id in self.students:
            if "Courses" not in self.students[student_id]:
                self.students[student_id]["Courses"] = {}
            self.students[student_id]["Courses"][course] = grade
            print(f"Course {course} with grade {grade} added for student ID {student_id}.")
        else:
            print(f"No student found with ID {student_id}.")

    def list_all_students(self):
        if not self.students:
            print("No students in the database.")
        else:
            for student_id, info in self.students.items():
                print(f"ID: {student_id}, Info: {info}") 
 
    def calculate_student_average(self, student_id):
        if student_id in self.students:
            grades = self.students[student_id]["Courses"].values()
            if grades:
                average = sum(grades) / len(grades)
                print(f"Average grade for student ID {student_id} is {average:.2f}.")
                return average
            else:
                print(f"No grades available for student ID {student_id}.")
                return None
        else:
            print(f"No student found with ID {student_id}.")
            return None 

    def calculate_course_average(self, course):
        total = 0
        count = 0
        for info in self.students.values():
            if "Courses" in info and course in info["Courses"]:
                total += info["Courses"][course]
                count += 1
        if count > 0:
            average = total / count
            print(f"Average grade across all students for course {course} is {average:.2f}.")
            return average
        else:
            print(f"No grades found for course {course}.")
            return None

    def get_student_count(self):
        return len(self.students)
    
    def get_students_by_course(self, course):
        return {sid: info for sid, info in self.students.items() if info["Course"] == course}
    
def main():
    db = StudentDatabase()

    while True:
        print("\n--- Student Database Menu ---")
        print("1. Add new student")
        print("2. Add new course and grade")
        print("3. Calculate student average grade")
        print("4. Calculate course average grade")
        print("5. List all students")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            course = input("Enter Course: ")
            grade = float(input("Enter Grade: "))
            db.add_student(student_id, name, age, course, grade)
        elif choice == '2':
            student_id = input("Enter Student ID: ")
            course = input("Enter Course: ")
            grade = float(input("Enter Grade: "))
            db.add_Course(student_id, course, grade)
        elif choice == '3':
            student_id = input("Enter Student ID: ")
            db.calculate_student_average(student_id)
        elif choice == '4':
            course = input("Enter Course: ")
            db.calculate_course_average(course)
        elif choice == '5':
            db.list_all_students()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()