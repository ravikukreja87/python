class Element:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def display(self):
        print("x:",self.x)
        print("y:",self.y)

obj=Element(5,8)
obj.display()