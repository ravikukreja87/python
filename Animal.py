from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass

class human(Animal):
    def move(self):
        print("I can walk and run")


class snake(Animal):
    def move(self):
        print("I can crawl")

class dog(Animal):
    def move (self):
        print("I can Bark")

    
R = human()
R.move()

s = snake()
s.move()

d = dog()
d.move()

