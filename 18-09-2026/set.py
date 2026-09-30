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

  # Average Score

total = 0

for i in students:
  total += i["score"]

average = total / len(students)

print(average)

# Add New Student

students.append({
  "id":104,
  "name":"Amit",
  "score":88
})

print("\n Student Added Successfully.")

print(students)

# Update student details (id:103 , new_score:79)

# students[2]["score"] = 79

for student in students:
  if student["id"] == 103:
    student["score"] = 79

print(students)

# Delete Student ("Pooja")

# for student in students:
#   if student["name"] == "Pooja":
#     students.remove(student)

# print("Student Delete Successfully!")

# print(students)

# Student Score > 80 

for student in students:
  if student["score"] < 80:
    print(student["name"] , "--", student["score"])

# Sort Decending Way

students.sort(key = lambda x : x["score"] , reverse=True)

print(students)

# Highest score student

highest = students[0]

for student in students:
  if student["score"] > highest["score"]:
    highest = student

print(highest["name"])

# Student report card

grade_count = {
  "A" : 0,
  "B" : 0,
  "C" : 0
}

for student in students:

  score = student["score"]

  if score >= 90:
    grade = "A"

  elif score >= 80:
    grade = "B"

  else:
    grade = "C"

  grade_count[grade] += 1

  print("Name :" , student["name"] , "\n" , "Score :" , score , "\n" , "Grade :" , grade)

  print(grade_count)
  
