try:
    num,num2=eval(input("Enter Two numbers Sepretated By Commas: "))
    result=num/num2
    print("Result is ",result)
except ZeroDivisionError:
    print("You cannot Divide by Zero")

except SyntaxError:
    print("Comma Is Missing")

except:
    print("Wrong Input")

else:
    print("No Errors")

finally:
    print("This will run no matter what")