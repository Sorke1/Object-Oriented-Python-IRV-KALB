import math

class Vector:
    '''The Vector class represents two values as a vector,
    allowing for many math calculations'''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, oOther):  # called for + operator
        return Vector(self.x + oOther.x, self.y + oOther.y)

    def __sub__(self, oOther):  # called for - operator
        return Vector(self.x - oOther.x, self.y - oOther.y)

    def __mul__(self, oOther):  # called for * operator
        # Special code to allow for multiplying by a vector or a scalar
        if isinstance(oOther, Vector):  # multiply two vectors
            return Vector(self.x * oOther.x, self.y * oOther.y)
        elif isinstance(oOther, (int, float)):  # multiply by a scalar
            return Vector(self.x * oOther, self.y * oOther)
        else:
            raise TypeError('Second value must be a vector or scalar')

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, oOther):  # called for == operator
        return (self.x == oOther.x) and (self.y == oOther.y)

    def __ne__(self, oOther):  # called for != operator
        return not (self == oOther)  # calls __eq__ method

    def __lt__(self, oOther):  # called for < operator
        return abs(self) < abs(oOther)

    def __gt__(self, oOther):  # called for > operator
        return abs(self) > abs(oOther)

    def __str__(self):
        return 'This vector has the value (' + str(self.x) + ', ' + str(self.y) + ')'


# Example usage
v1 = Vector(3, 4)
v2 = Vector(2, 2)
v3 = Vector(3, 4)

# These lines print Boolean or numeric values
print(v1 == v2)  # False
print(v1 == v3)  # True
print(v1 < v2)   # False
print(v1 > v2)   # True
print(abs(v1))   # 5.0
print(abs(v2))   # 2.8284271247461903

print()  # Print an empty line for readability

# These lines print Vectors (calls the __str__() method)
print('Vector 1:', v1)
print('Vector 2:', v2)
print('Vector 1 + Vector 2:', v1 + v2)
print('Vector 1 - Vector 2:', v1 - v2)
print('Vector 1 times Vector 2:', v1 * v2)
print('Vector 2 times 5:', v2 * 5)

# Output the custom string representation
oVector = Vector(3, 4)
print('My vector is', oVector)
