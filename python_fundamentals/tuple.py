#tuple 
a=(1,)
print(type(a))
print(a)
a=(1,2,3,4,5,6,7,8)
print(a)
a=(2,3,4,3,3,3,5,6,7,8,9)
print(a)
print(a.count(3))
print(a.index(3))

#wap to input fruits name and add in  tuple
a=[]
f1=input("enter 1st fruit name: ")
a.append(f1)
f2=input("enter 1st fruit name: ")
a.append(f2)
f3=input("enter 1st fruit name: ")
a.append(f3)
f4=input("enter 1st fruit name: ")
a.append(f4)
print(a)
a=tuple(a)
print(a)
print(type(a))

#wap to sum 4list

l1=[2,3,5,6]
print(sum(l1))