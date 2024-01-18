import random
number= input("Enter a number, The random number will be till that number only! ")
guesses=0

if number.isdigit():
    number=int(number)
else:
    print("Please enter a number.")
    

random_number=random.randint(0, number)
 
    
while True:
    user_guess=(input("Make a guess! "))
    guesses+=1
    
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Enter a number next time.")
        break
    
    if user_guess==random_number:
        print("You got it!")
        break     
    else:
        print("You got it wrong!")
        
    if user_guess>random_number:
        print("You were above the number")
    else:
        print("Your were below the number")   

print("You got it in", guesses,"guesses.") 



