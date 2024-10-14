"""
Authored by @akubima on 14-10-2024
at HS103
"""

jumlah = int(input("Masukkan jumlah data: "))

nomor = [i+1 for i in range(jumlah)]

print("Data Array: %s" % nomor)

kelipatan = int(input("Masukkan kelipatan yang ingin ditampilkan: "))

result = []

for i in nomor:
    if i % kelipatan == 0:
        result.append(i)

if len(result) > 0:
    print("Elemen yang merupakan kelipatan dari %s adalah:" % kelipatan)
    print(result)
else:
    print("Tidak ada elemen yang merupakan kelipatan dari %s" % kelipatan)