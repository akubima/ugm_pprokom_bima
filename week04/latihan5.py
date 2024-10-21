# Authored by @akubima
# on 2-9-2024

# Fisrt we declare a variable that hold dictionary for storing student's name and grade.
grades = {}

# Then we create some banner, just for fun.
separator = "-" * 40
print(separator.center(50))
print("SISTEM EVALUASI SISWA".center(50))
print(separator.center(50))
print()


# Then we put our code in the try except block so that if any error occured
# it will be handled safely in except block.
try:
    # Then we chcek if the length of the grades less than 5 means the inputed student data 
    # is not yet equal to 5, so we ask for more data.
    while (len(grades) < 5):
        name = input("Masukkan nama siswa: ")
        grade = int(input("Masukkan nilai " + name + ": "))
        # Update grades in everey input to store the student name and grade.
        grades.update({name: grade})
        # Print the existing data.
        print(separator)
        print(grades)
        print(separator)
    
    # After there are 5 data in the grades dictionary, we evaluate which student is going to
    # pass and which is going to fail.

    for grade in grades.keys():
        if(grades[grade]) >= 70:
            print(separator)
            print('- ' + str(grade) + ' - DINYATAKAN LULUS. SAMPAIKAN: "SELAMAT Anda dinyatakan lulus!"')
            print(separator)
        else:
            print(separator)
            print('- ' + str(grade) + ' - DINYATAKAN TIDAK LULUS. SAMPAIKAN: "JANGAN PUTUS ASA DAN TETAP SEMANAGAT!"')
            print(separator)
except Exception as err:
    # In this case the except block just simply print the error or Exception to the console.
    print("(!) Terjadi galat! " + str(err) + str(type(err)))
