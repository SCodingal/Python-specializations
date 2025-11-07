x=5 
if (type(x) is int):
    print("true")
else:
    print("false")

x=0.5
if (type(x) is not float):
    print("true")
else:
    print("false")

x=20
y=20
if (x is y):
    print("x and u SAME identity")

a=[1,2,3]
b=[1,2,3]
print(a is b)

#Membership operator
var= "Pineapple"
if "e" in var:
    print("NOT FOUND")
else:
    print("found")