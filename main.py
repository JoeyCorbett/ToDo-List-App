import time
import csv
import datetime

#tasks_done


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
    while True:
        choice = input("Due Date?(y/n): ")
        if choice.lower() == 'y':
            current_date = datetime.datetime.now()
            print("Current Date: ", current_date.strftime("%m/%d"))
            due_date = input("Due Date(MM/DD): ")
            name_date = str((name + " | Due: " + due_date))
            break
        elif choice.lower() == 'n':
            name_date = str(name)
            break
        else:
            print("Invalid Entry")
            continue
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
        if name == '':
            print("Input is empty, Please enter a valid number")
        elif 1 <= int(name) < n:
            data = list(tasks)
            data.remove(data[1 - name])
            break
        else:
            print("Invalid Task number")
    list_to_csv(data)
    print("Task Completed\nGreat Job!")


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
        choice = input("Are you sure? y/n: ").lower()
        if choice == 'n':
            continue
        elif choice == 'y':
            pass
        else:
            print("Invalid Input, please try again")
        if name == '':
            print("Input is empty, Please enter a valid number")
        elif 1 <= int(name) < n:
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
        print("----------------------\n")
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
