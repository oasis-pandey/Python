
def quiz_game():
    print("Welcome to my Quiz Game!")

    wanna_play=input("Do you want to play? ")
    if wanna_play.lower()=='yes':
        print("Good luck! You'll get 5 questions and 1 point for every correct answer")
    else:
        quit()

    score=0

    answer1=input("What is the capital city of Nepal? ")
    if answer1.lower()=='kathmandu': 
        print("Correct!")
        score=score+1
    else:
        print("Incorrect! The correct answer is Kathmandu")

    answer2=input("How many planets are there in the solar system? ")
    if answer2.strip()== '8': 
        print("Correct!")
        score=score+1
    else:
        print("Incorrect! The correct answer is 8")

    answer3=input("How many sense organs are there in human body? ")
    if answer3.strip()=='5': 
        print("Correct!")
        score=score+1
    else:
        print("Incorrect! The correct answer is 5")

    answer4=input("What is the full form of CPU? ")
    if answer4.lower()=='central processing unit': 
        print("Correct!")
        score=score+1
    else:
        print("Incorrect! The correct answer is 'central processing unit' ")

    answer5=input("How many bones are there in a adult human body? ")
    if answer5.strip()=='206': 
        print("Correct!")
        score=score+1
    else:
        print("Incorrect! The correct answer is 206")
    print("You gained "+ str(score)+" points")

quiz_game()

play_again=input("Doy you want to play again? ")
if play_again.lower()=='yes':
    quiz_game()
else:
    quit()

