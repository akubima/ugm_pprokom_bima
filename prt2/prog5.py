# PPROKOM PRT2
# Authored by Bima M. B. Sajjad
# NIM: 24/538197/SV/24473
# 19/08/2024

# Meminta input user untuk detik berupa integer
print("=== MENGKONVERSI JUMLAH DETIK === \n")

###
# Try-catch block digunakan untuk secara aman menangani error yang mungkin
# terjadi saat program dijalankan.
###
try:
  # Jika N adalah jumlah detik (contoh: 100.000)
  n = int(input("Masukkan detik -> "))

  # Buatlah sebuah variabel A, yang berisi (60 * 60 * 24)
  a = (60 * 60 * 24)

  # Bagi nilai N dengan A, simpan di variabel HARI
  hari = (n // a)

  # Kalikan nilai A dengan HARI, simpan di variabel B
  b = (a * hari)

  #  Kurangi nilai N dengan B, simpan di variabel C
  c = (n - b)

  # Bagi nilai C dengan (60 * 60), simpan di variabel JAM
  jam = (c // (60 * 60))

  # Kalikan nilai JAM dengan (60 * 60), simpan di variabel D
  d = (jam * (60 * 60))

  # Kurangi nilai C dengan D, simpan di variabel E
  e = (c - d)

  # Bagi nilai E dengan 60, simpan di variabel MENIT
  menit = (e // 60)

  # Modulus nilai N dengan 60, simpan di variabel DETIK
  detik = (n % 60)

  # Print variabel hari, jam, menit, dan detik.
  print("\n" + str(n) + " detik sama dengan: " + str(hari) + " hari " + str(jam) + " jam " + str(menit) + " menit " + str(detik) + " detik", end=".")
except Exception as error:
    print("\n[Exception] "+ str(error))
