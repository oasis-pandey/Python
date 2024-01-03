favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

polls=['sam','malika','oasis','jen','phil']
for poll in polls:
    if poll in favorite_languages.keys():
        print("Thank you "+ poll.title()+", for responding!")
    else:
        if poll not in favorite_languages.keys():
            print("Hey "+poll.title()+", You are invited to poll.")

