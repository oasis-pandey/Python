import random
score=0
#creating a roll funtion to roll the dice.
while True:
    def roll():
        x=random.randint(0,6)
        return x
    

    players=input("Enter the number of players:(2-4) ")
    player_scores=[0 for i in range(int(players))]    

#ensuring that the number entered is between 2-4 and is a valid number.
    if players.isdigit():
        players=int(players)
        if players>=2 and players<=4:
            break
        else:
            print("Enter a number between 2 and 4.")
    else:
        print("Enter a number!")

#Rolling.
for player_index in range(int(players)):
    while True:
        print("PLAYER", str(player_index+1),"TURN!")
        roll_or_not=input("Do you want to roll the dice?(y) ")

        if roll_or_not=='y':
            value=roll()
            
            
            if value==1:
                print("Your rolled a 1. Turn Over!")
                score=0
                print("Your score is 0.")
                break
            else:
                print("You rolled a "+str(value))
                score+=value
                print("your score is",score)
                player_scores[player_index]=score
        
        else:
            break
x=player_scores.index(max(player_scores))
x=x+1
print("HERE ARE THE SCORES:")
for index, value in enumerate(player_scores):
    print("Player", index+1, ": ", value)

print("\nPLAYER"+str(x)+" won with a total score of: "+str(player_scores[x-1])+'\n')





        

