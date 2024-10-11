# Create a Password Generator:
import string
import random  

print("Welcome to My Password Generator :)")

user_letter = int(input("How many letters would you like in your password?\n"))

user_symbol = int(input("How many symbols would you like?\n"))

user_number = int(input("How many numbers would you like?\n"))


letters = string.ascii_letters
numbers = string.digits  
symbols = string.punctuation

password_list = []

for i in range(user_letter):
    password_list.append(random.choice(letters))

for  i in range(user_symbol):
    password_list.append(random.choice(symbols))

for i in range(user_number):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ''.join(password_list)

print(f"Your generated password is: {password}")
