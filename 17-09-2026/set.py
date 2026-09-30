# Sets , Dictionary , Type Conversion , List of Dictionary

# Set

print("Q1. Set Operations")

numbers = {1 , 2 , 2 , 4 , 5}
num = [1 , 2 , 2 , 3 , 4]
num_tuple = (1 , 2 , 2 , 3 , 4)

print(numbers)
print(num)
print(num_tuple)

numbers.add(6)
numbers.remove(1)

print(numbers)

print("Is 1 Present?" , 1 in numbers)


num = [1 , 2 , 3 , 4 , 4 , 5 , 6 , 6]

set_num = set(num)

list_num = list(set_num)

print(list_num)

# Dictionary Operation

print("Q2. Dictionary")

student = {
  "name":"Devam",
  "age" : 19,
  "grade" : "A"
}


print(student["name"])

student["city"] = "Gir"

del student["age"]

print(student)

for key in student.keys():
  print(key)

for value in student.values():
  print(value)

for key in student.keys():
  print(f"{key} : {student[key]}")

# Dictionary from List

print("Dictionry From List")

keys = ['id' , 'name' , 'email']
values = [101 , "Devam" , 'devam@gmail.com']

employee = {}

for i in range(len(keys)):
  employee[keys[i]] = values[i]

print(employee)

# Delete List Item

# del keyword

numbers = [10 , 20 , 30 , 40 , 50]

print(numbers)

del numbers[2]

print(numbers)

# Student Management System

print("Student Management System")

students = [
  {"id" : 101 , "name":"Komal" , "score":85},
  {"id" : 102 , "name":"Devam" , "score":75},
  {"id" : 103 , "name":"Devam" , "score":89}
]

print(students)

# Print students Names

for i in students:
  print(i["name"])