# # Create a Password Generator:
# import string
# import random  

# print("Welcome to My Password Generator :)")

# user_letter = int(input("How many letters would you like in your password?\n"))

# user_symbol = int(input("How many symbols would you like?\n"))

# user_number = int(input("How many numbers would you like?\n"))


# letters = string.ascii_letters
# numbers = string.digits  
# symbols = string.punctuation

# password_list = []

# for i in range(user_letter):
#     password_list.append(random.choice(letters))

# for  i in range(user_symbol):
#     password_list.append(random.choice(symbols))

# for i in range(user_number):
#     password_list.append(random.choice(numbers))

# random.shuffle(password_list)

# password = ''.join(password_list)

# print(f"Your generated password is: {password}")




# Importing necessary modules: 'string' for characters and 'random' for randomness
import string
import random  

# Welcome message for the user
print("Welcome to My Password Generator :)")

# Taking user input for the number of letters, symbols, and numbers in the password
user_letter = int(input("How many letters would you like in your password?\n"))
user_symbol = int(input("How many symbols would you like?\n"))
user_number = int(input("How many numbers would you like?\n"))

# Defining possible characters to include in the password
letters = string.ascii_letters  # All uppercase and lowercase letters
numbers = string.digits          # Digits from 0 to 9
symbols = string.punctuation     # Special characters like @, #, $

# Initializing an empty list to store the randomly chosen characters
password_list = []

# Adding random letters to the password_list
for i in range(user_letter):
    password_list.append(random.choice(letters))

# Adding random symbols to the password_list
for i in range(user_symbol):
    password_list.append(random.choice(symbols))

# Adding random numbers to the password_list
for i in range(user_number):
    password_list.append(random.choice(numbers))

# Shuffling the password list to randomize the character order
random.shuffle(password_list)

# Joining the list elements into a single string for the final password
password = ''.join(password_list)

# Displaying the generated password
print(f"Your generated password is: {password}")
