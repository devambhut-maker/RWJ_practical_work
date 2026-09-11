# String JOIN

words = ['Python' , 'is' , 'awesome']

result = "   ".join(words)

print(result)

# String Strip

text = "     Hello Python    ";

print("strip :" , len(text.strip()))
print("lstrip :" , len(text.lstrip()))
print("rstrip :" , len(text.rstrip()))
print("strip :" , text.strip())
print("lstrip :" , text.lstrip())
print("rstrip :" , text.rstrip())

print(len(text))

# Remove Non-Alphabetic Character


text = "DataScience123#@AIML!"

clean_text = ""

for char in text:
  if char.isalpha():
    clean_text += char

print(text)
print(clean_text)

# String Cheking Method

text = "   " 

print(text.isalpha())
print(text.isdigit())
print(text.islower())
print(text.isupper())
print(text.isspace())

# Reverse String

text = 'Python'

reverse_text = "".join(reversed(text))
reverse_text1 = list(text)
reverse_text1.reverse()
print("".join(reverse_text1))
print(text[::-1])
print(reverse_text)

'''
text = input("\n Enter a string to check palindrome:")
reverse_text = text[::-1]
print(text)
print(reverse_text)
 

if text.lower() == reverse_text.lower():
  print("Palindrome")
else:
  print("Not a Palindrome") 
  
'''


# Escape Characters

print("Hello\nWorld")
print("Hello\tworld")
print("she talk \"hello\"")
print('It\'s Python')
print("C:\\Python")