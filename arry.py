import array as arr
a=arr.array('i',[1,2,3,3,33,4,5])
print("The original array is-",a)
print("The Times 3 occurs-",a.count(3))
a.reverse()
print("The reversed array is-",a)