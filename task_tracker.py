import json

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)

        return tasks

    except FileNotFoundError:
        return []            

tasks = load_tasks()

def show_menu():
    print("1 - Add task")
    print("2 - Show tasks")
    print("3 - Mark task as done")
    print("4 - Delete task")
    print("0 - Exit")

def add_task(tasks):
    title = input("Enter task title: ")

    task = {"title": title, "done": False}

    tasks.append(task)

    save_tasks(tasks)

    print("Task added")

def show_tasks(tasks):

    if tasks == []:
        print("No tasks")
        return

    for index, task in enumerate(tasks, start=1):
        if task["done"] == True:
            status = "[x]"
        else:
            status = "[ ]"

        print(f'{index}. {status} {task["title"]}')

def mark_task_done(tasks):

    if tasks == []:
        print("No tasks")
        return

    show_tasks(tasks)

    try:
        task_number = int(input("Enter task number: "))

        index = task_number - 1

        if index < 0 or index >= len(tasks):
            print("Wrong task number")
            return

        tasks[index]["done"] = True

        save_tasks(tasks)

        print(f'Task marked as done: {tasks[index]["title"]}')

    except ValueError:
        print("Please enter a number")

def delete_task(tasks):
    if tasks == []:
        print("No tasks")
        return

    show_tasks(tasks)

    try:
        task_number = int(input("Enter task number: "))

        index = task_number - 1

        if index < 0 or index >= len(tasks):
            print("Wrong task number")
            return

        deleted_task = tasks.pop(index)

        save_tasks(tasks)

        print(f'Task deleted: {deleted_task["title"]}')

    except ValueError:
        print("Please enter a number")                                                           

def run_app():
    while True:
        show_menu()

        choice = input("Choose option: ")

        if choice == "0":
            print("Goodbye!")
            break

        elif choice == "1":
            add_task(tasks)

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            mark_task_done(tasks)

        elif choice == "4":
            delete_task(tasks)            

        else:
            print("Wrong choice")

        print()

if __name__ == "__main__":
    run_app()