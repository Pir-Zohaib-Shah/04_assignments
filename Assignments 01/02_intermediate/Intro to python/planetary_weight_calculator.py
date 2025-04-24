MARS_MULTIPLE = 0.38
VENUS_MULTIPLE = 0.91
MOON_MULTIPLE = 0.165
JUPITER_MULTIPLE = 2.34

def main():
    print("Welcome to the Planetary Weight Calculator!")
    weight = float(input("Enter your weight on Earth (in kg): "))
    planet = input("Enter the planet: ").strip().lower()
    
    mars_weight = weight * MARS_MULTIPLE
    venus_weight = weight * VENUS_MULTIPLE
    moon_weight = weight * MOON_MULTIPLE
    jupiter_weight = weight * JUPITER_MULTIPLE

    if planet == "mars":   
        print(f"Your weight on Mars: {mars_weight:.2f} kg")
    elif planet == "venus":
        print(f"Your weight on Venus: {venus_weight:.2f} kg")
    elif planet == "moon":
        print(f"Your weight on the Moon: {moon_weight:.2f} kg")
    elif planet == "jupiter":
        print(f"Your weight on Jupiter: {jupiter_weight:.2f} kg")
    else:
        print("Invalid planet name. Please enter 'Mars', 'Venus', 'Moon', or 'Jupiter'.")

if __name__ == "__main__":
    main()