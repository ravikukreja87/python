class Myclass:
    __a = "Private Variable"

    def __private_method(self):
        print("This is a private method")

    def hello(self):
        print("Hello World")
        print(Myclass.__a)
obj = Myclass()
obj.hello()
obj.__private_method()