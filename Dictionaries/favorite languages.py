favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

friends = ['phil', 'sarah']

for names in favorite_languages.keys():
    print(names.title())

for name in friends:
    if name in favorite_languages:
        print("Hello, "+name+" Glad to hear that your favorite language is "+favorite_languages[name].title()+"!")
