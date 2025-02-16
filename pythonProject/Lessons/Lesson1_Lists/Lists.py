from random import random

from Main import print_delimeter

fruits = ["apple", "banana", "cherry"]
print(fruits)
print_delimeter()

empty_list = list()
print(empty_list)
print_delimeter()

print(len(fruits))
print_delimeter()

dif_values_list = ["str", 1, 2.3, True, 'a', [9, 8, 7, 6]]
print(dif_values_list)
print_delimeter()

list1 = [1, 2, 3]
list2 = [1, 3, 2]
list3 = [1, 2, 3]
print("List1 is equal list2? ", list1 == list2)
print("List2 is equal list3? ", list2 == list3)
print("List1 is equal list3? ", list1 == list3)
print_delimeter()

print(f"Boolean value from empty list is '{bool(list())}'")
print_delimeter()

print("Boolean value from empty list is {value}".format(value=bool([None])))
print_delimeter()

print(f"'Banana' word has in list {fruits}? {'banana' in fruits}")
print_delimeter()

print("'Donald' word has in list {fruits}? {value}".format(fruits=fruits, value='Donald' in fruits))
print_delimeter()

var1 = "element1"
var2 = "element2"
var3 = "element3"
list_of_vars = [var1, var2, var3]
print(list_of_vars)
print_delimeter()

word = "Hello"
list_from_word = list(word)
print(list_from_word)
print_delimeter()

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)
print_delimeter()

fruits.append("pineapple")
print(fruits)
print_delimeter()

print("Hello world".replace("world", "Python"))
print_delimeter()

fruit = fruits.pop()
print(fruit)
print(fruits)
print_delimeter()

fruits = ["apple", "banana", "cherry"]
fruits2 = ["grape", "orange"]
fruits.extend(fruits2)
print("Fruits list after extending: ", fruits)
print_delimeter()

print("List before reverse", fruits)
fruits.reverse()
print("List after reverse: ", fruits)
print_delimeter()

nums = []
for i in range(0, 8):
    value = round(random() * 10)
    if value not in nums:
        nums.append(value)
print("List before sorted: ", nums)
nums.sort()
print("List after sorted: ", nums)
nums.sort(reverse=True)
print("List after reverse sorted: ", nums)
print_delimeter()

source_string = "My name is Leo"
print(f"String '{source_string}' after split: {source_string.split()}")
print_delimeter()

srt_list = ["His", "name", "is", "Bob"]
print(f"List '{srt_list}' after join: {' '.join(srt_list)}")
print_delimeter()

import random

random.shuffle(nums)
print(f"Source list: {nums}")
print(f"List max value is {max(nums)}")
print(f"List min value is {min(nums)}")
print(f"List sum value is {sum(nums)}")
print_delimeter()

print(f"List is {fruits}")
source_element = fruits[2]
fruits[2] = "pineapple"
print(f"List after change second element '{source_element}' to '{fruits[2]}' is {fruits}")
print_delimeter()

print(f"List before elements rearrangement is {fruits}")
fruits[0], fruits[3] = fruits[3], fruits[0]
print(f"List after elements rearrangement is {fruits}")
print_delimeter()

print(f"List of nums is {nums}")
print(f"First three elements of list are {nums[:3]}")
print(f"Every second list element is {nums[1::2]}")
print_delimeter()

files_names = ["doc1.txt", "doc2.txt", "doc3.txt", "img.jpeg"]
for file_name in files_names:
    print(f"File name: {file_name}")
print_delimeter()

greeting = "Hello world!"
count_0 = 0
for char in greeting:
    count_0 += 1 if char == "o" else 0
    print(char)
print(f"Alpha 'o' frequency is {count_0}")
print_delimeter()

students = ["Alice", "Bob", "Carol", "Dave"]
for student in students:
    print(student)
    for char in student:
        print(char)
print_delimeter()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for number in numbers:
    if number % 2 == 0:
        print(number)
    if number == 10:
        print("Stop program!")
        break
print_delimeter()

range_obj = range(10)
print(range_obj)
print(list(range_obj))
print_delimeter()

# print(list(range(3, 7)))
# print_delimeter()
#
# print(list(range(5, 11, 2)))
# print_delimeter()
#
# print(list(range(8, 2, -1)))
# print_delimeter()
#
# numbers = [10, 11, 12, 13, 14, 15]
# for i in range(len(numbers)):
#     numbers[i] += 1
#     print(numbers[i])
# print_delimeter()
#
# indexes = []
# count = 0
# for i in range(len(greeting)):
#     if greeting[i] == "o":
#         count += 1
#         indexes.append(i)
# print(f"Alpha 'o' counter is {count}")
# print(f"Indexes are {indexes}")
# print_delimeter()
