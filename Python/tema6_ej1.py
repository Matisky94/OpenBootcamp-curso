class Vehiculo:
    color = "Verde"
    ruedas = 4
    puertas = 4

class Coche(Vehiculo):
    velocidad = 40
    cilindrada = 150

c = Coche
print(c.velocidad)
print(c.cilindrada)
print(c.color)
print(c.ruedas)
print(c.puertas)