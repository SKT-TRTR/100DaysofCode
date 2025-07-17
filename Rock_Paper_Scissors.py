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
game_icons = [rock,paper,scissors]
user= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n" ))
if user >=0 and user <=2:
    print(game_icons[user])
computer = random.randint(0,2)
print("Computer chose: ")
print(game_icons[computer])

if user >=3 and user<0:
    print("You've given an Invalid number. Try Again!")
elif user ==0 and computer ==2:
    print("You win!")
elif computer == 0 and user ==2:
    print("You Lose!")
elif user >computer:
    print("You Win!")
elif computer >user:
    print("You Lose!")
elif user ==computer:
    print("It's a Draw!")