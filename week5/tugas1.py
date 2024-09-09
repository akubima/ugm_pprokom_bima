# Authored by @akubima on 08-09-2024

# First declare a variable with list to store the designated values.
num_list = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]

# Then we define a new list used to hold copied value of the num_list.
new_num_list = num_list.copy()

#  We use the reverse method to reverse the order of the num_list objects.
num_list.reverse();

# Then we use for loop to add the reversed value of the num_list to the new_num_list.
for o in num_list:
    new_num_list.append(o)

# Last we print the value of new_num_list.
print(new_num_list)