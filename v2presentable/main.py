import os
from AASCII import logo
from map import Map

run = True
menu = True
play = False
rules = False
key = False
new_map = True

HP = 50
HPMAX = HP
ATK = 3
core= 0
coin = 0
x = 0
y = 0

map =  [["plains","plains","plains","plains","plains","plains","plains","plains","plains","plains","plains","plains"],
        ["plains","plains","plains","plains","plains","plains","plains","plains","plains","plains","plains","plains"],
        ["plains","plains","plains","plains","plains","plains","plains","plains","plains","plains","plains","plains"],
        ["plains","plains","plains","plains","plains","plains","plains","plains","plains","plains","plains","plains"],
        ["plains","plains","plains","plains","plains","plains","plains","plains","plains","plains","plains","plains"],
        ["plains","plains","plains","plains","plains","plains","plains","plains","plains","plains","plains","plains"],
        ["plains","plains","plains","plains","plains","plains","plains","plains","plains","plains","plains","plains"],
        ["plains","plains","plains","plains","plains","plains","plains","plains","plains","plains","plains","plains"],
        ["plains","plains","plains","plains","plains","plains","plains","plains","plains","plains","plains","plains"],
        ["plains","plains","plains","plains","plains","plains","plains","plains","plains","plains","plains","plains"]]

y_len = len(map)-1
x_len = len(map[0])-1

tile = {
    "plains": {
        "t": "PLAINS",
        "e": True},
    "forest": {
        "t": "WOODS",
        "e": True},
    "fields": {
        "t": "FIELDS",
        "e": False},
    "bridge": {
        "t": "BRIGE",
        "e": True},
    "shop": {
        "t": "SHOP",
        "e": False},
    "mountain": {
        "t": "MOUNTAIN",
        "e": True},
    "hills": {
        "t": "HILLS",
        "e": True,
    }
}

def clear():
    os.system("cls")

def draw():
    print("Xx-------------------xX")

def save():
    list = [
        name,
        str(HP),
        str(ATK),
        str(core),
        str(coin),
        str(x),
        str(y),
        str(key),
        str(new_map)
    ]

    f = open("load.txt", "w")

    for item in list:
        f.write(item + "\n")
    f.close()

while run:
    while menu:
        clear()
        print(logo())
        input("> ")
        clear()
        draw()
        print("1, NEW GAME")
        print("2, LOAD GAME")
        print("3, RULES")
        print("4, QUIT GAME")
        draw()

        if rules:
            print("There are no rules yet")
            rules = False
            choice = ""
            input("> ")
        else:
            choice = input("# ")

        if choice == "1":
            clear()
            name = input("Name: ")
            menu = False
            play = True
            choice = ""
            input("> ")
        elif choice == "2":
            try:
                f = open("load.txt", "r")
                load_list = f.readlines()
                if len(load_list) == 9:
                    name = load_list[0][:-1]
                    HP = int(load_list[1][:-1])
                    ATK = int(load_list[2][:-1])
                    core = int(load_list[3][:-1])
                    coin = int(load_list[4][:-1])
                    x = int(load_list[5][:-1])
                    y = int(load_list[6][:-1])
                    key = bool(load_list[7][:-1])
                    new_map = bool(load_list[8][:-1])
                    clear()
                    print("Welcome back " + name +"!")
                    input("> ")
                    menu = False
                    play = True
                else:
                    print("Corrupted save file!")
                    input("> ")
            except OSError:
                print("Missing save file!")
                input("> ")
        elif choice == "3":
            rules = True
        elif choice == "4":
            quit()

    while play:
        while new_map == True:
            if __name__ == "__main__":
                map_w, map_h = 30, 20
                game_map = Map(map_w, map_h)
                new_map = False
        save()  # autosave
        clear()
        game_map.display_map()
        draw()
        print("LOCATION: " + tile[map[y][x]]["t"])
        draw()
        print("NAME: " + name)
        print("HP: " + str(HP) + "/" + str(HPMAX))
        print("ATK: " + str(ATK))
        print("CORES: " + str(core))
        print("COINS: " + str(coin))
        print("COORDINATES: " + str(x) + "," + str(y))
        draw()
        print("0 - SAVE AND QUIT")
        if y > 0:
            print("1 - NORTH")
        if x < x_len:
            print("2 - EAST")
        if y < y_len:
            print("3 - SOUTH")
        if x > 0:
            print("4 - WEST")
        draw()

        dest = input("# ")

        if dest == "0":
            play = False
            menu = True
            save()
        elif dest == "1":
            if y > 0:
                y -=1
        elif dest == "2":
            if x < x_len:
                x += 1
        elif dest == "3":
            if y < y_len:
                y +=1
        elif dest == "4":
            if x > 0:
                x -= 1
