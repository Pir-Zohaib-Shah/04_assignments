import random

num_sides = 6

def main():

    die1 = random.randint(1, num_sides)
    die2 = random.randint(1, num_sides)
    total = die1 + die2

    print(f"dice have {num_sides} sides each!")
    print(f"first die: {die1}")
    print(f"second die: {die2}")
    print(f"total of two dice: {total}")

if __name__ == '__main__':
    main()