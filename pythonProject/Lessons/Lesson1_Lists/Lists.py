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