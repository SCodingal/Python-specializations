emtpy_list=[]
print()

numbers = [1,2,3,4,5,]
print(numbers)
print("First element", numbers[0])
print("Last element", numbers[-1])

triples = [1,2,3]*3
print(triples)

aList = [100,200,300,400,500]
aList = aList[::-1]
print(aList,"\n")
print("minimum value", min(aList))
print("maximum value", max(aList))
print(len(aList))

student_details = ["Tchiyna", 8, 168.88, True]
print(student_details)
student_details.append(33)
print(student_details)

student_details.remove(168.88)
print(student_details)
student_details.insert(2,"Orange")
print(student_details)

var = [1,1,2,3,5,5]
print(var.count(1))
var.reverse()
print(var)
var.sort()
print(var)
var.pop()
print(var)
a = var.pop()
print(a)