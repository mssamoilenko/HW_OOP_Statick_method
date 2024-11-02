#task1
class Fraction:
    count = 0
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.count += 1

    @staticmethod
    def count_fraction():
        return Fraction.count

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)
print("Total number of Fraction objects created:", Fraction.count_fraction())