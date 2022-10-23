import sqlite3

def main():
    conn = sqlite3.connect("miaplicacion.db")
    cursor = conn.cursor()

    rows = cursor.execute("SELECT * FROM alumnos")
    for row in rows:
        print(row)

    cursor.close()
    conn.close()

def main2():
    id = 0
    for i in range(1, 9):
        nombre = input(f"Nombre del alumno {i}: ")
        apellido = input(f"Apellido del alumno {i}: ")
        id += 1
        agregar_alumnos(id, nombre, apellido)

def agregar_alumnos(id, nombre, apellido):
    conn = sqlite3.connect("miaplicacion.db")
    cursor = conn.cursor()

    query = '''INSERT INTO alumnos(id, nombre, apellido) VALUES(?, ?, ?)'''
    rows = cursor.execute(query, (id, nombre, apellido))

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()