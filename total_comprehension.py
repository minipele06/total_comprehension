# total_comprehension.py

def great_three(i):
    return i > 3

def great_eight(i):
    return i > 8

my_numbers = [1, 2, 3, 4, 5, 6, 7]
print("--------------")
print("ORIGINAL LIST:", my_numbers)

print("--------------")
print("TOTAL COMPREHENSION...")

# TODO: write python code here

my_list = []
my_list2 = []

for i in my_numbers:
    my_list.append(i*100)

great3_list = list(filter(great_three,my_numbers))
great8_list = list(filter(great_eight,my_numbers))

for i in great3_list:
    my_list2.append(i*100)

print("--------------")
print("MAPPED LIST:", my_list)

print("--------------")
print("FILTERED LIST W/ MATCHES:", great3_list)

print("--------------")
print("FILTERED LIST W/O MATCHES:", great8_list)
print("--------------")
print("MAPPED AND FILTERED LIST:", my_list2)
