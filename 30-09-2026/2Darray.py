# Transpose of 2 X 3 array

matrix = [
  [1 , 2 , 3],
  [4 , 5 , 6]
]

output = []

for j in range(3):
  row = []

  for i in range(2):
    row.append(matrix[i][j])

  output.append(row)

print(output)

for row in matrix:
  print(row)

for row in output:
  print(row)

# Sum of two matrix

matrix_1 = [
  [1 , 2 , 3],
  [4 , 5 , 6]
]

matrix_2 = [
  [1 , 2 , 3],
  [4 , 5 , 6]
]

# output = [[0 , 0 , 0],[0 , 0 , 0]]

# for i in range(len(matrix_1)):

#   for j in range(3):
#     output[i][j] = matrix_1[i][j] + matrix_2[i][j]

# print(output)

output = []

for i in range(2):
  row = []
  for j in range(3):
    value = matrix_1[i][j] + matrix_2[i][j]
    row.append(value)

  output.append(row)

print(output)


# Find Minimum and Maximum value in Matrix

matrix_1 = [
  [10, 2 , 9],
  [4 , 5 , 6]
]

maximum = matrix_1[0][0]
minimum = matrix_1[0][0]

for i in matrix_1:
  for value in i:
    if value > maximum:
      maximum = value
    if value < minimum:
      minimum = value

print("Maximum" , maximum)
print("Minimum" , minimum)
