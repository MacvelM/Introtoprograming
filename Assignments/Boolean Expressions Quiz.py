
print("Boolean Expression Quiz")
print()

# Comparison Operators

answer1 = int(input("1. Give a whole number greater than 10:\n"))
print(answer1 > 10)
print()

answer2 = int(input("2. Give a whole number less than 5:\n"))
print(answer2 < 5)
print()

answer3 = int(input("3. Give a whole number equal to 7:\n"))
print(answer3 == 7)
print()

answer4 = int(input("4. Give a whole number that is NOT equal to 3:\n"))
print(answer4 != 3)
print()

answer5 = int(input("5. Give a whole number greater than or equal to 20:\n"))
print(answer5 >= 20)
print()

# Logical Operators

answer6 = int(input("6. Give a whole number greater than 5 AND less than 15:\n"))
print(answer6 > 5 and answer6 < 15)
print()

answer7 = int(input("7. Give a whole number less than 0 OR greater than 100:\n"))
print(answer7 < 0 or answer7 > 100)
print()

answer8 = int(input("8. Give a whole number that is NOT greater than 50:\n"))
print(not(answer8 > 50))
print()

print("Quiz Complete!")