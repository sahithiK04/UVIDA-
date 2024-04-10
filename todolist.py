tasks = {}

def add_task():
    task = input("Enter the task: ")
    tasks[task] = False
    print("Task added!")

def mark_task_done():
    task = input("Enter the task to mark as done: ")
    if task in tasks:
        tasks[task] = True
        print("Task marked as done!")
    else:
        print("Task not found!")


def show_tasks():
    print("Tasks:")
    for task, done in tasks.items():
        status = "Done" if done else "Not done"
        print(f"{task}: {status}")

while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. Mark Task as Done")
    print("3. Show Tasks")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        mark_task_done()
    elif choice == '3':
        show_tasks()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")