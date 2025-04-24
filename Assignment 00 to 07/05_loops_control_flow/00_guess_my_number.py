import random

def number_guessing_game():
    secret_number = random.randint(1, 100)

    print('Welcome to the "Number Guessing Game!"')
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?")

    while True:
       try :
        guess = int(input("Enter your guess: "))
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("too high! Try again.")
        elif guess == secret_number:
            print("Congratulations! You guessed the number!")
            break
       except ValueError:
        print("Invalid input. Please enter a valid number.")

number_guessing_game()