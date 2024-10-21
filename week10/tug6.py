"""
Authored by @akubima on 21-10-2024
at HS103
"""
Array1 = [
    [4,6],
    [1,7]
]

Array2 = [
    [2,3],
    [5,6]
]

addition = []
substraction = []

for row in range(len(Array1)):
    addition.append([])
    for col in range(len(Array1)):
        addition[row].append(Array1[row][col] + Array2[row][col])

for row in range(2):
    substraction.append([])
    for col in range(2):
        substraction[row].append(Array1[row][col] - Array2[row][col])

print(f"Addition: {addition}")
print(f"Substraction: {substraction}")