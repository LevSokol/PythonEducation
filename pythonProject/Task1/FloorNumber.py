import math

APARTMENTS = 20


class FloorNumber:

    @staticmethod
    def calculate_entrance(appart_number):
        return math.ceil(appart_number / APARTMENTS)

    @staticmethod
    def calculate_floor(appart_number):
        return math.ceil((appart_number - 1) % APARTMENTS // 4 + 1)

# for _ in iter(int, 1):
#     pass
#     number = int(input("Введите номер квартиры: "))
#     entrance = math.ceil(number / APARTMENTS)
#     print("Номер подъезда: ", calculate_entrance(number))
#     print("Номер этажа: ", calculate_floor(number), "\n")
