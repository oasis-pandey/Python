name=input("Enter you name: ")
print("Welcome to the adventure game!", name)
escape=input("You woke up and found yourself locked in a room. You see a gun. Would you shoot the doorlock or break the glass to escape? (shoot/break): ")

if escape=='shoot':
    print("You shot the doorlock and the door opened.")
    escape=input("You see a bike and a car. What would you choose?(bike/car): ")

    if escape=='bike':
        print("The assasinator heard the bike starting and killed you. YOU LOSE !")

    elif escape=='car':
        print("The assasinator heard you but the car had bulletproof windows.")
        escape=input("You're safe. Would you drive left or right?(left/right): ")

        if escape=='left':
            print("The assasinator killed you with a sniper. YOU LOSE!")

        elif escape=='right':
            print("You drove yourself safely to your home. YOU WON!")

        else:
            print("Not a valid option. You lose")

    else:
        print("Not a valid option. You lose")
    

elif escape=='break':
    print("You broke the window and jumped. You are injured and bleeding.")
    escape=input("You have to search for a first aid kid. You see a building. Would you enter ?(yes/no)")

    if escape=='yes':
        print("You found a first aid kit. You healed and reached your home. YOU WON!")

    elif escape=='no':
        print("YOU LOSE! (excess blood lost)")

    else:
        print("Not a valid option. You lose")
    
else:
    print("Not a valid option. You lose")