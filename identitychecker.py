a = [1,2,3,4]
b = [2,3,4,5,]
c = a

print(id(a))
print(id(b))
print(id(c))

print(a is b)
print(a is c)
print(b is c)

print(a is not b)
print(a is not c)
print(b is not c)