import random

while True:
    def roll():
        x=random.randint(0,6)
        return x
    
    score=0

    players=input("Enter the number of players:(2-4) ")

    if players.isdigit():
        players=int(players)
        if players>=2 and players<=4:
            break
        else:
            print("Enter a number between 2 and 4.")
    else:
        print("Enter a number!")

while True:
    
    roll_or_not=input("Do you want to roll the dice?(y) ")

    if roll_or_not=='y':
        value=roll()
        
        if value==1:
            print("Your rolled a 1. Turn Over!")
            score=0
            print("Your score is 0.")
        else:
            print("You rolled a "+str(value))
            score+=value
            print("your score is",score)
        
    else:
        break



        

