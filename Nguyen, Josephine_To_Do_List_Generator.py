# Program allows user to create their own To-Do List. User can add a task and the due date, delete tasks,
# change due dates, look up tasks, and view their To-Do List.

def main():
    #Initialize an empty dictionary to store tasks and their due dates
    to_do_list = {
    }

    #Program name and description for user
    print("To-Do List Generator"
          "\nCreate a personal to-do list manager to organize your daily tasks! To get started, enter your name.")

    #Prompt user to input their name for personalizing their To-Do List
    user_name=input("\nName: ")

    #User inputs a task to add to their To-Do List and their updated list is displayed
    add_to_list(to_do_list)
    display_to_do_list(user_name, to_do_list)

    #User can continue to edit and review their To-Do List or exit the program
    print("\nTo edit and review your To-Do List, explore the options below.")
    display_to_do_list_menu()

    keep_going = input("\nTo continue type 'y' or 'n' to quit: ")
    while keep_going == "y":
        display_to_do_list_menu()
        user_selection = int(input("Select option (1-5): "))
        while user_selection < 1 or user_selection > 4:
            print("\nInvalid option. Please try again.")
            user_selection = int(input("Select option (1-5): "))
        if user_selection == 1:
            add_to_list(to_do_list)
            display_to_do_list(user_name, to_do_list)
        elif user_selection == 2:
            delete_from_list(to_do_list)
            display_to_do_list(user_name, to_do_list)
        elif user_selection == 3:
            change_due_date(to_do_list)
            display_to_do_list(user_name, to_do_list)
        elif user_selection == 4:
            look_up_task(to_do_list)
            display_to_do_list(user_name, to_do_list)
        else:
            quit()
        keep_going = input("\nType 'y' to continue or 'n' to quit: ")

def display_to_do_list_menu():
    #Show list of available actions the user can take
    print("\n\t1. Add to To-Do-List" +
    "\n\t2. Delete from To-Do List" +
    "\n\t3. Change Due Date" +
    "\n\t4. Look Up A Task")

def display_to_do_list(user_name,to_do_list):
    #Print the user's current To-Do List
    print(f"\n{user_name}'s To-Do List")
    print(to_do_list)

def add_to_list(to_do_list):
    #Prompt user for a task and due date, then add it to the To-Do list if it doesn't exist
    print("\nAdd To To-Do List")
    task = input("\tEnter task: ")
    due_date = input("\tEnter due date: ")

    if task in to_do_list:
        print("\nTask found.")
    else:
        to_do_list[task] = due_date
        print("\nTask added!")

def delete_from_list(to_do_list):
    #Prompt user for a task name and delete it if it exists in the To-Do List
    print("\nDelete From To-Do List")
    task = input("\tEnter task: ")
    if task in to_do_list:
        del to_do_list[task]
        print("\nTask deleted.")
    else:
        print("\nTask was not found.")

def change_due_date(to_do_list):
    #Allow user to change the due date of an existing task in their To-Do List
    print("\nChange Due Date")
    task = input("\tEnter task: ")

    if task in to_do_list:
        print("\nTask found.")
        new_due_date = input("\tEnter new due date: ")
        to_do_list[task] = new_due_date
        print("\nDue date updated!")
    else:
        print("\nTask was not found.")

def look_up_task(to_do_list):
    #Let the user search for a task and display its due date if found
    print("\nLook Up Task In To-Do List")
    task = input("\tEnter task: ")

    if task in to_do_list:
       print(f"\nTask found: {to_do_list.get(task)}")
    else:
        print("\nTask was not found.")

main()


