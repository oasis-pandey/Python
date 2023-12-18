guests=['mom','dad','brother','sister']
print("hello everyone, I would like to inform you that i can invite only two people to dinner.")
no_brother=guests.pop(2)
no_sister=guests.pop(2)
print("Sorry, "+no_brother.title()+" I could not invite you.")
print("Sorry, "+no_sister.title()+" I could not invite you.")
print('Hello, ' +guests[0] + " and " +guests[1]+ " You're still invited to the dinner.")
del guests[0]
del guests[0]
print(guests)
