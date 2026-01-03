t = ()
t2 = (12,13,14,15,11)
print(t2)

t3=(6,"code",90.300,False)
print(t3)

t4=(8,)
t5=t2+t4
print(t5)

t6=(9,0,4,4,4,100)
print(t6.count(2))
print(t6[2:5])

weather= (1,0,0,0,1,0,1,1,1,1,1)
sunny=0
rainy=0
for i in range(0,11):
    if(weather[i]==0):
        rainy+=1
    else:
        sunny+=1
if(sunny>rainy):
    print("Good weather")
else:
    print("Bad weather")