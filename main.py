import time

def add_task(tasks):
    name = input("\nTask Name: ")
    tasks.append(name)
    return tasks

def rm_task(tasks):
    n = 1
    for task in tasks:
        print(f"{n} {tasks}")
        n += 1
    name = int(input("Enter Task Number: "))


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
        choice = input("Enter Number: ")
        if choice == "1":
            add_task(tasks)
        #elif choice == 2:

        elif choice == "3":
            if len(tasks) > 0:
                rm_task(tasks)
            else:
                print("\nNo Tasks to Remove")
                time.sleep(1)



if __name__ == "__main__":
    main()






