
# % formatting

print("% Formatting")

name="Rahul"
city="Ahmedabad"
age = 25

print("My name is %s and my city is %s and my age is %d." % (name , city ,  age))

'''

%s : String
%d : Integer
%f : Float
%.2f : Float with 2 decimal places

'''

# String Case Manipulation

text = "PYTHON PROGRAMMING LANGUAGE"
print("Original Case :" , text) 

print("Upper :" , text.upper())

print("lower :" , text.lower())

print("title:" , text.title())

print("Capitalize:" , text.capitalize())

print("Swapcase:" , text.swapcase())

# String Searching

sentence = "Machine Learning and AI are AI trending."
print(sentence)
print("AI Position:" , sentence.find("AI"))
print("AI exists:" , "AI" in sentence)
print("AI index:" , sentence.index("AI"))
print(sentence.startswith("M"))
print(sentence.endswith("."))
print(sentence.endswith("trending."))

# String Replacement

sentence = "Machine Learning and AI are AI trending."
new_sentence = sentence.replace("AIML" , "Artificial Intelligence MACHINE LEARNING" , 1)
new_sentence_2 = sentence.replace("AIML" , "Artificial Intelligence MACHINE LEARNING" , 1)

print(new_sentence)
print(new_sentence_2)

# String Counting

data = "data mining and big data"

print(data.count("d"))


# String Split

fruits = "apple , banana , mango , graps"
fruits_list = fruits.split(",")
print(fruits_list)
data = "data mining and big data"
words = data.split()
print(words)