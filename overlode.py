class A():
    def __init__ (self ,a ):
        self .a = a 
        

    def __lt__(self, other):
        if self.a < other.a:
            return("Ob1 is Less Than Ob2")
        else:
            return("Ob2 is Less Than Ob1")
        
    def __eq__ (self, other):
        if self.a == other.a:
            return("Ob1 is Equal To Ob2")
        else:
            return("Ob1 is not Equal to Ob2")
        
ob1 =A(10)
ob2 =A(20)
print(ob1 < ob2)
print(ob1 == ob2)
