import questionary
import os
thing_list = [
    "hi"
]
file_path = "feedback.txt"
while True:
    action = questionary.select(
        "Select list operation to perform:",
            choices = [
                {
                    "name": "add to the list",
                    "value": "add",
                },
                {
                    "name": "view list",
                    "value": "view",
                },
                {
                    "name": "remove an option",
                    "value": "remove",
                },
                {
                    "name": "click this if you are depressed and want to leave",
                    "value": "lkdj;lj;lajldjad;ljdlja;ljdlkdaj;ljlkdj;ldjaja;ljd;ld",
                }
            ]
    ).ask()
    if action == "add":
        thing_to_add = input("what do you want to add to the list: ")
        thing_list.append(thing_to_add)
    elif action == "view":
        print(thing_list)
    elif action == "remove":
        thing_to_remove = questionary.select(
            "which object to remove:",
                thing_list
        ).ask()
        thing_list.remove(thing_to_remove)
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

