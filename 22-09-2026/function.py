# Python Functions

# 1. Recursive Function
# 2. lambda Function
# 3. Global Keyword
# 4. Return Multiple value


# 1. Recursive Function

# Function call itself.
'''
def fectorial(n):
  if n < 0:
    return "Factorial is not possible for negative numbers"

  if n == 0 or n == 1:
    return 1
  
  return n * fectorial(n - 1)


num = int(input("Enter a number:"))
print(fectorial(num))
'''
'''
def fibonacci(n):
  if n <= 0:
    return 0

  if n == 1:
    return 1

  return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter fibonacci number:"))

print(fibonacci(num))

for i in range(num):
  print(fibonacci(i) , end=" ")
'''
# Lambda Function

# Calculate square of number

# def square(n):
#   return n * n


# print(square(10))
# print(square(5))
'''
square = lambda x : x * x

num = int(input("Enter a number:"))

print(square(num))
'''
# Filter odd number using lambda function filter()

numbers = [10 , 15 , 20 , 25 , 30 , 35 , 40 , 45 , 50]

odd_num = list(filter(lambda x : x % 2 != 0 , numbers))

print(odd_num)

print(max(numbers))
print(min(numbers))

largest = lambda a , b , c : min(a , b , c)

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

print(largest(a , b, c))