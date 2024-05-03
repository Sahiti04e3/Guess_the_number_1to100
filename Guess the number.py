import random


def guess_the_number():
    secret_number = random.randint(1, 100)

    print("Welcome to the Number Guessing Game!")
    print("I've selected a random number between 1 and 100. Try to guess it!")

    attempts = 0

    while True:
        user_guess = int(input("Your guess: "))
        attempts += 1

        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")


guess_the_number()