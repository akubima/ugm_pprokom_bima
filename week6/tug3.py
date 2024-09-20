a = {100,7,8}
b = {200,4,5}
c = {300,2,3}
d = {100,200,300}

separator = "-"*50

print(separator)
print("A & B = ", format(a.intersection(b)))
print(separator)
print("B & D = ", format(b.intersection(d)))
print(separator)
print("C & D = ", format(c.intersection(d)))
print(separator)
print("A & B & C & D = ", format(a & b & c & d))