import random

while True:
    try:
        secret = int(input("Pick a number:"))
    except ValueError:
        print("Pick a valid number")
    else:
        break

min = 1
max = 100

while True:
    guess = (min + max) // 2
    print(f"Guessed Number: {guess}")

    user_input = input("Lower/Higher/Correct: ").lower()

    match user_input:
        case "lower":
            max = guess - 1
        case "higher":
            min = guess + 1
        case "correct":
            print("Thank You For Playing")
            break
        case _:
            print("Please Enter A Valid Input")
