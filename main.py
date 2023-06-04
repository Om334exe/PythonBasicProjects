#Rock Paper And Scissors Project
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
game_images=[rock,paper,scissors]
user_choice = int(input("What do you choose ,0 for Rock ,1 for paper pr 2 fpr scissors"))
print(game_images[user_choice])

computer_choice = random.randint(0,2)
print(game_images[computer_choice])
if user_choice>=3 or user_choice < 0 :
    print("You typed an invalid number , you loose")
elif user_choice ==0 and computer_choice ==2 :
    print("You win ")
elif computer_choice ==0 and user_choice ==2 :
    print("You loose ")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")

