m1=[1,2,3]
m2=[1,2,3]
result= map(lambda x,y: x+y, m1,m2)
print("Addition of two list")
print(list(result))

num=[1,2,3,4,5]
def sq(n):
    return n*n
square=list(map(sq, num))
print("Square of numbers in list")
print(square)

#Zip elements of two list
s1={2,3,1}
s2={"b","a","c"}
s3=list(zip(s1,s2))
print(s3"\n")

list1=[1,20,30,40]
list2=[100,200,300,400]
for x,y in zip(list1,list2[::-1]):
    print(x,y)

stocks=["reliance", "infosys","tcs"]
prices=[2175,1127,2750]

new_dict={stocks:prices for stocks,prices in zip(stocks,prices)}
print("\n".format(new_dict))