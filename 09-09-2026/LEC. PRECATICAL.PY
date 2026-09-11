
# Creating String

name = "devam"
city = 'Gir'

print(name)
print(city)

# Multiline String


message = ''' Hello World
Welcome to 
Red and
 White 
 Education '''

print(message)

# String Indexing

text = "Programming"

print(text[0])
print(text[1])
print(text[-2])
print(text[-1])

# String Slicing

print(text[0:3])
print(text[2:7])
print(text[:3])
print(text[3:])
print(text[:])
print(text[:-1])
print(text[::2])
print(text[::-1])

# String Concatinating

first_name = "devam"
last_name = "bhut"
full_name = first_name + " " +  last_name
print(full_name)

# String Formatting - f-string

item = "pen"
price = 2.50
print(item)
print(price)
print(f"The price of {item} is {price} dollars.")

# Decimal Places

print(f"The price of {item} is {price:.2f} dollars.")

# Expression inside f-string

a = 20
b = 60
print(f"Sum = {a + b}")

# format() Method

print("The price of {} is {} dollers.".format(item , price))

# Positional Arguments

print("welcome , {0} {1}".format(first_name , last_name))

# Named Arguments

print("Hello , {first} {last}".format(first = first_name , last = last_name))
