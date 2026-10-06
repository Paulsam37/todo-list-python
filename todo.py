# Simple To-Do List

tasks = []

while True:
    print("\n--- To-Do List ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == '2':
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == '3':
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid number.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
