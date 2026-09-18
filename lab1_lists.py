# Lab 1 - Lists in Python


# Task 1: Creating Lists

my_list1 = [5, 12, 13, 14]  # the list contains all integer values
print(my_list1)

my_list2 = ['red', 'green', 'black', 'white']  # the list contains all string values
print(my_list2)

my_list3 = ['blue', 12, 112.12]  # the list contains a string, an integer and a float value
print(my_list3)

my_list = []  # empty list
print(my_list)


# ------------------------------------------------------
# Task 2: List Indices

color_list = ["RED", "Purple", "Green", "Grey"]  # the list has four elements, indices start at 0 and end at 3

print(color_list[0])  # Return the first element

print(color_list[0], color_list[3])  # Print first and last elements

print(color_list[-1])  # Return the last element

print(color_list[4])  # Creates an error as the index is out of range


# ------------------------------------------------------
# Task 3: List Slice

color_list = ["RED", "Blue", "Green", "Black"]  # the list has four elements, indices start at 0 and end at 3

print(color_list[0:2])   # cut first two items
print(color_list[1:2])   # cut second item
print(color_list[1:-2])  # cut second item
print(color_list[:3])    # cut first three items
print(color_list[:])     # creates a copy of the original list



# Bonus: Conditional Statement

a = 4
b = 10

if b > a:
    print("b is greater than a")
