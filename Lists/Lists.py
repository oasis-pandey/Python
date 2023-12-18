#LISTS

#to print specific item in a list
alphabets = ['a','b','c','d','e'] 
print(alphabets[0])


# to add in a list
alphabets.insert(5,'f')
print(alphabets)


#to remove from a list
del alphabets[5]
print(alphabets)

#POP COMMAND


# pop command can be used to delete an item in the list while storing the deleted value in a variable. For example:

popped_alphabets= alphabets.pop()# here the popped alphabet i.e "e" is stored 
print(alphabets) #here it shows that the last item was popped i.e "e" and it gives only remaining values i.e a,b,c,d
print(popped_alphabets)#this print the deleted item from the list which is stored in popped_alphabets


#you can also use pop to remove specific items. For example:
popped_alphabets= alphabets.pop(1) # pops the 2nd value i.e "b" and stores in popped_alphabets
print(alphabets) #print the list of alphabet removing the 2nd value
print(popped_alphabets) # prints the removed value i.e "b"

#you can also remove an item from the list by using remove command. For example:
alphabets = ['a','b','c','d','e'] 
first_alphabet="a"
removed_alphabet=alphabets.remove(first_alphabet)
print(alphabets)
print("I removed "+first_alphabet.upper()+" because it's the first letter in the alphabets")

#SORTING THE LISTS
locations=['india','nepal','china','bhutan','usa']
print(locations)
print(sorted(locations)) # sorts in alphabetical order 
print(locations)
print(sorted(locations,reverse=True))#sorts in reverse alphabetical order
print(locations)
locations.reverse()#changes the order of list
print(locations)
locations.reverse()
print(locations)
locations.sort()#sorts in alphabetical order PERMANENTLY
print(locations)
locations.sort(reverse=True)#sorts in reverse alphabetical order PERMANENTLY
print(locations)
print(len(locations)) # gives the length of a list (starts from 1 here)





