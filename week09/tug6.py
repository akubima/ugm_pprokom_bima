"""
Authored by @akubima on 14-10-2024
at HS103
"""

daftar = [1, 5, 4, 6, 7, 12, 45, 9, 99, 55, 100, 88, 75, 60]

genap = [i for i in daftar if i % 2 == 0]
ganjil = [i for i in daftar if i % 2 != 0]
jumlah_genap = len(genap)
jumlah_ganjil = len(ganjil)

print(daftar)

print("Ini adalah angka genap:", genap)
print("Jumlah angka genap: %s angka" % jumlah_genap)
print("Ini adalah angka ganjil:", ganjil)
print("Jumlah angka ganjil: %s angka" % jumlah_ganjil)