# Rock, paper, scissor.
# Authored by @akubima
# on 2-9-2024

import random
import time

print("=== BATU KERTAS GUNTING ===".center(50))
print()

options = {
    1: "batu",
    2: "kertas",
    3: "gunting"
}

separator = "-"*20
point_system = 0
point_user = 0

try:
    for option in options.keys():
        time.sleep(1)
        print(separator)
        print("Ketik " + str(option) + " untuk " + options[option])

    time.sleep(1)
    print(separator)
    print("Ketik 4 untuk mengakhiri")

    while True:
        time.sleep(1)
        system_choice = random.randint(1, 3)  # Generate a random choice for the system
        print()
        print("(!) Sistem telah memilih! Giliran kamu!")

        choice = int(input("Masukkan pilihan kamu: "))
        while choice not in range(1, 5):
            print("(!) Masukkan pilihan yang valid!")
            choice = int(input("Masukkan pilihan kamu: "))

        if choice == 4:
            print(separator)
            print("=== Permainan Berakhir ===")
            print("Poin kamu: " + str(point_user) + "\t\tPoin sistem: " + str(point_system))
            if point_user > point_system:
                print("(!) Kamu MENANG! SELAMAT!!!")
            elif point_user == point_system:
                print("(!) Kamu dan sistem seimbang.")
            else:
                print("(!) Sistem MENANG! AI akan segera menguasai dunia!! Gawat!!!")
            print(separator)
            break

        time.sleep(1)
        print()
        print("(!) Pilihan sistem: " + options[system_choice] + ", pilihan kamu: " + options[choice] + ".")
        print()

        if choice == system_choice:
            print("(!) Hasil: DRAW!")
        else:
            if (choice == 1 and system_choice == 3) or (choice == 2 and system_choice == 1) or (choice == 3 and system_choice == 2):
                print("(!) Hasil: KAMU MENANG (+1 poin)!")
                point_user += 1
            else:
                print("(!) Hasil: SISTEM MENANG (+1 poin)!")
                point_system += 1
        
        time.sleep(1)
        print(separator)
        print("Poin kamu: " + str(point_user) + "\t\tPoin sistem: " + str(point_system))
        print(separator)
        
except Exception as err:
    # In this case, the except block just simply prints the error or Exception to the console.
    print("(!) Terjadi galat! " + str(err) + " " + str(type(err)))