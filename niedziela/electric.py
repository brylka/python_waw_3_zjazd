from vehicle import Vehicle

class Electric(Vehicle):
    def __init__(self, mark, model, year, battery):
        super().__init__(mark, model, year)
        self.battery = battery

    def hong_2(self):
        print(f"{self.mark} inaczej trąbi!")
    def get_battery_info(self):
        print(f"Pojemność baterii {self.mark} wynosi {self.battery}Ah")


if __name__ == '__main__':
    electric = Electric("TESLA", "126", 1979, 100)
    electric.hong()
    electric.hong_2()
    electric.get_battery_info()
