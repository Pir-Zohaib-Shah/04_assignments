import random

Num_sides = 6

def roll_dice():

    die1: int = random.randint(1, Num_sides)
    die2: int = random.randint(1, Num_sides)
    total: int = die1 + die2
    print("Total of the two dice is: ", total)

def main():
    die1: int = 10
    print("Die1 in main() starts as: " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("Die1 in main() is " + str(die1))

if __name__ == '__main__':
    main()