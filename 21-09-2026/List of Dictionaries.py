# Python Functions

# 1. Built-in Functions vs User-Defined Function
# 2. Arbitrary Arguments
# 3. Keyword Arguments
# 4. __doc__ (docstrings)


# Q1. Built-in Function

numbers = [45 , 12 , 85 , 22 , 60]

print("Original List" , numbers)
print("Length" , len(numbers))
print("Maximum",  max(numbers))
print("Sorted",  sorted(numbers))
print("Sum" , sum(numbers))
print("Data Types " , type(numbers))


# User-defined function

# syntax

"""

def functionName(parameter):
  # code

"""

def greet(name):
  """ Create a function with greet name a person by name. """
  return f"Hello , {name} Welcome to the Python Class."

print(greet("Vivek"))


def add_numbers(*args):
  """ Add any number of arguments passed to it and return the total """
  total = 0
  for num in args:
    total += num
  return total

print(add_numbers(10 , 20 , 30 , 40))



# **kwargs

def student_summary(*args , **kwargs):
  """ Demonstrate using *args and **kwargs together in the same function """
  print("Positional args:" , args)
  print("Keyword args ", kwargs)

student_summary("vivek" , 20 , 89)
student_summary(name="vivek")

def product_details(**kwargs):
  total = kwargs["price"] * kwargs["quantity"]

  return f"""
    ProductName : {kwargs['name']}
    ProductPrice : {kwargs['price']}
    ProductQuantity : {kwargs['quantity']}
    Total : {total}
    """

print(product_details(name="Laptop" , price=45000 , quantity=2))


print(student_summary.__doc__)
print(add_numbers.__doc__)




