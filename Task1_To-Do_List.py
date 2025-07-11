def main():
    todo_list = []
    while True:
        print("\n===To-do List===")
        print("1. Add Task")
        print("2. Show Task")
        print("3. Done")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if choice == '1':
            print()
            num_task = int(input("How many tasks do you want to add: "))
            for i in range(num_task):
                task_desc = input("Enter the task: ")
                todo_list.append({"task": task_desc, "Done": False})
                print("Task added!")

        elif choice == '2':
            print("\nTasks")
            if not todo_list:
                print("No tasks to show.")
            for index, t in enumerate(todo_list):
                status = "Done" if t["Done"] else "Not Done"
                print(f"{index + 1}. {t['task']} - {status}")

        elif choice == '3':
            if not todo_list:
                print("No tasks to mark as done.")
                continue
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(todo_list):
                todo_list[task_index]["Done"] = True
                print("Done!")
            else:
                print("Invalid task number.")

        elif choice == '4':
            print("Goodbye")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()