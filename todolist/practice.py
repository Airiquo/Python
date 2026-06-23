tasks = {"workout": True, "study": False, "play": True}

task = input("Enter task: ")
tasks[task] = False

#selects index
choice = int(input("Select Task to mark as done: "))

#grabs task of the index in the dictionary
chosen_task = list(tasks.items())[choice - 1]

#converted into a key to access the task (0,1)
task_key = chosen_task[0]

#manipulates the boolean of the task 
tasks[task_key] = True


for index, (task, progress) in enumerate(tasks.items(), start = 1):
    if(progress == True):
        print(f"No. {index} |Task: {task} marked as done")  
    else:
        print(f"No. {index} |Task: {task} marked as pending") 
    