class Vehicle:
    def __init__(self, mark, model, year, color=None):
        self.mark = mark
        self.model = model
        self.year = int(year)
        self.color = color
    def __str__(self):
        return f"Jestem obiekt z klasy Vehicle - marka {self.mark}"
    def hong(self):
        print(f"Samochód {self.color} {self.mark} trąbi!")

if __name__ == '__main__':
    vehicle = Vehicle("BMW", "e30", "2000", "niebieski")
    vehicle.hong()
    print(vehicle)
    #print("ala ma kota")