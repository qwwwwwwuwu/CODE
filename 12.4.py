
import math

class Hexagon:
    def __init__(self, l):
        
        self.length=l
    def calculate_per(self):
        # длина стороны равностороннего треугольника
        
        return 6 * self.length  # периметр шестиугольника

hexa = Hexagon(5)
print(hexa.calculate_per())  # вызов метода
