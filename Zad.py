def zad_6(lista1: list, lista2: list) -> list:
    return list(x ** 3 for x in set(lista1+lista2))

if __name__ == '__main__':
    lista = [2, 4, 6, 8, 10]
    lista2 = [6,2,3,4,5,6,7,11]
    zad_6(lista1, lista2)
    print(zad_6(lista1,lista2))