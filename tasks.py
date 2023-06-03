import time

titles_list = []  # List to store task titles
tasks_list = []   # List to store task details

def loading():
    print('\n--------LOADING--------\n')
    time.sleep(1)

def new_task():
    print("Welcome to the create page!")
    new_title = input("Title: ")
    new_tasks = input("Write here!: ")
    titles_list.append(new_title)
    tasks_list.append(new_tasks)
    print("Saved: ", new_title, "\n", new_tasks)
    input("Press Enter to exit")

def open_task():
    if not titles_list:
        print("------No tasks------")
    else:
        for i, title in enumerate(titles_list, start=1):
            print("Task {}: {}".format(i, title))
        title_choice = int(input("Open task (enter number): ")) - 1
        if 0 <= title_choice < len(titles_list):
            print("-------: {} :--------\n--: {}".format(titles_list[title_choice], tasks_list[title_choice]))
        else:
            print("Invalid task number")
    input("Press Enter to exit")

def account(pas):
    while True:
        account_choice = input('''
        (1) Change name
        (2) Change password
        (3) Delete account
        (4) Exit
        Enter your choice: ''')
        if account_choice == '1':
            loading()
            name = input("Enter your name: ")
            loading()
        elif account_choice == '2':
            loading()
            pas = password(pas)
            loading()
        elif account_choice == '3':
            name = 0
            pas = 0
            tasks_list.clear()
            titles_list.clear()
            print('\n----Account deleted----\n')
        elif account_choice == '4':
            break

def password(pas):
    count = 0
    while count < 3:
        count += 1
        pas0 = input("Enter your password: ")
        if pas0 == pas:
            pas = input("Enter the new password: ")
            break
        else:
            print("Try again, you have {} attempts".format(3 - count))
    return pas

name = input("Enter your name: ")
pas = input("Enter your password: ")
print('\n----Welcome, {}----'.format(name))

while True:
    main_choice = input('''
    (1) New task
    (2) Open tasks
    (3) Account
    (4) Settings
    (5) Leave app
    Enter your choice: ''')

    if main_choice == '1':
        loading()
        new_task()
        loading()
    elif main_choice == '2':
        loading()
        print('\n----Here are all your tasks----\n')
        open_task()
        loading()
    elif main_choice == '3':
        loading()
        account(pas)
        loading()
    elif main_choice == '5':
        print('\nGoodbye! Have a nice day(:')
        loading()
        break
        
 #explain:      
#The titles_list and tasks_list are declared as empty lists to store task information.
#The loading() function displays a loading message and adds a delay to simulate loading time.
#The new_task() function prompts the user to enter a task title and details, which are then added to the titles_list and tasks_list respectively.
#The function also prints the saved task and waits for the user to press Enter.
#The open_task() function displays a numbered list of available tasks. The user selects a task by entering the corresponding number. If a valid task number is entered, the function displays the title and details of the selected task. If an invalid task number is entered or there are no tasks, appropriate messages are displayed. The function waits for the user to press Enter.
#The account() function handles account-related actions. It provides options for changing the name, changing the password, deleting the account, and exiting. The function uses a while loop to repeatedly display the menu until the user chooses to exit.
#The password() function handles password validation and change. It takes the current password as input and prompts the user to enter the password. If the entered password matches the current password, the user is prompted to enter a new password. The function ensures that the user has a maximum of three attempts to enter the correct password. The new password is returned by the function.
#The user is prompted to enter their name and password at the beginning of the program. The name is stored in the name variable, and the password is stored in the pas variable.
#The main program starts with an infinite loop, allowing the user to choose from various options.
#Inside the loop, the user's choice is obtained using the input() function.
#Depending on the user's choice, the corresponding function is called.
#The program continues to run until the user chooses to exit (selects option 5).

