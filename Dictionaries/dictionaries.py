aliens={'color':'green','points':5}
print(aliens['color'])
aliens['X dimension']=10
aliens['Y dimension']=15
print(aliens.keys())
print(aliens.values())
print(aliens.items())
print(aliens)
print(aliens['X dimension'])


aliens['color']='yellow'
print(f"the color of the alien is now {aliens['color']}")
