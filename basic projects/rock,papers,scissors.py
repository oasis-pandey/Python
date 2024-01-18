import random

computer_score=0
user_score=0

print('WELCOME TO ROCK PAPER SCISSORS'+'\n')

elements=['rock','paper','scissors']

while True:
    user_pick=input("Please pick rock, papers or scissors or Q to quit: ")
    computer_pick= elements[random.randrange(0,3)]# generates random number from 0 to 2
    if user_pick.lower()=='q':
        quit()
    
    elif user_pick not in elements:
        continue

    elif user_pick=='rock' and computer_pick=='scissors':
        print("You won!")
        print("The computer picked scissors")
        user_score+=1
        

    elif user_pick=='paper' and computer_pick=='rock':
        print("You won!")
        print("The computer picked rock")
        user_score+=1
        

    elif user_pick=='scissors' and computer_pick=='paper':
        print("You won!")
        print("The computer picked paper")
        user_score+=1
        

    else:
        print("You lost!")
        print("The computer picked: "+str(computer_pick))
        computer_score+=1
    print(" ")
    print(" The scores are as follows: ")
    print("USER SCORE: "+str(user_score))
    print("COMPUTER SCORE: "+ str(computer_score))
    print(" ") 
        

    
    

 

    
