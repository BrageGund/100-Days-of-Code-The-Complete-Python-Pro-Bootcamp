rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random


your_input = input("Choose Rock, Paper, or Scissors: ")

game = [rock, paper, scissors]
random = random.choice(game)
print(random)

# Rock
if your_input == "Rock" and random == paper:
    print("You lose")
elif your_input == "Rock" and random == scissors:
    print("You win")
elif your_input == "Rock" and random == rock:
    print("Draw. Try again")

# Paper
elif your_input == "Paper" and random == scissors:
    print("You lose")
elif your_input == "Paper" and random == rock:
    print("You win")
elif your_input == "Paper" and random == paper:
    print("Draw. Try again")

# Scissors
elif your_input == "Scissors" and random == rock:
    print("You lose")
elif your_input == "Scissors" and random == paper:
    print("You win")
elif your_input == "Scissors" and random == scissors:
    print("Draw. Try again")
else:
    print("Invalid")