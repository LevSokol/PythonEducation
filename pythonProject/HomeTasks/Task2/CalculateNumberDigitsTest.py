import unittest

from HomeTasks.Task2.CalculateNumberDigits import CalculateNumberDigits


class MyTestCase(unittest.TestCase):
    def test_number_digits_length(self):
        number = CalculateNumberDigits(5)
        self.assertEqual(number.calculate(), 1)

    def test_number_digits_length2(self):
        number = CalculateNumberDigits(123456789)
        self.assertEqual(number.calculate(), 9)

    def test_number_digits_length3(self):
        number = CalculateNumberDigits(1234567890987654321)
        self.assertEqual(number.calculate(), 19)


if __name__ == '__main__':
    unittest.main()
