import sys

def show_menu():
    print("\n" + "=" * 30)
    print("To do list manager")
    print("=" * 30)
    print("1-view list")
    print("2-add item")
    print("3-delete item")
    print("4-exit")
    print("=" * 30)

def add_task(tasks):
    task = input("\n enter the task").strip()
    if task:
        tasks.append(task)
        print("task has been added")
    else:
        print("task cannot be empty")

def view_task(tasks):
    if not tasks:
        print("\n your todo list is empty")
    else:
        print("\n_current tasks_")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}.{task}")

def delete_task(tasks):
    view_task(tasks)
    if not tasks:
        return
    try:
        choice = int(input("Enter number of task to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            print(f"removed: {removed}")
        else:
            print("invalid task number")
    except ValueError:
        print("enter valid number")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("choice option 1-4: ").strip()

        if choice == "1":
            view_task(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("bye")
            sys.exit()
        else:
            print("invalid selection")

if __name__ == "__main__":
    main()