import random

def showChoice(show):
    if show==0:
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')
    elif show==1:
        print('''
        
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)''')
    else:
        print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')


print("Rock, paper, Scissors Game")
choice=int(input("What dou youse choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
print("Your Choice:")
showChoice(choice)


computerChoice=random.randint(0,2)
print("Computer Choice")
showChoice(computerChoice)

if choice==0 and computerChoice==1 or choice==1 and computerChoice==2 or choice==2 and computerChoice==0:
    print("You loose!")
elif choice== computerChoice:
    print("It is a draw!")
else:
    "You win!"