
import random
import string

print("Welcome to Random Password Generator!")

# Ask the user for password length
length = int(input("Enter password length: "))

# Characters to use in the password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate random password
password = ""

for i in range(length):
    password += random.choice(characters)

# Display password
print("Your random password is:", password)
