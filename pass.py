for i in range (10):
    if i % 20==0:
        print("Twist")
    elif i % 15 == 0:
        pass
    elif i % 10 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Nothing")
    
    else:
        print (i)
