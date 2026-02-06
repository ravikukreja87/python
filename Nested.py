valid=False

while not valid:
    try:
      cc=int(input("Enter Any Number: "))
      while cc%2==0:
         print("Bye")
      valid=True
    except ValueError:
       print("ERROR")
