
# Rock, Paper, Scissors Game using Python
import random  # Importing the random module to generate random choices for the computer

try:
    # Asking the user to make a choice between Rock (0), Paper (1), and Scissors (2)
    user_say = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n"))
    
    # Validating the user's input to ensure they enter a valid number (0, 1, or 2)
    if user_say not in [0, 1, 2]:
        raise ValueError("You typed an invalid number!")  # Raise an error if the input is invalid

    # Randomly generating the computer's choice using randint, which can be 0, 1, or 2
    computer_say = random.randint(0, 2)

    # Defining the choices list that maps numbers to Rock, Paper, and Scissors
    choices = ['Rock', 'Paper', 'Scissors']

    # Displaying the user's choice and the computer's choice
    print(f"You chose: {choices[user_say]}")
    print(f"Computer chose: {choices[computer_say]}")

    # Logic to determine if the match is a draw, the user wins, or the computer wins
    if user_say == computer_say:
        print("This match is a Draw!")  # When both the user and the computer have the same choice
    elif (user_say == 0 and computer_say == 2) or (user_say == 1 and computer_say == 0) or (user_say == 2 and computer_say == 1):
        print("You Win!")  # User wins when Rock beats Scissors, Paper beats Rock, or Scissors beats Paper
    else:
        print("You Lose!")  # Otherwise, the user loses

    # Fun ASCII art display based on the user's choice
    if user_say == 0:
        print(''' 

            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
  
    ''')
    elif user_say == 1:
        print(''' 
            _______
        ---'   ____)____
                  ______)
                  _______)
                 _______)
        ---.__________)

    ''')
    elif user_say == 2:
        print(''' 
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
    ''')

# Handling errors if the user enters an invalid number
except ValueError as ve:
    print(f"Invalid input! {ve}")
# Handling any other exceptions that may occur
except Exception as e:
    print(f"An error occurred: {e}")
