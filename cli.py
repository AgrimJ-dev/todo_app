import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("Hi there!")
print(f"It is, {now}")

while True:
    user_choice = input("Type add, show, edit, complete or exit: ").strip()

    if user_choice.startswith("add"):
        todo = user_choice[4:] + "\n"

        todo_list = functions.get_todos()

        if not todo_list[-1].endswith("\n"):
             todo_list[-1] = todo_list[-1] + "\n"

        todo_list.append(todo)

        functions.write_todos(todo_list)

    elif user_choice.startswith("show"):

        todo_list = functions.get_todos()

        for index, item in enumerate(todo_list,start=1):
            print(index,item,end="")

    elif user_choice.startswith("edit"):

        todo_list = functions.get_todos()

        number = user_choice[-1]
        task_idx = int(number) - 1

        new_todo = input("enter a new task: ") + "\n"
        todo_list[task_idx] = new_todo

        functions.write_todos(todo_list)

    elif user_choice.startswith("complete"):
        try:
            number = int(user_choice[9:])

            todo_list = functions.get_todos()
            index = number - 1 
            removed_task = todo_list[index].strip("\n")
            todo_list.pop(index)

            message = f"{removed_task} was completed and now removed from the list!"

            print(message)

            functions.write_todos(todo_list)
        except IndexError:
             print("There is no item with that number.")
             continue

    elif user_choice == "exit":
        break
    
    else:
        print("enter a valid action please")

print("Bye!")