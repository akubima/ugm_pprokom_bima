"""
Authored by @akubima on 21-10-2024
at HS103
"""

matriks = []

for row in range(2):
    matriks.append([])
    for col in range(3):
        matriks[row].append(int(input(f"Masukkan nilai ke-[{row}][{col}] ")))

for row in range(2):
    for col in range(3):
        print(matriks[row][col], end=" ")
    print()