num1=[1,2,3]
num2=[4,5,6]
result=map(lambda x,y :x+y,num1,num2)
print(list(result))

p=[1,2,3,4,5]

def square(x):
    return x**2

result=map(square,p)
print("The Square of the p is", list(result))