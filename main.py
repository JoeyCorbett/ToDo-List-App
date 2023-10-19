import time
import csv


def csv_to_list(tasks):
    with open('task_list.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        j = 0
        for row in reader:
            for _ in row:
                tasks.append(row[j])
                j += 1
    return tasks


def add_task():
    name = input("\nTask Name: ")
    with open('task_list.csv', 'a', newline='') as csvfile:
        if csvfile.tell() == 0:
            csvfile.write(name)
        else:
            csvfile.write("," + name)
        print("Task Added")


def complete_task(tasks):
    print()
    n = 1
    for tasks in tasks:
        print(f"{n}. {tasks}")
        n += 1
    name = int(input("\nEnter Number to Complete: "))
    tasks.remove(tasks[1-n])
    return tasks


def rm_task(tasks):
    print()
    n = 1
    for task in tasks:
        print(f"{n}. {task}")
        n += 1
    # TODO: fix bug allowing user to enter number out of range
    name = int(input("\nEnter Number to Delete: "))
    data = list(tasks)
    data.remove(data[1-name])
    with open('task_list.csv', 'w', newline='') as csvfile:
        j = 0
        for x in data:
            if len(data) > 1:
                if j > 0:
                    csvfile.write(',' + x)
                else:
                    csvfile.write(x)
            else:
                csvfile.write(x)
            j += 1
    print("Task Deleted")


def main():
    while True:
        tasks = []
        csv_to_list(tasks)
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
                add_task()
                break
            elif choice == "2":
                if len(tasks) > 0:
                    complete_task(tasks)
                    break
                else:
                    print("\nNo Tasks to Complete\n")
                    time.sleep(.3)
            elif choice == "3":
                if len(tasks) > 0:
                    rm_task(tasks)
                    break
                else:
                    print("\nNo Tasks to Remove\n")
                    time.sleep(.3)
            else:
                print("\nInvalid Input\n")
                time.sleep(.5)


if __name__ == "__main__":
    main()
