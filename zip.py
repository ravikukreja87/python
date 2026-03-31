a={1,2,3,4}
b={6,7,8,9}
r=zip(a,b)
print(list(r))

A=[1,2,3,4,5,6,7,8]
B=["a","b","c","d","e","f","g","h"]
for i in zip(A,B[::-1]):
    print(i)