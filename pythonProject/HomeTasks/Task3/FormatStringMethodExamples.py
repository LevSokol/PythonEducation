from Main import print_delimeter

# Именованные параметры
text = "Hello, {first_name}".format(first_name="Jack")
print(text)
print_delimeter()

person_info = "Name is {name}, age is {age}".format(name="Donald", age=54)
print(person_info)
print_delimeter()

# Параметры по позиции
person_info_new = "Name is {0}, age is {1}".format("Bill", 40)
print(person_info_new)
print_delimeter()

print("{0}{1}{2}".format("Hello", ", ", "World"))
print_delimeter()

# Подстановки
print("Hello, {:s}".format("Tom"))
print_delimeter()

print("В строке '", person_info, "' больше {:d} символов.".format(10), sep="")
print_delimeter()

number = 5000000
source = f"{number:,d} символов"
print(source)
print_delimeter()

number = 23.46184512498785156
print("{:.2f}".format(number))
print("{:.7f}".format(number))
print("{:.12f}".format(number))
print_delimeter()

print("{:.2f}".format(number))
print("{:6.2f}".format(number))
print("{:7.2f}".format(number))
print("{:8.2f}".format(number))
print_delimeter()

name = "Ann"
age = 35
print("Person name is '%s' and age is %d" % (name, age))
print_delimeter()

print("Formatting numbers are: %.2f and %e" % (number, number))
print_delimeter()