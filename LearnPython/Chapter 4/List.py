marks = [89, 35, 78, 98]
student = ["Samosa", "Mango", 24, 98]
# marks[0] = 90   Change (Mutable)


print(max(marks))  # List Functions
print(min(marks))  # List Functions


marks.append(100)  #List Method
print(marks)

marks.insert(0, 35) #List Method
print(marks)

marks.remove(78) #List Method
print(marks)

marks.pop(2) #List Method
print(marks)

marks.sort() #List Method
print(marks)

marks.reverse() #List Method
print(marks)


print(len(marks), marks)
print("The First value of markslist", marks[1])
print(student)
