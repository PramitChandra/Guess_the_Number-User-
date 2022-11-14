import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0  # Because we don't want our guess to ever
    # accidentally equal that random number.

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 to {x}: "))
        if guess < random_number:
            print("Sorry! Guess again. Too Low.\n")
        elif guess > random_number:
            print("Sorry! Guess again. Too High\n")

    print(f"Congrats! You have guessed the number {random_number} correctly.")


guess(50)
