class Calc:
    def __init__(self):
        pass
    def add(self,a,b):
        return float(a)+float(b)
    def mul(self,a,b):
        return float(a)*float(b)

print(Calc().add(0.1,0.2))
print(Calc().add(1,2))