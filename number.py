L=[4,5,7,8,4,45,6,7,8,7,5,4,5,6]
print("Original list-",L)

count=0
for i in L:
    count += i


avg= count/len(L)

print(count)
print(avg)
L.sort()

print("Largest Element-",L[-1])
print("smallest Element-",L[0])