import time


def add_task(tasks):
    name = input("\nTask Name: ")
    tasks.append(name)
    return tasks


def rm_task(tasks):
    print()
    n = 1
    for task in tasks:
        print(f"{n}. {task}")
        n += 1
    name = int(input("\nEnter Number to Delete: "))
    print(tasks)
    tasks.remove(tasks[1-name])
    return tasks


def main():
    tasks = []
    while True:
        print("\nToDo App\n")
        if len(tasks) > 0:
            for task in tasks:
                print(f"• {task}")
        else:
            print("• No Tasks")
        print("\n1. Add Tasks\n2. Complete Tasks\n3. Delete Tasks\n")
        while True:
            choice = input("Enter Number: ")
            if choice == "1":
                add_task(tasks)
                break
                # elif choice == 2:

            elif choice == "3":
                if len(tasks) > 0:
                    rm_task(tasks)
                    break
                else:
                    print("\nNo Tasks to Remove\n")
                    time.sleep(.3)
            else:
                print("\nInvalid Input")
                time.sleep(.5)


if __name__ == "__main__":
    main()
