import math

class Fraction:
    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int):
            raise TypeError('Numerator must be an integer')
        if not isinstance(denominator, int):
            raise TypeError('Denominator must be an integer')

        self.numerator = numerator
        self.denominator = denominator

        # Find the greatest common divisor to simplify the fraction
        gcd = math.gcd(self.numerator, self.denominator)
        if gcd > 1:
            self.numerator //= gcd
            self.denominator //= gcd

        self.value = self.numerator / self.denominator

        # Normalize the sign of the numerator and denominator
        self.numerator = int(math.copysign(1.0, self.value)) * abs(self.numerator)
        self.denominator = abs(self.denominator)

    def getValue(self):
        return self.value

    def __str__(self):
        return f'Fraction: {self.numerator}/{self.denominator}\nValue: {self.value}\n'

    def __add__(self, oOtherFraction):
        if not isinstance(oOtherFraction, Fraction):
            raise TypeError('Second value in attempt to add is not a Fraction')

        # Find the least common multiple
        lcm = (self.denominator * oOtherFraction.denominator) // math.gcd(self.denominator, oOtherFraction.denominator)

        # Calculate equivalent numerators
        new_numerator = (lcm // self.denominator) * self.numerator + (lcm // oOtherFraction.denominator) * oOtherFraction.numerator

        return Fraction(new_numerator, lcm)

    def __eq__(self, oOtherFraction):
        if not isinstance(oOtherFraction, Fraction):
            return False

        return self.numerator == oOtherFraction.numerator and self.denominator == oOtherFraction.denominator

# Test code
oFraction1 = Fraction(1, 3)
oFraction2 = Fraction(2, 5)
print('Fraction1\n', oFraction1)
print('Fraction2\n', oFraction2)
oSumFraction = oFraction1 + oFraction2
print('Sum is\n', oSumFraction)
print('Are fractions 1 and 2 equal?', (oFraction1 == oFraction2))

oFraction3 = Fraction(-20, 80)
oFraction4 = Fraction(4, -16)
print('Fraction3\n', oFraction3)
print('Fraction4\n', oFraction4)
print('Are fractions 3 and 4 equal?', (oFraction3 == oFraction4))

oFraction5 = Fraction(5, 2)
oFraction6 = Fraction(500, 200)
print('Sum of 5/2 and 500/2\n', oFraction5 + oFraction6)
