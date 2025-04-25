import random

print("Welcome to the Password Generator!")
print("====================================")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+[]{}|;:,.<>?"
length = int(input("Enter the desired length of the password: "))
num_passwords = int(input("Enter the number of passwords to generate: "))

passwords = []
for _ in range(num_passwords):
    password = ''.join(random.choice(chars) for _ in range(length))
    passwords.append(password)
    

print("\nGenerated Passwords:")
for i, password in enumerate(passwords, 1):
    print(f"Password {i}: {password}")