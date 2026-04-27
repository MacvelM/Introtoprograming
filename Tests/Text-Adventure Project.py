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

def go_help():
    print("You decided to jump in to fight of the dark elves")
    print(" when you get down there you are confruntted by a Large dark elf with a black greatsword, Do you: ")
    print("1. throw a fire bomb")
    print("2. Try to fight him with your longsword")
    print("3. turn and run")

    choice = input(">")

    if choice == "1":
        fire()
    
    elif choice == "1":
        fight()

    elif choice == "3":
        run() 

    else:
        print("Invalid choice. Try again")
        go_help         

def fire():
    print("You decided to throw a fire bomb but what you didn't realize you guys were fighting a dry shrubs, which ignited and you all died a gruesome death ")
    print("Better Luck next time")

def fight():
    print("You decided to fight, as you go to pull out your sword the dark elf splits you in half with one swing, and you were dead before you even knew it.")
    print("Better Luck next time")
    
def run():
    print("You decided To run, as you turn to run you only get a few feet before you feel a sword go through youre chest")
    print("Better Luck next time")


def distraction():
    print("You decide to make a distraction so the carrage can escape")
    print("As you look down on the battle you get some ideas on how to get their attention, Do you:")
    print("1.Throw a firework in to the middle of the clearing")
    print("2.Use your viking horn you got form a dungen")
    

    choice = input(">")

    if choice== "1":
        firework()
    
    elif choice== "2":
        horn()
    
    else:
        print("Invalid choice. Try again")
        distraction()
    
def firework():
        print("You decided to throw a firework")
        print("You pull out the firework from your bag and as you light it boom! it blows up killing you,")
        print("Better Luck next time")

def horn():
        print("You decided to use your viking Horn as a distraction") 
        print("You blew as hard as you could into the horn, as the noise engulfed the battle. The dark elves' archers turn to you and turned you into a pincushion")
        print("Better Luck next time")




def keep_walking():
    print("You decided to keep walking because its not your problem")
    print("Because of all the noise from the battle a you hve face to face with a 20ft snow bear and he's hungery. Do You:")
    print("")



def wait():
    print





start_quest()