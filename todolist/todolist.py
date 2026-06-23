tasks = {"workout": True, "study": False, "play": True}


menu = """ 
0. Quit
1. Add Task
2. Delete Task
3. Mark Task as Done/Pending
4. Show All Tasks
"""

print(menu)
loop = True

while loop:
    choice = input("Enter Choice: ")

    if choice == "0":
        print("Exiting Program....")
        break

    elif choice == "1":
        task = input("Enter task: ")
        tasks[task] = False

    elif choice == "2":
        delete = int(input("Enter Task to Delete: "))
        tasks_list.pop(delete - 1)

    elif choice == "3":
        #selects index
        choice = int(input("Select Task to mark as done: "))

        #grabs task of the index in the dictionary
        chosen_task = list(tasks.items())[choice - 1]

        #converted into a key to access the task (0,1)
        task_key = chosen_task[0]

        #manipulates the boolean of the task 
        tasks[task_key] = not tasks[task_key]

    elif choice == "4":
        for index, (task, progress) in enumerate(tasks.items(), start = 1):
            if(progress == True):
                print(f"No. {index} |Task: {task} marked as done")  
            else:
                print(f"No. {index} |Task: {task} marked as pending") 
            
    else:
        print("Exiting Program....")
        loop = False