def print_multiple(message: str, repeat: int):

    for i in range(repeat):
        print(message)

def main():

    message = input("Enter a message: ")
    repeat = int(input("How many times do you want to print it? "))
    print_multiple(message, repeat)

if __name__ == '__main__':  
    main()