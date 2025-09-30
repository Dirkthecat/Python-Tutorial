def load_tasks(todo_list):
    tasks = []
    try:
        with open(todo_list, 'r') as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        print(f"No existing to-do list found. A new one will be created.")
    except IOError:
        print(f"Error: Unable to read the file {todo_list}.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read the file {todo_list}.")
    return tasks

def save_tasks(todo_list, tasks):
    try:
        with open(todo_list, 'w') as file:
            for task in tasks:
                file.write(f"{task}\n")
    except IOError:
        print(f"Error: Unable to save tasks to the file {todo_list}.")

def add_task(tasks,task):
    tasks.append(task)
    print(f'Task "{task}" added.')

def remove_task(tasks, index):
    try:
        task = tasks.pop(index)
        print(f'Task "{task}" removed.')
    except IndexError:
        print("Error: Invalid task number: {index}.")

def view_tasks(tasks):
    if tasks:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("No tasks in the to-do list.")  

def main():
    todo_list = "todo.txt"
    tasks = load_tasks(todo_list)
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            task = input("Enter the task to add: ")
            add_task(tasks, task)
            save_tasks(todo_list, tasks)
        elif choice == '3':
            try:
                index = int(input("Enter the task number to remove: ")) - 1
                remove_task(tasks, index)
                save_tasks(todo_list, tasks)
            except ValueError:
                print("Error: Please enter a valid number.")
        elif choice == '4':
            print("Exiting To-Do List application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()


