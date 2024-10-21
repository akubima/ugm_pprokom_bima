a = {'a', 'b', 'c', 'd'}
b = {'c', 'd', 'e'}
c = set()

separator = "-"*50

print(separator)
print("A - B = ", format(a.difference(b)))
print(separator)
print("B - A = ", format(b.difference(a)))
print(separator)
print("A - C = ", format(a.difference(c)))
print(separator)
print("B - C = ", format(b - c))