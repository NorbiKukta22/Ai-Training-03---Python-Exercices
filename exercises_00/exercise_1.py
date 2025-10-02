import random

def pick_random_number (a,b):
    return random.randint(a,b)


a = 1
b = 100
secret = random.randint(a,b)
print(secret)

while True:
    guess = random.randint(a,b)
    print(guess)

    if guess < secret:
        a = guess + 1
    
    elif guess > secret:
        b = guess - 1

    else:
        print("The Machine Won")
        break

