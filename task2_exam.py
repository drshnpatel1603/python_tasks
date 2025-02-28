# Task 2: Find and Count Duplicates in a List and print it on screen.

numbers = [4, 5, 6, 4, 7, 8, 5, 9, 4, 7, 6, 10]

# set used to duplicate element remove than convert list
diifernt_number = list(set(numbers))

 # count the number how many time repeate
for num in diifernt_number:
    if numbers.count(num) > 1:
        print(f"{num} appears  {numbers.count(num)} Times")