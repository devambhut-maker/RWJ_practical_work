# Sets , Disctonary , Type Conversion , List of Dictionary

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