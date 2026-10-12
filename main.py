#from functions import get_todos,write_todos
import functions
import time
now = time.strftime("%b-%m-%Y %H:%M:%S")
print("It is ",now)
while True:
    user_action = input("To add, show, edit, complete, or exit: ")
    user_action = user_action.strip().lower()
    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + "\n")
        functions.write_todos(todos)
    elif user_action.startswith("show"):
        todos = functions.get_todos()
        for index,item in enumerate(todos):
            print(f"{index+1}-{item.strip('\n')}")
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            index = number - 1
            todos = functions.get_todos()
            new_todo = input("Enter the new todo")
            todos[index] = new_todo + '\n'
            functions.write_todos(todos)
        except ValueError:
            print("Please enter a valid command")
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            index = number - 1
            todos = functions.get_todos()
            todo_to_remove = todos[index]
            todos.pop(index)
            print(f"Todo {todo_to_remove.strip('\n')} was removed from the list")
            functions.write_todos(todos)
        except IndexError:
            print("There is no item with that number")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Please enter a valid commmand")

print("bye!!!!")
