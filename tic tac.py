b=[" "]*9
def print_board():
    print(f"{b[0]}|{b[1]}|{b[2]}")
    print("-+-+-")
    print(f"{b[3]}|{b[4]}|{b[5]}")
    print("-+-+-")
    print(f"{b[6]}|{b[7]}|{b[8]}")

def win(p):
    win=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for i in win:
        if b[i[0]]==b[i[1]]==b[i[2]]==p:
            return True
    return False
p ="x"
for i in range(9):
    print_board()
    print(f"Player {p}'s turn.")
    while True:
        try:
            move=int(input("Enter your move (1-9): "))
            if move<1 or move>9:
                print("Invalid move. Please enter a number between 1 and 9.")
            elif b[move-1]!=" ":
                print("That spot is already taken. Please choose another one.")
            else:
                b[move-1]=p
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
    if win(p):
        print_board()
        print(f"Congratulations! Player {p} wins!")
        break
    p="o" if p=="x" else "x"    
else: 
    print_board()
    print("It's a tie!")
    