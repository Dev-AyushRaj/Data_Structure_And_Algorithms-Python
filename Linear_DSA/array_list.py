from array import *
a1 = array("i",[23,26,89])

print(type(a1))
print(a1)

for x in a1:
    print(x)

for i in range(len(a1)):
    print(a1[i], end=" ")


print()

i = 0
while i<len(a1):
    print(a1[i],end=" ")
    i += 1

a1.append(58)
print(a1)
print(a1.count(23))