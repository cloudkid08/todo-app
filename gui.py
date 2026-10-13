# Add an Edit button + a list box that shows existing todos.
#
# NEW WIDGET: sg.Listbox
#   values        -> the initial list of strings to show
#   key           -> identifier so we can read what the user selected
#                    (values["todos"] is a LIST of selected items;
#                    use [0] to grab the first/only one).
#   enable_events -> True so clicking a row fires an event (we just
#                    rely on it for `values["todos"]` here).
#   size          -> (width_in_chars, height_in_rows)
#
# The edit case:
#   1. Read the currently-selected todo from values["todos"][0].
#   2. Read the new text from the input box (values["todo"]).
#   3. Get the full list from the file, find the old todo's index,
#      replace it with the new text (+"\n"), and write the list back.
#   4. Call window["todos"].update(values=todos) to refresh the
#      listbox in REAL TIME — otherwise the GUI keeps showing the
#      stale list until the user restarts the app.
#
# We do the same `window["todos"].update(...)` at the end of the Add
# case so newly-added todos appear in the listbox immediately.

import FreeSimpleGUI as sg
import functions


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")

window = sg.Window("My To-Do App",
                   layout=[
                       [label],
                       [input_box, add_button],
                       [list_box, edit_button],
                   ],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)

            window["todos"].update(values=todos)
        case 'todos':
            window['todo'].update(value = values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
