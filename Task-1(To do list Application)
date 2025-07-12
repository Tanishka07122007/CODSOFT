tasks = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Update task")
    print("4. Remove task")
    print("5. Exit")

def show_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\n Your Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

            def add_task():
    task = input(" Enter the task to add: ")
  
tasks.append(task)
  
print(" Task added!")
   def update_task():
    show_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to update: "))
            if 1 <= task_num <= len(tasks):
                new_task = input("Enter the new task: ")
                tasks[task_num - 1] = new_task
                print(" Task updated!")
            else:
                print(" Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def remove_task():
    show_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f" Removed task: {removed}")
            else:
              print(" Invalid task number.")
        except ValueError:
            print(" Please enter a valid number.")
while True:
    show_menu()
    choice = input(" Enter your choice (1-5): ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        update_task()
    elif choice == '4':
        remove_task()
    elif choice == '5':
       
print(" Exiting To-Do List. Have a productive day!")
        break
    else:
       
print(" Invalid choice. Please choose between 1-5.")
