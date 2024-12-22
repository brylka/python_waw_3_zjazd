from vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, mark, model, year, capacity):
        super().__init__(mark, model, year)
        self.capacity = capacity

    def load(self):
        print(f"Samochód {self.mark} został załadowany!")

if __name__ == '__main__':
    truck = Truck("Star", "25", 1970, 10)
    truck.hong()
    truck.load()