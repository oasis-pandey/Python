"""
guests=['mom','dad','brother','sister']
not_make_it=guests.pop(1)
guests.insert(1,'anoodit')
print("those who would be invited are:"+','.join(guests)) 

print(not_make_it+" could not make it to the dinnner.So, I'll be removing "+not_make_it+" and adding "+guests[1]+".")
for p in range(4):
    print("Hello, "+ guests[p]+" you are invited to join me on dinner tomorrow.")
    p=p+1
guests=['mom','dad','brother','sister']
print("Hello everyone, I found a bigger dinner table so i would like to invite more people besides: "+",".join(guests))
guests.insert(0,"anoodit")
guests.insert(3,"roshni")
guests.append("anushka")

for i in guests:
    print("Hello, "+i+" you are invited to dinner tomorrow.")

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

 EXERCISE 3.8
locations=['india','nepal','china','bhutan','usa']
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations,reverse=True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)
"""




