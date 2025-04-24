def main():
    
    inches_per_foot: int = 12

    feet: float = float(input("Enter feet: "))
    inches: float = feet * inches_per_foot
    print(str(feet) + " feet is " + str(inches) + " inches")
    
if __name__ == '__main__':
    main()