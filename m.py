class flashcards:
    def __init__ (self, word ,meaning):
        self.word = word
        self.meaning = meaning

    def display(self):
        print(f"Word: {self.word}")
        print(f"Meaning: {self.meaning}")

flash = []
while True:
    word = input("Enter a word : ")
    meaning = input("Enter the meaning : ")
    flash .append (flashcards(word, meaning))
    c = input("Do you want to add more flashcards? (yes/no) : ")
    if c == "no":
        break

print("Your flashcards:")
for card in flash:
    card.display()              