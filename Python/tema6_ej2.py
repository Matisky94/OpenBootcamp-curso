class Alumno():
    nombre = None
    nota = 0
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

a = Alumno("Juan", 9)
if a.nota >= 7:
    print(f"La nota de {a.nombre} es {a.nota}, ha aprovado")
else:
    print(f"La nota de {a.nombre} es {a.nota}, ha desaprovado")