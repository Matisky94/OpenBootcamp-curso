from functools import reduce

def main():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    res = list(filter(impares, numeros))
    print(res)
    res2 = reduce(suma, res)
    print(res2)

def impares(x):
    if x % 2 == 0:
        return True
    return False

def suma(a, b):
    return a + b

if __name__ == "__main__":
    main()