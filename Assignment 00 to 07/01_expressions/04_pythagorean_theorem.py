import math

def main():
    
    ab: float = float(input("Enter the length of side AB: "))
    ac: float = float(input("Enter the length of side AC: "))

    bc: float = math.sqrt(ab**2 + ac**2)
    print(f"\nThe length of side BC is:" + str(bc))

if __name__ == '__main__':
    main()