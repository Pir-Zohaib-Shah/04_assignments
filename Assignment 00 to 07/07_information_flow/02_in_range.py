def in_range(n, low, high):

  if n >= low and n <= high:
      return True


  return False

def main():
    n : str = int(input("Enter a number: "))
    low : str = int(input("Enter the lower bound: "))
    high : str = int(input("Enter the upper bound: "))
    
    print(in_range(n, low, high))

if __name__ == "__main__":
    main()