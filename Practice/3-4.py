def get_number():
    n=input("Enter a Whole Number")
    try:
        n=int(n)
    except:
        print("you entered a wrong number, please enter a number...")
        get_number()
    return n

def divide(x):
    try:
        return 100/x

    except:
        print("cannot devided by zero, try afain...")
        get_number()

num= get_number()
print(divide(num))   
