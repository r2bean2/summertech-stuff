import questionary
import os
matrix = [
    ["1", "2", "3", "4"],
    ["5", "6", "7", "8"],
    ["9", "10", "11", "12"]
]
file_path = "feedback.txt"


def get_rows():
    print(matrix)
    print 
    global selected_row 
    selected_row = questionary.select(
        "select the row to modify:",
            num_op_rows
    ).ask()
    selected_row = int(selected_row)
    selected_row -=1
while True:
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0
    num_op_rows = [str(i) for i in range(1, num_rows + 1)]
    num_op_cols = [str(i) for i in range(1, num_cols+ 1)]

    action = questionary.select(
        "Select list operation to perform:",
            choices = [
                {
                    "name": "add to the matrix",
                    "value": "add",
                },
                {
                    "name": "view matrix",
                    "value": "view",
                },
                {
                    "name": "remove an part of the matrix",
                    "value": "remove",
                },
                {
                    "name": "click this if you are depressed and want to leave",
                    "value": "lkdj;lj;lajldjad;ljdlja;ljdlkdaj;ljlkdj;ldjaja;ljd;ld",
                }
            ]
    ).ask()
    if action == "add":
        get_rows()
        thing_to_add = input("what do you want to add to the matrix: ")
        matrix[selected_row].append(thing_to_add)
    elif action == "view":
        print(matrix)
    elif action == "remove":
        get_rows()
        thing_to_remove = questionary.select(
            "which object to remove:",
                matrix[selected_row]
        ).ask()
        matrix[selected_row].remove(thing_to_remove)
    else:
        print("would you like to leave a review today")
        yn =  questionary.select(
            "do you wish to leave feedback",
            choices=[
                "yes",
                "no",
            ],
            ).ask()
        if yn == "no":
            print("you dont want to leave feedback so you must not be ready to leave")
        else:
            stuff = input("please explain your experince, and weather you'd use this script agian: ")
            print("other respouses include:")

            # Determine where this script is
            full_path = __file__
            if not os.path.abspath(full_path):
                full_path = os.path.join(os.getcwd(), full_path)

            # The directory it's located in should be install/local/
             # So we should change to that
            install_local_dir = os.path.dirname(full_path)
            os.chdir(install_local_dir)
            if not os.path.exists(file_path):
                with open(file_path, "w") as file:
                    pass  # 'pass' creates an empty file
            with open("feedback.txt", "r") as file:
                print(file.read())
            with open("feedback.txt", "a") as file:
                file.write("\n" + stuff)
            break

