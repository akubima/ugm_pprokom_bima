# Authored by @akubima on 08-09-2024
# To count the average value from a user inputed data.

# First we declare an empty list that whill hold the inputed value.
numbers = []

# Then we use while loop with always True condition to ask the user for an input.
while True:
    print("-"*50)
    print("Masukkan nilai negatif sembarang untuk menghitung rata-rata.")
    number = float(input("Masukkan nilai (desimal gunakan titik)-> "))
    
    # If the user inputed any negative value this loop should be ended and the average val. will be counted.
    if(number < 0):
        break

    # For every input we append the value to the numbers list.
    numbers.append(number)

    # Display the current values.
    print(numbers)

# We calculate the average value.

# Declate a variable called total to hold the sum of every objets in number.
total = sum(numbers);

# Print the calculated avg. value.
print("-"*50)
print("Jumlah nilai total: {:.2f}".format(sum(numbers)))
print("Jumlah data: %i" % (len(numbers)))
print("Rata-rata: {:.2f}".format(total / len(numbers)))
