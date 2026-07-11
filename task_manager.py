import os

#To-Do app
#App title
print("!! Welcome to To Do App !!")

FILENAME = "todo.txt"
Task_dict={} #Dictionary to save the To-Do items

def load_tasks():
    Task_dict.clear() #clears memory
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            lines = file.readlines()
            for index, line in enumerate(lines, start=1):
                clean_line = line.strip()
                if clean_line:  # Skip blank lines
                    Task_dict[index] = clean_line

# Function to save dictionary items to text file
def save_tasks():
    with open(FILENAME, "w") as file:
        for task in Task_dict.values():
            file.write(task + "\n")

# Load existing tasks when app starts
load_tasks()

def add_item():  # function created to add to dict, once item is added
    uint = input("Enter task: ").strip()  # ask input
    if uint:
        index = len(Task_dict) + 1  # counter for item index
        Task_dict[index] = uint
        save_tasks()  # save to text file
        print(f"Task '{uint}' added")
    else:
        print("Task cannot be empty")


while True: #loop the question-options of To-Do list#
    print("\nPlease select the following- \n1. Add task \n2. View tasks \n3. Remove tasks \n4. exit")

    try: #to save from wrong input crashes
        uin=int(input("Enter (1/2/3/4): "))
        # add a task
        if uin==1:
            add_item()

        #view tasks
        elif uin==2:
            if not Task_dict:
                print("Your To-Do list is empty!")
            else:
                for key, task in Task_dict.items():
                    print(f"{key}. {task}")

        #remove tasks
        elif uin==3:
            if not Task_dict:
                print("No tasks to remove!")
            else:
                for key, task in list(Task_dict.items()):
                    print(f"{key}. {task}")

                # input from user -for item to be removed
                rem_item_input=int(input("select item to remove: "))
                rem_task=str(Task_dict.pop(rem_item_input, None)) #new dict with remaining items

                if rem_task:
                    print(f"{rem_task} removed")

                    #Re-index remaining tasks
                    Task_dict = {
                        new_idx: task
                        for new_idx, task in enumerate(Task_dict.values(), start=1)
                        }
                    save_tasks() #saves the new list to text file
                else:
                    print("Invalid task number.")

        elif uin == 4: #exit the app
            print("Goodbye!")
            break

        else: #user enters anything else
            print("Please enter a valid choice (1, 2, 3, or 4).")

    except ValueError: #user enters anything else-crash save
        print("Invalid input! Please enter numbers only.")







