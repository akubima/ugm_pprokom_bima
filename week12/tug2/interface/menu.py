def menu():
    print( 'Pilih Bentuk 2D')
    print()
    print( '1. Persegi Panjang')
    print( '2. Lingkaran')
    print( '3. Segitiga')
    print( '4. Keluar')

    pilihan = int(input('Masukkan Pilihan : '))
    while pilihan - 1 not in range(4):
        print( 'Pilihan tidak valid')
        pilihan = int(input('Masukkan Pilihan : '))

    match pilihan:
        case 1:
            from hitung_luas import persegi
            persegi()
        case 2:
            from hitung_luas import lingkaran
            lingkaran()
        case 3:
            from hitung_luas import segitiga
            segitiga()
        case 4:
            exit()