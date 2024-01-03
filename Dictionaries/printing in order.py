favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

for name in sorted(favorite_languages.keys()):
    print(name)

for name in favorite_languages.keys():
    print(name)

for language in set(favorite_languages.values()):
    print(language.title())
