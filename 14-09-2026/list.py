
print("="*40)

print("List in Python")

# create

fruits =['Apple' , 'Banana' , 'Mango' , 'Orange',  'Grapes']
           

print(fruits)

# Value Eccess

print(fruits[0])
print(fruits[1])
print(fruits[-1])
print(fruits[-3])


# Value Access through loop

print("Value Access through loop")

for fruit in fruits:
  print(fruit)

# Add New Value

# Python New Value Adding : Built-in Function (append())

fruits.append("Kiwi")

print(fruits)


fruits.sort()

print(fruits)

fruits.sort(reverse=True)

print(fruits)

# Tuple

# create

numbers = (44 , 45 , 46 , 47 , 48)

print(numbers)

# Access value from tuple individual

print(numbers[0])
print(numbers[1])

# Access value from tuple using loop

for num in numbers:
  print(num)

numbers[0] = 1 



# List Comprehension 

# Normal Method

square_value = []

for number in range(1 , 11):
  if number % 2 == 0:
    square_value.append(number)

print(square_value)

# List Comprehension

#[expression for item in iterable]

square_value = [number ** 2 for number in range(1 , 21)]

print(square_value)

# Even number

Even_value = [number for number in range(1 , 20) if number % 2 != 0]

print(Even_value)


numbers = list(range(1 , 20))

Even_value = [number for number in numbers if number % 2 != 0]

print(Even_value)







