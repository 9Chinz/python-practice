import random

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

game_img = [rock, paper, scissors]

user_choice = int(input("1) Rock, 2) Paper, 3) Scissors : "))-1
bot_choice = random.randint(0,2)

if user_choice == bot_choice:
    print(f"draw you : {game_img[user_choice]} bot : {game_img[bot_choice]}")
elif user_choice == 0 and bot_choice == 2 or user_choice > bot_choice:
    print(f"you win you : {game_img[user_choice]} bot : {game_img[bot_choice]}")
else:
    print(f"you lose you : {game_img[user_choice]} bot : {game_img[bot_choice]}")
