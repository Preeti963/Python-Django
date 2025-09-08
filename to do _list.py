#  To-Do List Program

tasks = []

while True:
    """
    1. Add Task
    2. View Tasks
    3. Remove Task
    4. Exit
    """

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

    elif choice == "3":
        task_no = int(input("Enter task number to remove: "))
        if 0 < task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number!")

    elif choice == "4":
        print("Thank you")
        break
    else:
        print("Invalid choice! Try again.")
