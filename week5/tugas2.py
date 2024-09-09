# Authored by @akubima on 08-09-2024

# Fisrt we asked the user how much balance did he/she have.
balance = float(input("Saldo kamu (gunakan titik [.] untuk desimal contoh: 1.75])-> "))

# Then we use the while loop with always True condition, this loop will continue to be executed
# until eternity unless a break is performed. This loop is used to ask the user for
# the amount of expense.
while (True):
    print("Masukkan -1 untuk keluar.")
    expense = float(input("Pengeluaran kamu (gunakan titik [.] untuk desimal contoh: 1.75])-> "))

    # If the user inputed -1 it mean the user wanted to exit the program so we break the loop.
    if(expense == -1):
        print("Sisa saldo kamu:  {:.2f}". format(balance))
        break

    # else we deduct the balance. But first we need to check if the expense is larger than the balance
    # to determine if the user still has the sufficient balance to perform a transaction. 
    if (expense > balance):
        print("Saldo Tidak Cukup!\nSaldo kamu tersisa: {:.2f}". format(balance))
        break

    balance -= expense