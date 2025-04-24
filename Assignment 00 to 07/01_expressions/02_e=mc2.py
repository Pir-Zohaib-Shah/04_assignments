C: int = 299792458  # Speed of light in m/s

def main():
    mass_in_kg: float = float(input("Enter mass in kg: "))
    energy_in_joules: float = mass_in_kg * C**2

    print("e = m * c^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("c = " + str(C) + " m/s")

    print(str(energy_in_joules) + " Joules of energy")

if __name__ == '__main__':
    main()