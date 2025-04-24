def main():

    adj1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    fam_person = input("Enter a famous person: ")
   

    madelib = f"Programming is so {adj1}! It makes me want to {verb1} like a {noun1}. " \
              f"One day, I hope to be as good as {fam_person} at coding. "
    
    print(madelib)

if __name__ == "__main__":
    main()