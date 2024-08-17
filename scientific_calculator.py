class calculator():
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
        
    def sum(self):
        result = self.number1 + self.number2
        return result

    def sub(self):
        result = self.number1 - self.number2
        return result

    def mult(self):
        result = self.number1 * self.number2
        return result

    def div(self):
        result = self.number1 / self.number2
        return result
    
    def checker_triangle(self, number3):
        if (self.number1 + self.number2) > number3:
            return 'Forma um triângulo! ', True
        else:
            return 'Não forma um triângulo ', False
    
    def checker_equilateral(self, number3):
        if self.number1 == self.number2 == number3:
            return 'Esse triângulo é equilátero! ', True
        else:
            return 'Esse trângulo não é equilátero! ', False
    
    def checker_scalene(self, number3):
        if self.number1 != self.number2 != number3:
            return 'Esse triângulo é escaleno! ', True
        else:
            return 'Esse triângulo não é escaleno! ', False
        
    def checker_isosceles(self, number3):
        if self.number1 == self.number2 or self.number2 == number3 or self.number1 == number3:
            return 'Esse triângulo é isósceles! ', True
        else:
            return 'Esse triângulo não é isósceles! ', False
    
obj = calculator(4, 3)

print(obj.sum())
print(obj.sub())
print(obj.mult())
print(obj.div())
print(obj.checker_triangle(6))
print(obj.checker_equilateral(3))
print(obj.checker_scalene(6))
print(obj.checker_isosceles(5))