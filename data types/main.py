#student details
name= str(input("enter your name"))
height= float(input("enter your height"))
age= int(input("enter your age"))
is_student= bool(input("are you a student? true or false"))
print("student name is", name)
print("student height is", height)
print("student age is", age)
print("are you a student?", is_student)
#type- function to tell what data type is stored in variable
print(type(name))
# typecasting- converting one data type to other data type
new_height=int(height)
print("new height is" , new_height)
new_age=float(age)
print("new age is" , new_age)
#string operations
word="avocado"
print("first letter", word[0])
print("last letter", word[-1])
print("number of chracters", len(word))
print(word[4:6])
print(word[::-1])