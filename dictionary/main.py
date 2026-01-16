student_detail={"name": "Tchiyna","Grade":8,"City":"Luanda", "Country":"Angola"}
print(student_detail)

#adding a value
student_detail["language"]="Portoguese"
print(student_detail)

#remove a value
del student_detail["Grade"]
print(student_detail)

#updating a value
student_detail["City"]="Lagos"
print(student_detail)

print(len(student_detail))
for i in student_detail.keys():
    print(i)

for i in student_detail.values():
    print(i)

for i in student_detail.items():
    print(i)

print("name of the student is",student_detail["name"])

print("city of the student is",student_detail.get("City","not found"))
print("city of the student is",student_detail.get("Grade","not found"))