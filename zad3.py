#Lab3_zad3
def zad_3(arg1: int) -> bool:
    if arg1 % 2 == 0:
        return True
    else:
        return False
if __name__ == '__main__':
    x = 7
    wynik = zad_3(x)
    if wynik == True:
        print('Liczba parzysta')
    else:
        print('Liczba nieparzysta')
