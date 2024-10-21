"""
Authored by @akubima on 21-10-2024
at HS103
"""

counter = 0
elements = [i for i in range(10, 18)]
array = []

for row in range(4):
    array.append([])
    for col in range(2):
        array[row].append(elements[counter])
        counter += 1

first_col = [elem[0] for elem in array]
print(first_col)