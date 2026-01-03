var = [1,2,3,4,5,6,7]
print(var)

emty1 = []
emty2= []
for i in var:
    if i %2 == 0:
        emty1.append(i)
    else:
        emty2.append(i)
print(emty1)
print(emty2)