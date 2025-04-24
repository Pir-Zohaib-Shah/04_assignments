def main():
    
    number: float = float(input("\033[1;3m Enter a number to see its square: \033[0m"))

    print(" The square of " + str(number) + " is " + str(number ** 2))

if __name__ == '__main__':
    main()