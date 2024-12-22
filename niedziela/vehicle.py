class Vehicle:
    def __init__(self, mark, model, year, color=None):
        self.mark = mark
        self.model = model
        self.year = int(year)
        self.color = color
    def hong(self):
        print(f"Samochód {self.color} {self.mark} trąbi!")

if __name__ == '__main__':
    vehicle = Vehicle("BMW", "e30", "2000", "niebieski")
    vehicle.hong()
    #print("ala ma kota")