from modules import functions
import time

print("TODO LIST APP\nThis app will help you create your todo list and saves when you stop the program.\nClick one of the following choices below, if your todo list is empty, you\n may want to add first! After adding, your must type in show!\n")
print("\nIMPORTANT!!!\nIf this is ur first time using app, please type help first!!!\n\n")

current_time = time.strftime("%B, %D, %A, %Y %I:%M:%S %p")
print("It is: ", current_time)
while True:
    user_action = input("Enter Add, Show, Edit, Complete or Exit: ")
    user_action = user_action.lower().strip()

    if user_action.startswith("add"):

        todo = user_action[4:]

        todos = functions.get_todos() # FUNCTION

        todos.append(todo + "\n") # ADDING THE TODO

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        if not todos:
            print("YOU FINISHED YOUR TODO LIST")

        else:
            new_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(new_todos):
                row = f"{index + 1}-{item}"
                print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter your new todo: ") + "\n"
            todos[number] = new_todo  # ADDING THE EDITED TODO

            functions.write_todos(todos)

        except ValueError:
            print("\n\nYour command was not valid, you may have typed it wrong, check the help section by typing in (help)\n\n")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip("\n")  # GETTING RID OF TODO FROM LIST
            todos.pop(index)

            write_todos(todos)

            message = f"Todo: {todo_to_remove}, was completed."
            print(message)

        except IndexError:
            print("\n\nNo item with that number, please run the show command to check which number your looking for.\n\n")
    elif user_action.startswith("exit"):
        break
    elif user_action.startswith("help"):

        print("HOW TO USE ADD : type[add *todo*]") # PAY CAREFUL ATTENTION TO THE SPACES
        print("HOW TO USE SHOW : type[show]")
        print("HOW TO USE EDIT : type[edit *number of todo*] (check the number by using show command)")
        print("HOW TO USE COMPLETE : type[complete *number of todo*] (check the number by using show command)")
        print("HOW TO USE EXIT : type[exit]")

print("Bye!")
