
tasks = []
def show_tasks():
    if not tasks:
        print("add your list")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' has been added.")

def update_task():
    
    show_tasks()
    task_num = int(input("Enter the no. of the task you want to update: "))
    if 1 <= task_num <= len(tasks):
        new_task = input("Enter the new task: ")
        tasks[task_num - 1] = new_task
        print(f"Task {task_num} has been updated.")
    else:
        print("Invalid task number.")

def delete_task():
    show_tasks()
    task_num = int(input("Enter the number of the task you want to delete: "))
    if 1 <= task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task}' has been deleted.")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("1. Show tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("GO AHEAD!")
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()
