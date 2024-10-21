nilai = set({3,6,9,2,5,7})
nilai2 = {1,4,8,10}
nilai = nilai.union(nilai2);
presisted = [6,9,2]

for el in list(nilai):
    if el in presisted:
        continue
    nilai.remove(el)

print(nilai)