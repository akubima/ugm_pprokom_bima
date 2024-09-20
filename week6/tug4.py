a = {100,7,8}
b = {200,4,5}
c = {300,2,3}
d = {100,200,300}

separator = "-"*50

print(separator)
print("A - B = ", format(a.difference(b)))
print(separator)
print("B - C = ", format(b.difference(c)))
print(separator)
print("B - C - D = ", format(b.difference(c).difference(d)))
print(separator)
print("A - B - C - D = ", format(a - b - c - d))