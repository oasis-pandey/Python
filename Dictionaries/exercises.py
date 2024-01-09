rivers={
    'nile':'egypt',
    'amazon':'brazil',
    'karnali':'nepal'
}
# for river, country in rivers.items():
#     print("The "+ river.title() +" river runs through "+country.title()+".")

# for river, country in rivers.items():
#     print(river)
#     print(country)
# print(rivers.get('nile'))
rivers.update({'ram':'shyam'})
print(rivers)
print(rivers.items())
rivers.pop('amazon') # DELETE A VALUE
print(rivers.get('ram')) # ACCESS A CERTAIN VALUE
rivers.popitem()# DELETES THE LAST VALUE 
print(rivers)
rivers.clear()# DELETES EVERYTHING
print(rivers)

