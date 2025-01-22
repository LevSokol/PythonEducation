import unittest

from HomeTasks.Task1.FloorNumber import *


class FloorNumberTestCase(unittest.TestCase):
    def test_entrance_number(self):
        self.assertEqual(FloorNumber.calculate_entrance(1), 1)

    def test_entrance_number2(self):
        self.assertEqual(FloorNumber.calculate_entrance(20), 1)

    def test_entrance_number3(self):
        self.assertEqual(FloorNumber.calculate_entrance(21), 2)

    def test_floor_number(self):
        self.assertEqual(FloorNumber.calculate_floor(1), 1)

    def test_floor_number2(self):
        self.assertEqual(FloorNumber.calculate_floor(8), 2)

    def test_floor_number3(self):
        self.assertEqual(FloorNumber.calculate_floor(21), 1)


if __name__ == '__main__':
    unittest.main()
