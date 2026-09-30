# A 1D Array in Python is seperated using a list. Here , We create a list containing some data / content
# values.

# Types of Array

# 1. Homogeneous Array

# A Homogeneous array contain element of the same data type.

numbers = [10 , 12 , 14  , 18 , 22 , 28 ]

print(numbers)

# All element are integers(int) This is called a Homogeneous list.

fruits=["Apple" , "Banana" , "Orange" , "Mango"]

print(fruits)


# 2. Heterogeneous Array

# A Heterogeneous array contains element of diffrent data types.


student = ["vivek" , 25 , 89.30 , True]

print(student)


# Example : 1

numbers = [10 , 20 , 30 , 40 , 50 , 60]

print(numbers[0])
print(numbers[3])

for num in numbers:
  print(num)



size = int(input("Enter Size of Array : "))

numbers = []

for i in range(size):
  value = int(input(f"Enter Element {i + 1} : "))
  numbers.append(value)

print(numbers)

for num in numbers:
  print(num)