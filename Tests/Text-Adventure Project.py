def start_quest():
    print("You are an adventurer and you find yourself walking down a dirt path in a foggy forest, a noise rings out into the distance, you look and a carriage is being attacked by dark elves. Do you:")
    print("1. Go help fight off the dark elves")
    print("2. Try to make a distraction so the carage can get away")
    print("3. Keep walking and do nothing")
    print("4. Wait for them to fight it out and dive in to take the loot")

    choice = input("> ")

    if choice == "1":
        go_help()
    elif choice == "2":
        distraction()
    elif choice == "3":
        keep_walking()
    elif choice == "4":
        wait()
    else:
        print("Invalid choice. Try again.")
        start_quest()


# HELP PATH

def go_help():
    print("You jump in to fight the dark elves.")
    print("A large dark elf with a black greatsword approaches. Do you:")
    print("1. Throw a fire bomb")
    print("2. Fight with your longsword")
    print("3. Turn and run")

    choice = input(">")

    if choice == "1":
        fire()
    elif choice == "2":
        fight()
    elif choice == "3":
        run()
    else:
        print("Invalid choice. Try again")
        go_help()


def fire():
    print("The fire bomb explodes in dry shrubs... everything catches fire.")
    print("You died in the chaos.")
    print("ENDING 1")


def fight():
    print("You try to fight bravely, but the dark elf cuts you down instantly.")
    print("ENDING 2")


def run():
    print("You run away, but you don’t make it far before you are caught.")
    print("ENDING 3")


# DISTRACTION PATH

def distraction():
    print("You try to distract the dark elves so the carriage escapes.")
    print("Do you:")
    print("1. Throw a firework")
    print("2. Use your Viking horn")

    choice = input(">")

    if choice == "1":
        firework()
    elif choice == "2":
        horn()
    else:
        print("Invalid choice. Try again")
        distraction()


def firework():
    print("The firework explodes too early and kills you.")
    print("ENDING 4")


def horn():
    print("The horn alerts everyone... including archers.")
    print("You are taken down instantly.")
    print("ENDING 5")


# KEEP WALKING PATH


def keep_walking():
    print("You ignore the battle and keep walking.")
    print("A 20ft snow bear appears. Do you:")
    print("1. Run into a cave")
    print("2. Run to the river")
    print("3. Climb a tree")

    choice = input(">")

    if choice == "1":
        cave()
    elif choice == "2":
        river()
    elif choice == "3":
        tree()
    else:
        print("Invalid choice. Try again")
        keep_walking()


def cave():
    print("You enter the cave and reach a split path. Do you:")
    print("1. Go left")
    print("2. Go right")

    choice = input(">")

    if choice == "1":
        left()
    elif choice == "2":
        right()
    else:
        print("Invalid choice. Try again")
        cave()


def left():
    print("You hit a dead end... the bear catches you.")
    print("ENDING 6")


def right():
    print("You find a glowing pool and jump in.")
    print("It leads to a treasure cave.")
    print("You become rich.")
    print("ENDING 7")


def river():
    print("You fall into the river. Do you:")
    print("1. Use spirit charm")
    print("2. Try to swim")

    choice = input(">")

    if choice == "1":
        charm()
    elif choice == "2":
        swim()
    else:
        print("Invalid choice. Try again")
        river()


def charm():
    print("A spirit saves you and gives you a magical sword.")
    print("ENDING 8")


def swim():
    print("The current is too strong...")
    print("You are dragged into a waterfall.")
    print("ENDING 9")


def tree():
    print("You climb the tree. Do you:")
    print("1. Jump to another tree")
    print("2. Stay still")

    choice = input(">")

    if choice == "1":
        jump_tree()
    elif choice == "2":
        safe_tree()
    else:
        print("Invalid choice. Try again")
        tree()


def jump_tree():
    print("You fall and get caught by the bear.")
    print("ENDING 10")


def safe_tree():
    print("The bear leaves and you escape safely.")
    print("ENDING 11")


# -------------------------
# WAIT PATH
# -------------------------

def wait():
    print("You wait for the battle to end.")
    print("Do you:")
    print("1. Take the treasure chest")
    print("2. Leave it")

    choice = input(">")

    if choice == "1":
        chest()
    elif choice == "2":
        leave()
    else:
        print("Invalid choice. Try again")
        wait()


def chest():
    print("The chest curses you and turns you into a dark king.")
    print("ENDING 12")


def leave():
    print("You safely take gold from the battlefield.")
    print("ENDING 13")


# -------------------------
# EXTRA PATHS (to meet 20 encounters requirement)
# -------------------------

def hidden_path():
    print("You find a hidden path. Do you:")
    print("1. Enter")
    print("2. Ignore it")

    choice = input(">")

    if choice == "1":
        ruins()
    elif choice == "2":
        wander_end()
    else:
        print("Invalid choice")
        hidden_path()


def ruins():
    print("You find ancient ruins. Do you:")
    print("1. Enter temple")
    print("2. Leave")

    choice = input(">")

    if choice == "1":
        temple()
    elif choice == "2":
        wander_end()
    else:
        print("Invalid choice")
        ruins()


def temple():
    print("Inside is a cursed artifact.")
    print("You either become powerful or die.")
    print("ENDING 14")


def wander_end():
    print("You wander until you are lost forever.")
    print("ENDING 15")


def secret_castle():
    print("You find a secret castle. Do you:")
    print("1. Enter")
    print("2. Run away")

    choice = input(">")

    if choice == "1":
        throne()
    elif choice == "2":
        escape()
    else:
        print("Invalid choice")
        secret_castle()


def throne():
    print("The king gives you a choice to rule or die.")
    print("ENDING 16")


def escape():
    print("You escape but fall into a trap outside.")
    print("ENDING 17")


# -------------------------
# FIX YOUR BROKEN STARTING CONNECTIONS
# -------------------------

def extra_routes():
    hidden_path()
    secret_castle()


start_quest()