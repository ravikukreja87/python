class parrot:
    species = "bird"
    def __init__(self,name,age):    
        self.name = name
        self.age = age

blu = parrot("Blu", 10)
woo = parrot("Woo", 15)

print("{} is a {} and is {} years old.".format(blu.name,blu.species, blu.age))
print("{} is a {} and is {} years old.".format(woo.name,woo.species, woo.age))