class dog:
    def bark(self):
     return "bhaw bhaw"
    
dog1=dog()
dog1.name="tommy"
print(dog1.bark())

class items:
    def say_my_name(self,name):
        return name +" You're Goddam Right"
    
name1=items()
first_name=name1.say_my_name('Heisenberg')
print(first_name)
