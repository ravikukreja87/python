from abc import ABC , abstractmethod

class ABSC(ABC):
    def print(self, x):
        print(f"Value is {x}")

    @abstractmethod
    def task(self):
        print("This is an Abstract Method")
class child(ABSC):
    def task (self):
        print("This is the implementation of abstract method")

c =child()
c.print(100)
c.task()