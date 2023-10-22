import time
import csv
import datetime


def csv_to_list(tasks):
    with open('task_list.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        j = 0
        for row in reader:
            for _ in row:
                tasks.append(row[j])
                j += 1
    return tasks


def list_to_csv(data):
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
    for task in tasks:
        print(f"{n}. {task}")
        n += 1
    # Doesn't allow user to enter number outside or range
    while True:
        name = int(input("\nEnter Number to Complete: "))
        if name < n or name >= n:
            print("Invalid Task Number")
        else:
            data = list(tasks)
            data.remove(data[1 - name])
            break
    list_to_csv(data)
    print("Task Completed")


# copies csv file to list, removes tasks from list, writes list to csv file formatted
def rm_task(tasks):
    print()
    n = 1
    for task in tasks:
        print(f"{n}. {task}")
        n += 1
    # Doesn't allow user to enter number outside or range
    while True:
        name = input("\nEnter Number to Delete: ")
        if name == '':
            print("Input is empty, Please enter a valid number")
        elif int(name) >= 1 and int(name) >= n - 1:
            data = list(tasks)
            data.remove(data[int(name) - 1])
            break
        else:
            print("Invalid Task Number")
    list_to_csv(data)
    print("Task Deleted")


def main():
    print("\nPrioriTask")
    while True:
        tasks = []
        csv_to_list(tasks)
        current_datetime = datetime.datetime.now()

        print("\n" + current_datetime.strftime("%A")
              + ", " + current_datetime.strftime("%B")
              + " " + current_datetime.strftime("%d"))
        print("----------------------")
        print("0/5 Daily Tasks Completed\n")

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
                    print("\nNo Tasks to Delete\n")
                    time.sleep(.3)
            else:
                print("\nInvalid Input\n")


if __name__ == "__main__":
    main()
