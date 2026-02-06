try:
    num=int(input("Enter any number: "))
    print("The number is ",num)
except ValueError as ea:
    print("Exception:",ea)
    