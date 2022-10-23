print("Ingrese su peso en kilos:")
peso = int(input())
print("Ingrese su estatura en metros:")
estatura = float(input())
estatura *= estatura
print(estatura)
imc = round((peso / estatura), 2)
print("Su índice de masa corporal es", imc)
