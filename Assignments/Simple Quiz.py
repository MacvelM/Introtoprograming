# Simple Quiz Project

score = 0

def ask_question(question, correct_answer):
    global score

    print(question)
    answer = input("> ")

    if answer.lower() == correct_answer.lower():
        print("Correct!\n")
        score += 1
    else:
        print("Wrong!\n")


def tally_score():
    print("Quiz Complete!")
    print("Your final score is:", score, "/ 10")

    if score == 10:
        print("Perfect score! You're a genius.")
    elif score >= 7:
        print("Great job!")
    elif score >= 5:
        print("Not bad, keep practicing.")
    else:
        print("You might need to study a bit more.")


def start_quiz():
    print("Welcome to the Simple Quiz!\n")

    ask_question("1. What is 5 + 3?", "8")
    ask_question("2. What is the capital of France?", "Paris")
    ask_question("3. What planet is known as the Red Planet?", "Mars")
    ask_question("4. What is 10 x 2?", "20")
    ask_question("5. What gas do plants breathe in?", "Carbon dioxide")
    ask_question("6. What is the largest ocean on Earth?", "Pacific")
    ask_question("7. What is H2O commonly known as?", "Water")
    ask_question("8. How many continents are there?", "7")
    ask_question("9. What is the square root of 16?", "4")
    ask_question("10. What language is this code written in?", "Python")

    tally_score()


start_quiz()