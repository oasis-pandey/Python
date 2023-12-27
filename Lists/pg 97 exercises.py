'''
4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
inclusive
''' 
numbers=[]
for i in range(1,21):
    print(i)
    numbers.append(i)
print(numbers)

'''
4-4. One Million: Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, stop it by
pressing ctrl-C or by closing the output window.

''' 

'''
million=list(range(1,1000001))
for i in million:
    print(i)
'''

'''
4-5. Summing a Million: Make a list of the numbers from one to one million,
and then use min() and max() to make sure your list actually starts at one and
ends at one million. Also, use the sum() function to see how quickly Python can
add a million numbers.
'''

'''

mil=list(range(1,1000001))
print(min(mil))
print(max(mil))
print(sum(mil))

'''

'''
4-6. Odd Numbers: Use the third argument of the range() function to make a list
of the odd numbers from 1 to 20. Use a for loop to print each number.
'''

print("the odd numbers are:", list(range(1,20,2)))
