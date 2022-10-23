def main():
    paises = input("Ingrese una lista de países separados por coma:")
    paises = paises.split(",")
    paises = list(set(paises))
    print(sorted(paises))

if __name__ == "__main__":
    main()