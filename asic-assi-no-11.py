# # Indexing in Dictionary:
# name_dict: dict = {"name": "Mustafa","age":18 ,"city":{1:"Sialkot",2:"Lahore",3:{1:"Pakistan"}}}
# #print(name_dict)
# #print(name_dict["name"])
# #print(name_dict["city"][1])
# print(name_dict["city"][3][1])
 
# Create a Dict with user input:
# user_input   = ("name","age","country","city")
# for user in user_input:
#     print(f"Enter your : {user_input} ")
#     in_user =(input(user))
#     print(in_user)
    
# name =(input("Enter your name :"))
# age = (input("Enter your age :"))
# country =(input("Enter your Country name :"))
# city = (input("Enter you city name :"))

# user_input["name"]=name
# user_input["age"]=age
# user_input["Country"]=country
# user_input["City"]=city

# print(user_input)

# # Add value in dict using for loop: 
# user_input = ("name", "age", "country", "city")
# user_data = {}  # Create an empty dictionary

# for user in user_input:
#     in_user = input(f"Enter your {user}: ")  # Take input from the user
#     user_data[user] = in_user  # Add the input to the dictionary

# print(user_data)  # Print the final dictionary with all inputs

user_input = ("name", "age", "country", "city")
user_in : dict ={}
for user in user_input:
    input1 = (input(f"Enter your {user}"))
    user_in[user] = input1    
print(user_in)
