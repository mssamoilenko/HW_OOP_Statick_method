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

#task2
class TemperatureConverter:
    count = 0
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def count_conversion():
        TemperatureConverter.count += 1
        return TemperatureConverter.count
celsius = 25
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is {fahrenheit}°F")
print("Total temperature conversions:", TemperatureConverter.count_conversion())

fahrenheit = 77
celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit}°F is {celsius}°C")
print("Total temperature conversions:", TemperatureConverter.count_conversion())