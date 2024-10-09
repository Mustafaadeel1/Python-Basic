# Rock', 'Paper', 'Scissors Game 
import random

try:
   
    user_say = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n"))


    if user_say not in [0, 1, 2]:
        raise ValueError("You typed an invalid number!")

    computer_say = random.randint(0, 2)

    choices = ['Rock', 'Paper', 'Scissors']

    print(f"You chose: {choices[user_say]}")
    print(f"Computer chose: {choices[computer_say]}")

   
    if user_say == computer_say:
        print("This match is a Draw!")
    elif (user_say == 0 >=  computer_say == 2) or (user_say == 1 >= computer_say == 0) or (user_say == 2 >= computer_say == 1):
        print("You Win!")
    else:
        print("You Lose!")


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
        
except ValueError as ve:
    print(f"Invalid input! {ve}")
except Exception as e:
    print(f"An error occurred: {e}")
