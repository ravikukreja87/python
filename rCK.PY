import random
choices=["rock","paper", "scissor"]
xomputer=random.choice(choices)
print(choices)
user=input("Choose From Above: ")

print("Computer Chose ",xomputer)
if user==xomputer:
    print("Tie")

elif user=="rock" and xomputer=="paper":
    print("Computer Win")

elif user == "paper" and xomputer=="scissor":
    print("Computer Win")
   
elif user == "scissor" and xomputer=="rock":
    print("Computer Win")

else:
    print("User Win")

    