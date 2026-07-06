import questionary
thing_list = [
    "hi"
]
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
            print("you dont want to leave feedback so you must not be sirouse about leaving")

