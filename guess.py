import random
computer=random.randint(1,26)
print("Welcome to the guessing game!")
print("I have selected a number between 1 and 25. Can you guess it?")
print("I will give you hints along the way. Let's get started!")
ATTEMPTS=0
while True:
    try:
        guess=int(input("Enter your guess: "))
        ATTEMPTS+=1
        if guess==computer:
            print(f"Congratulations! You've guessed the number {computer} in {ATTEMPTS} attempts!")
            break
        else:
            if guess<computer:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
            if computer%2==0:
                print("Hint: The number is even.")
            else:
                print("Hint: The number is odd.")   
            if ATTEMPTS==5:
                print(f"Don't worry! The number is {computer}. Better luck next time!")
                break
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 25.")