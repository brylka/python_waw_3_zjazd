class Calc:
    @staticmethod
    def add(a,b):
        return float(a)+float(b)
    @staticmethod
    def mul(a,b):
        return float(a)*float(b)

print(Calc.add(0.1,0.2))
print(Calc.mul(4,2))