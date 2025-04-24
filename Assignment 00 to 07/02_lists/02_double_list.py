def main():

    numbers:list[int] = [1, 2, 3, 4, 5]

    for i in range(len(numbers)):
        el_at_index = numbers[i]
        numbers[i] = el_at_index * 2

        print(numbers)

if __name__ == "__main__":
    main()