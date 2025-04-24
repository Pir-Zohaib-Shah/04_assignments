def main():
    print("This program will convert Fahrenheit to Celsius\n")

    fahrenheit: str = input("\033[1;3m Enter the temperature in Fahrenheit: \033[0m")
        
    fahrenheit: float = float(fahrenheit)

    celsius: float = (fahrenheit - 32) * 5 / 9

    print(f"\n \033[1;3m Temperature: {fahrenheit}F = {celsius}C \033[0m")

if __name__ == '__main__':
    main()