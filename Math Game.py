import random
print("Number Guessing Game")

while True:
    comp=random.randint(1 , 10)
    user=int(input("Enter any number From 1 To 10 : "))
    if user==comp:
        print("You Win")
        print("\n Congratulations")
        break


    else:
        print("You Lose")
        print("\n Try Again")
        print(f"\n The Correct Answer Was {comp}")  

print("Bye Bye")