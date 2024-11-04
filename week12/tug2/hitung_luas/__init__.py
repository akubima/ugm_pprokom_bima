from interface.menu import menu
from interface.input import raw_input

def persegi():
    print( 'Menghitung Luas Persegi Panjang')
    p = int(input('Masukkan Panjang : '))
    l = int(input('Masukkan Lebar : '))
    luas = p*l
    print( 'Luas Persegi Panjang adalah ',luas)
    print()
    print( 'Coba lagi [Y/N]? ')
    back = raw_input().upper()
    if back == 'Y':
        menu()
    else:
        exit()
        
def lingkaran():
    print( 'Menghitung Luas Lingkaran')
    r = int(input('Masukkan Jari-Jari : '))
    luas = 3.14*(r**2)
    print( 'Luas Lingkaran adalah ',luas)
    print()
    print( 'Coba lagi [Y/N]? ')
    back = raw_input().upper()
    if back == 'Y':
        menu()
    else:
        exit()
def segitiga():
    print( 'Menghitung Luas Segitiga')
    a = int(input('Masukkan Alas : '))
    t = int(input('Masukkan Tinggi : '))
    luas = (a*t)/2
    print( 'Luas Segitiga adalah ',luas)
    print()
    print( 'Coba lagi [Y/N]? ')
    back = raw_input().upper()
    if back == 'Y':
        menu()
    else:
        exit()