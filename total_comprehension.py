# total_comprehension.py

my_numbers = [1, 2, 3, 4, 5, 6, 7]
my_list = [n * 100 for n in my_numbers]
my_list2 = [n for n in my_numbers if n > 3]
my_list3 = [n for n in my_numbers if n > 8]
my_list4 = [n * 100 for n in my_numbers if n > 3]

print("--------------")
print("ORIGINAL LIST:", my_numbers)

print("--------------")
print("TOTAL COMPREHENSION...")

print("--------------")
print("MAPPED LIST:", my_list)

print("--------------")
print("FILTERED LIST W/ MATCHES:", my_list2)

print("--------------")
print("FILTERED LIST W/O MATCHES:", my_list3)

print("--------------")
print("MAPPED AND FILTERED LIST:", my_list4)
