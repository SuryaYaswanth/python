import random

user_wins = 0
comp_wins = 0
options= ["rock","paper","scissor"]
while True:
    user_input= input("Type Rock/Paper/Scissors or 0 to Quit:  ").lower()
    if user_input=="0":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    #rock=0, paper = 1,scissor=2
    computer_pick = options[random_number]
    print("Computer picked",computer_pick+".")

    if user_input=="rock" and computer_pick=="scissor":
        print("You won")
        user_wins+=1
        
    elif user_input=="scissor" and computer_pick=="paper":
        print("You won")
        user_wins+=1
        
    elif user_input=="rock" and computer_pick=="paper":
        print("You won")
        user_wins+=1
        
    elif user_input=="rock" and computer_pick=="rock":
        print("Draw")
        
    elif user_input=="paper" and computer_pick=="paper":
        print("Draw")
        
    elif user_input=="scissor" and computer_pick=="scissor":
        print("Draw")
    
    else:
        print("You lost")
        comp_wins+=1

print("You won",user_wins,"times")
print("Computer won",comp_wins,"times")
print("Good bye") 
