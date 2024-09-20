a = {'a', 'b', 'c', 'd'}
b = {'c', 'd', 'e'}
c = set()

separator = "-"*50

print(separator)
print("A ^ B = ", format(a.symmetric_difference(b)))
print(separator)
print("B ^ A = ", format(b.symmetric_difference(a)))
print(separator)
print("A ^ C = ", format(a.symmetric_difference(c)))
print(separator)
print("B ^ C = ", format(b.symmetric_difference(c)))