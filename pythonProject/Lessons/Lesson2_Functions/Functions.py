import random

from Main import print_delimeter

number1 = [random.randint(1, 9) for i in range(10)]
number2 = [random.randint(1, 9) for k in range(17)]


def calc_average(numbers):
    result = sum(numbers) / len(numbers)
    print(f"Average of {numbers} is {'{:.2f}'.format(result)}")
    print_delimeter()
    return result


calc_average(number1)
calc_average(number2)

def count_vowels(string):
    count = 0
    VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for letter in string:
        count += 1 if letter in VOWELS else 0
    print(f"Number of vowels '{string}': {count}")
    print_delimeter()

count_vowels("Hello world and Albhus Dumbledor!")
count_vowels("Python is a very powerful programming language!")