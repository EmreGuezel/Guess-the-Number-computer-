import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess > random_number:
            print("Your guess is too high!")
        elif guess < random_number:
            print("Your number is too low!")
    print(f"Well done! You have guessed the number correctly that is {random_number}")

guess(10)