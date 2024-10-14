"""
Authored by @akubima on 14-10-2024
at HS103
"""

bilangan = [4, 5, 11, 12, 14, 16, 16, 19]

prima = [i for i in bilangan if i % 2 != 0 or i == 2]

print("Bilangan prima dari \n%s\nadalah:\n%s\ndan jumlahnya ada: %s" % (bilangan, prima, len(prima)))