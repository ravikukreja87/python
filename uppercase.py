class IString:
    def __init__(self):
        self.value = ""
    def set_value(self):
        self.value = input("Enter a string: ")
    def get_value(self):
        print(self.value.upper())
itring = IString()

itring.set_value()
itring.get_value()