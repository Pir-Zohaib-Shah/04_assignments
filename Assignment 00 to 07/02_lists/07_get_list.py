def main():

    lst = []

    val = input("Enter a Value: ")
    while val:
        lst.append(val)
        val = input("Enter a Value: ")
        print("Press Enter to stop adding values.")

    print("Here is the List:", lst)

if __name__ == "__main__":
    main()