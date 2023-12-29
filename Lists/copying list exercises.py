'''
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
(page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
Then, do the following:

Add a new pizza to the original list.
Add a different pizza to the list friend_pizzas
Prove that you have two separate lists.

 Print the message, My favorite pizzas are:, and then use a for loop to print the first list

 Print the message,My friend’s favorite pizzas are:, and then use a for loop to print the second list.
 
  Make sure each new pizza is stored in the appropriate list.
  '''

my_pizzas=['chicken','buff','veg','cheese']
friend_pizzas=my_pizzas[:]  # if you use [:] then only it will be copied , if you won't then it will equate
my_pizzas.append('a')      # CHECK THE DIFFERENCE WITH AND WITHOUT [:]
friend_pizzas.append('b')
print("my fav pizzas are: ")
print(str([x for x in my_pizzas])+"\n")
print("my friend's fav pizzas are :")
print(str([i for i in friend_pizzas])+"\n")

