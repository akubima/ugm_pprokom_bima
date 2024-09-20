a = {100,7,8}
b = {200,4,5}
c = {300,2,3}
d = {100,200,300}

separator = "-"*50

print(separator)
print("A - B = ", format(a.difference(b)))
print(separator)
print("B - D = ", format(b.difference(d)))
print(separator)
print("C - D = ", format(c.difference(d)))
print(separator)
print("A - B - C - D = ", format(a.difference(b).difference(c).difference(d)))