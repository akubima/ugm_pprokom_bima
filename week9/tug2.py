"""
Authored by @akubima on 14-10-2024
at HS103
"""

nilai = []
for i in range(5):
    nilai.append(float(input("Masukkan nilai mahasiswa %s: " % (i+1))))
    print("Data nilai mahasiswa:", nilai)

jumlah: float = sum(nilai)
average: float = jumlah / len(nilai)

option: str = input("Apakah Anda ingin melihat jumlah nilai atau rata-ratanya? (jumlah/rata-rata):")

while option != "jumlah" and option != "rata-rata":
    print("Pilihan tidak valid, ketikkan hanya 'jumlah' atau 'rata-rata' tanpa tanda petik! (CTRL+C untuk keluar)")
    option: str = input("Apakah Anda ingin melihat jumlah nilai atau rata-ratanya? (jumlah/rata-rata):")

if option == "jumlah":
    print("Jumlah nilai mahasiswa:", jumlah)
elif option == "rata-rata":
    print("rata-rata nilai mahasiswa:", average)