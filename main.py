run = True
menu = True
play = False
rules = False

HP = 50
ATK = 3

def save():
    list =[
        name,
        str(HP),
        str(ATK),

    ]

    f = open("load.txt", "w")

    for item in list:
        f.write(item + "\n")
    f.close()

while run:
    while menu:
        print("1, NEW GAME")
        print("2, LOAD GAME")
        print("3, RULES")
        print("4, QUIT GAME")

        if rules:
            print("There are no rules yet")
            rules = False
            choice = ""
            input("> ")
        else:
            choice = input("# ")

        if choice == "1":
            name = input("Name: ")
            menu = False
            play = True
            choice = ""
            input("> ")
        elif choice == "2":
            pass
        elif choice == "3":
            rules = True
        elif choice == "4":
            quit()

    while play:
        save()  # autosave

        dest = input("# ")

        if dest == "0":
            play = False
            menu = True
            save()