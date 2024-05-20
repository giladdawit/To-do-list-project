def display_menu():
    print("To do list Menu")
    print("1. Add Task: ")
    print("2. Mark task as completed: ")
    print("3. Delete task: ")
    print("4. View task: ")

#Function to add a task to the do list

def add_task(todo_list):
    task = input("Enter a task: ")
    todo_list.append(task) # adds the task entered to the todo_list list
    print("Task added sucessfully")

#Function to mark tasks done as completed

def mark_completed(todo_list):
    print("Tasks: ") # print tasks as a header

    for i, task in enumerate(todo_list):# enumerate loops through and assignd a number to each task in the to do list
         print(f"{i+1.} {task}") # since index starts at 0 "i+1" makes the first index start at 1
    choice = int(input("Enter a task number to mark as completed: "))
    todo_list[choice-1] += " (Completed)"
    print ("Task marked as completed")

# Function to delete task 

def delete_task(todo_list):
    print("Tasks: ")

    for i, task in enumerate(todo_list):
        print(f"{i+1}. task")
    choice = int(input("Enter a number to delete a task: "))
    del todo_list[choice-1]
    print("Task has been sucessfully deleted")


def view_tasks(todo_list):
    print("Tasks: ")
    for task in todo_list:
        print(task)

#Calling out the functions
def main():
    todo_list = []
    while True: #loops infinitley until the function breaks
        display_menu() # This line calls a function named display_menu() to show a menu of options to the user.
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_task(todo_list)
        elif choice == 2:
            mark_completed(todo_list)
        elif choice == 3:
            delete_task(todo_list)
        elif choice == 4:
            view_tasks(todo_list)
        elif choice == 5: 
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()







