import random


def print_delimeter():
    print("**************************")


print("first")
print("second")
print_delimeter()

# name = input("Enter name: ")
# print(name)
# print_delimeter()

name = "Alice"
age = 25
print(name, "is", age, "years old")
print_delimeter()

name2, age2 = "Bob", 64
print(name2, "is", age2, "years old")
print_delimeter()

fullName = name + " Ivanova"
print(fullName)
print_delimeter()

x = 3
y = 4
x, y = y, x
print("x = ", x, "; y = ", y)
print_delimeter()

var = 1
print(type(var))
print_delimeter()

my_int = 10
my_float = 3.14
summary = my_int + my_float
print("Sum = ", summary)
print_delimeter()

is_student = True
print("Is the child a student? ", is_student)
print_delimeter()

is_graduated = False
print("Is the student a graduate? ", is_graduated)
print_delimeter()

x = 10
y = 5
are_variables_equals = x == y
are_variables_not_equals = x != y
print("x == y ? ", are_variables_equals)
print("x != y ? ", are_variables_not_equals)
print_delimeter()

print("x is between [8; 11]: ", 8 < x < 11)
print("x is not between [12; 13]: ", not 12 < x < 13)
print_delimeter()

print("Is 5 not None? ", bool(5))  # проверка на None
print_delimeter()

a = None
print("Is object Null? ", not bool(a))
print_delimeter()

if random.random() > random.random():
    print("Condition is True")
else:
    print("Condition is False")
print_delimeter()

x = 10
y = 20
if x > 0 and y > 0:
    print("x > 0 and y > 0")
elif x > 0 > y:
    print("x > 0 and y < 0")
else:
    print("Another condition")
print_delimeter()

message = "Hello World"
if message:
    print("message '", message, "' is not empty!", sep='')
print_delimeter()

my_string = """Ссылки, используемые в курсе: 
1. Онлайн-интерпретатор: https://www.online-python.com/
2. Установка Python на компьютер: https://www.python.org/downloads/
3. PyCharm Community Edition: https://www.jetbrains.com/pycharm/dow...
4. Репозиторий с кодом курса: https://github.com/jjoskey/python_beg...
5. Документация к открытому API Binance: https://binance-docs.github.io/apidoc...
6. Visual Crossing, бесплатный API погоды: https://www.visualcrossing.com/weathe...
7. JSON Formatter: https://jsonformatter.curiousconcept....
8. Официальный бот от Telegram для регистрации других ботов: https://t.me/BotFather"""
print(my_string)
print_delimeter()

# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# print(first_name + " " + last_name)
# print_delimeter()

string = "Hello World"
print("Length of string: ", len(string))
print_delimeter()

int_var = 100
str_var = str(int_var)
print("Variable type after convert is ", type(int_var))
print_delimeter()

str_var = "120"
int_var = int(str_var)
print("Variable type after convert is ", type(int_var))
print_delimeter()

# input = input("Enter a number: ")
# print("Input default type is ", type(input))
# print_delimeter()

