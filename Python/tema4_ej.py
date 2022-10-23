lista = [1]
for numero in range(2, 101):
    lista.append(numero)

listaInversa = sorted(lista, reverse=True)
for numero in lista:
    print(listaInversa[numero-1])