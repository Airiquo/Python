tasks_list = []
finished_tasks = []

menu = """ 
0. Quit
1. Add Task
2. Delete Task
3. Mark Task as Done
4. Show Pending Tasks
5. Show Done Tasks
"""

print(menu)
loop = True

while loop:
    choice = input("Enter Choice: ")

    if choice == "0":
        print("Exiting Program....")
        break

    elif choice == "1":
        task = input("Enter Task: ").strip()
        tasks_list.append(task)

    elif choice == "2":
        delete = int(input("Enter Task to Delete: "))
        tasks_list.pop(delete - 1)

    elif choice == "3":
        done = int(input("Enter Task to mark as done: "))
        print(tasks_list[done] + " | Marked as Done")
        finished_tasks.append(tasks_list.pop(done - 1))

    elif choice == "4":
        for index, task in enumerate(tasks_list, start = 1):
            print(f"{index}. {task}")

    elif choice == "5":
        for index, task in enumerate(finished_tasks, start = 1):
            print(f"{index}. {task}")
            
    else:
        print("Exiting Program....")
        loop = False