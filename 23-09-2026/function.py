# Global Keyword
'''
count = 0

def my_count():
  global count
  count += 1
  print("Function called" , count)

my_count()
my_count()
my_count()

# Global veriable updated inside function Sum of all numbers entered by the user


total = 0

def add_num(num):
  global total
  total += num

n = int(input("How many numbers do you want to enter? :"))

for i in range(n):
  num = int(input(f"Enter number {i} : "))
  add_num(num)

print(total)
'''
# Modify global veraible stroring username

'''
username = "VIP Guest"

def change_username(new_name):

  global username
  username = new_name


print("Before :" , username)

new_username = input("Enter new username : ")

change_username(new_username)

print("After :" , username)

'''
# Return Multiple Value
'''
def multi_operation(numbers):

  total = sum(numbers)
  maximum = max(numbers)
  minimum = min(numbers)

  return total , maximum , minimum

numbers = [10 , 20 , 30 , 40 , 50]

total , maximum , minimum = multi_operation(numbers)

print(total)
print(maximum)
print(minimum)
'''

# Split string into two parts:
# 1. Only vowels
# 2. Remining characters
'''
def split_string(text):
  vowels = ""
  remaining = ""

  for char in text:

    if char.lower() in "aeiou":
      vowels += char

    else:
      remaining += char

  return vowels , remaining


text = input("Enter a string :")

vowels , remaining = split_string(text)

print("Vowels : " , vowels)
print("Remaining : " , remaining)

'''

def prime(n , i = 2):

  if n < 2:
    return False
  if i == n:
    return True
  if n % i == 0:
    return False
  return prime(n , i + 1)


def print_prime(start , end):
  if start > end:
    return
  
  if prime(start):
    print(start)

  print_prime(start + 1 , end)

start = int(input("Enter start number:"))
end = int(input("Enter end number:"))

print_prime(start , end)