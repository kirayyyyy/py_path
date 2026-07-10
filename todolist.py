choice = 1
tasks = []
while 0 < choice < 4:
    choice = int(input("1. Add task\n2. Show tasks\n3. Remove task\n4. Exit\nchoose: "))
    if choice == 1:
        task = input("Enter a task: ")
        tasks.append(task)
    if choice == 2:
        print("Tasks:")
        for task in tasks:
            print (task)
    if choice == 3: 
        for task in tasks:
            print (task)
        print ("Task to remove")
        taskrm = (input("choose : "))
        tasks.remove(taskrm)
    elif choice == 4:
        print("Goodbye!")
        break