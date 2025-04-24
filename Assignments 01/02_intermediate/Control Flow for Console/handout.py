import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    round = 0
    score = 0

    while True:
        computer = random.randint(1, 100)
        user = random.randint(1, 100)
        round += 1
        print("\nRound", round)
        print("your number is", user)
        user_input = input("Do you think your number is higher or lower than the computer's? ")

        if user > computer:
            if user_input.lower() == "higher":
                print("You were correct! the computer's number was", computer)
                score += 1
                print("Your score is now", score)
            elif user_input.lower() == "lower":
                print("You were wrong! the computer's number was", computer)
                print("Your score is now", score)
            else:
                print("Invalid input. Please enter 'higher' or 'lower'.")
                round -= 1
        elif user < computer:
            if user_input.lower() == "lower":
                print("You were correct! the computer's number was", computer)
                score += 1
                print("Your score is now", score)
            elif user_input.lower() == "higher":
                print("You were wrong! the computer's number was", computer)
                print("Your score is now", score)
            else:
                print("Invalid input. Please enter 'higher' or 'lower'.")
                round -= 1
        else:
            pass
        
        if round == NUM_ROUNDS:
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()