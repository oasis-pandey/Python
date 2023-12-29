'''
4-10. Slices: Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:

•	 Print the message, The first three items in the list are:. Then use a slice to
print the first three items from that program's list.

•	 Print the message, Three items from the middle of the list are:. Use a slice
to print three items from the middle of the list.

•	 Print the message, The last three items in the list are:. Use a slice to print
the last three items in the list.

'''
alphabets=['a','b','c','d','e','f','g','h','i']
print("the first three items in the list are: ")
print(str(alphabets[:3])+"\n")
print("the 3 middle items are: ")
print(str(alphabets[3:6])+ "\n")
print("the last 3 items are: ")
print(str(alphabets[6:])+"\n")