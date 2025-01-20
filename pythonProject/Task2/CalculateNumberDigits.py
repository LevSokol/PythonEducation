class CalculateNumberDigits:
    def __init__(self, number):
        self.number = number

    def calculate(self):
        return len(str(self.number))
