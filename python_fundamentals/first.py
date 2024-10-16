prin="he \n llo \n hii"
slicing = prin[1:4:2]
print(slicing)

print(prin.startswith("hel"))
print(prin.endswith("i"))
print(prin.capitalize())
print(prin.upper())
print(prin.lower())
print(len(prin))
b = "sushmitha "
print(len(b))
print(b[0:6:2])
print(prin)
print(f"welcome and, {prin}")

letter=''' hello my name is <|name|>
and today is <|date|>'''

print(letter.replace("hello","yash").replace("<|date|>","11 sept 2024"))

# wap to detect double sapce in string

a='[helo my name  is meoow]'
print(a.find('  '))
print(a.replace("  ","haha"))
print(a[0],a[4])


# list

l1=[66,2,3,4,5,6,7,8,44]
print(l1)

l1.sort()
print(l1)
l1.reverse
l1.append(20)
l1.insert(3,75)
print(l1)
l1.pop(3)
print(l1)
l1.remove(3)