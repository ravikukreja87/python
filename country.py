class India:
    def capital(self):
        print("New Delhi")

    def Language(self):
        print("Hindi")

class Usa:
    def capital(self):
        print("Washington DC")  

    def Language(self):
        print("English")
obj_india = India()
obj_Usa = Usa()

for i in (obj_india, obj_Usa):
    i.capital()
    i.Language()

