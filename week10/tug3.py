"""
Authored by @akubima on 21-10-2024
at HS103
"""

X = [
    [12, 7],
    [4, 5],
    [3, 8]
]

result = []

for row in range(len(X[0])):
  result.append([])
  for col in X:
    result[row].append(col[row])
    
for r in result:
 print(r)