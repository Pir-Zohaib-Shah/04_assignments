def add_many_numbers(numbers)-> int:
    
    total = 0

    for number in numbers:
        total += number

    return total

def main():

    numbers:list = [1, 2, 3, 4, 5]
    sum_of_numbers = add_many_numbers(numbers)
    print(f"The sum of {numbers} is {sum_of_numbers}")

if __name__ == "__main__":
    main()