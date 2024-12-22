class Vehicle:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = int(year)
    def hong(self):
        print(f"Samochód {self.mark} trąbi!")

if __name__ == '__main__':
    vehicle = Vehicle("BMW", "e30", "2000")
    vehicle.hong()
    print("ala ma kota")