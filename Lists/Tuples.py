'''

4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five 
simple foods, and store them in a tuple.

•	 Use a for loop to print each food the restaurant offers.
•	 Try to modify one of the items, and make sure that Python rejects the 
change.
•	 The restaurant changes its menu, replacing two of the items with different 
foods. Add a block of code that rewrites the tuple, and then use a for
loop to print each of the items on the revised menu.

'''

foods=('pizza','burger','momo','chowmean','sewale')
print('\n')
print('the menu is:')
for food in foods:
    print(food)
print('\n')

foods=('pizza','burger','momo','masu','bhat')
print('the revised food menu are:'+'\n')
for food in foods:
    print(food)

