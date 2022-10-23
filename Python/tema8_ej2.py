import pickle

class Vehiculo:
    color = ""
    puertas = 0
    def __init__(self, color, puertas):
        self.color = color
        self.puertas = puertas

    def get_color(self):
        return self.color

    def get_puertas(self):
        return self.puertas

f = open("coche.bin", "rb")
c = pickle.load(f)
f.close()

print(type(c))
print(c.get_color())
print(c.puertas)