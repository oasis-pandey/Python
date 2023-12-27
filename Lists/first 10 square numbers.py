# we are going to work on printing first 10 square numbers

number=[] # we start by introducing an empty list
for i in range(1,11):
    value= i**2 # it takes numbers from 1 to 10 and (**2 i.e squares them)
    number.append(value) # it adds the squared number to the list

print(number) # it prints the first 10 square numbers

#simple statistics in python
digits=[1,2,3,4,5,6,7,8,9,10]
print(min(digits)) 
print(max(digits))
print(sum(digits))
