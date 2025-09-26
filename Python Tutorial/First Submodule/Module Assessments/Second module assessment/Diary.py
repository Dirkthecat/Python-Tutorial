import datetime
Diary_file = "Val's_Diary.txt"
def add_entry():
    try:
        entry = input("Enter your diary entry: ")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(Diary_file, "a") as file:
            file.write(f"{timestamp} - {entry}\n")
        print("Entry added.")
    except PermissionError:
        print("Error: Permission denied when trying to write to the diary file.")

def view_entries():
    try:
        with open(Diary_file, "r") as file:
            entries = file.readlines()
            if entries:
                print("Diary Entries:")
                for entry in entries:
                    print(entry.strip())
            else:
                print("No entries found.")
    except FileNotFoundError:
        print("No diary file found. Start by adding an entry.")
    except PermissionError:     
        print("Error: Permission denied when trying to read the diary file.")
def main():
    while True:
        print("\nDiary Menu:")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")
        if choice == '1':
            add_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            print("Exiting diary.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



