import random

def fortune_teller():
    print("Welcome traveler...")
    print("I am the Mystic Fortune Teller.")
    print("Answer my questions and I shall reveal your future.\n")

    try:
        lucky_number = int(input("Enter your lucky number: "))
        future_years = float(input("How many years into the future do you wish to see?: "))
        magic_multiplier = float(input("Enter a magical multiplier: "))
        spirit_number = int(input("Enter your spirit number: "))
        moon_power = float(input("Enter the moon's power level: "))

    except ValueError:
        print("\nThe spirits are confused...")
        print("You must enter the correct number type!")
        print("Try again.\n")
        fortune_teller()
        return

    random_number = random.randint(1, 10)

    fortune_value = (lucky_number + future_years + spirit_number) * magic_multiplier + moon_power + random_number

    print("\nThe crystal ball glows...\n")

    if fortune_value < 50:
        print("A great adventure waits for you.")
    
    elif fortune_value < 100:
        print("You will discover hidden treasure.")
    
    elif fortune_value < 150:
        print("A powerful ally will soon appear.")
    
    elif fortune_value < 200:
        print("You must prepare for a dangerous challenge.")
    
    elif fortune_value < 250:
        print("A mysterious stranger will change your fate.")
    
    elif fortune_value < 300:
        print("You will gain great knowledge.")
    
    elif fortune_value < 350:
        print("Fortune and wealth are in your future.")
    
    elif fortune_value < 400:
        print("A dark secret will soon be revealed.")
    
    elif fortune_value < 450:
        print("The stars show a legendary victory.")
    
    else:
        print("You are destined to rule kingdoms.")

    print("\nYour fortune number was:", fortune_value)


fortune_teller()