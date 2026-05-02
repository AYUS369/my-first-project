import random
import string

# 1. Setup the character bucket
all_characters = string.ascii_letters + string.digits + string.punctuation

print("🔐 Welcome to the Password Generator!")

# 2. Get user input for length
length = int(input("How many characters should the password have? "))

# 3. Generate the password using a loop
password = ""
for i in range(length):
    password += random.choice(all_characters)

# 4. Show the result
print(f"✨ Your secure password is: {password}")
