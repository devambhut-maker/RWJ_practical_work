# Q1. Find Length of array 

new_arr = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]

print('Length of Array :' , len(new_arr))

count = 0

for i in new_arr:
  count += 1

print("Length Of Array :" , count)

# Average of array

sum_new_array = sum(new_arr)

average_array = sum_new_array / len(new_arr)

print('Average of Array :' , average_array)

# Addition of two arrays 


new_arr_1 = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
new_arr_2 = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]

new_arr_3 = []

for i in range(len(new_arr_1)):
  value = new_arr_1[i] + new_arr_2[i]
  new_arr_3.append(value)

print(new_arr_3)

# Search Element in Array

find_element = 10

found = False

new_arr_1 = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]

for i in new_arr_1:
  if i == find_element:
    print(f"{find_element} present in array.")
    found = True
    break

if found == False:
  print(f"{find_element} is not present in array.")


# Print First , Middle and last Element in Array.abs


new_arr_1 = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]

print("First Element :" , new_arr_1[0])
print("Middle Element : " , new_arr_1[len(new_arr_1)//2])
print("Last Element : " , new_arr_1[-1])


# 2D array

array_2d = [
  [1 , 2 , 3],
  [4 , 5 , 6],
  [7 , 8 , 9]
]

print(array_2d)
print(array_2d[1][2])

# Q1. Create and Display a 3 x 3 Matrix

matrix = []
list_1 = []

for i in range(3):
  for j in range(3):
    value = int(input("Enter Elements : "))
    list_1.append(value)
  matrix.append(list(list_1))


print(matrix)




# print(matrix)