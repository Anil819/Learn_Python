
Student = {
           "name": "Anil Lohar",
           "Age": 21,
           "City": "Indore"
           }
print(type(Student))


Student["City"]="Hyderbad"
Student["Roll number"]= ["04381011"]


print(Student["name"])
print(Student["Age"])
print(Student["City"])
print(Student["Roll number"])

#Dictionary Method

print(Student.keys())
print(Student.values())
print(Student.items())
print(Student.get("name"))



