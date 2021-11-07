#Lab3_zad6

def zad_6(arg1: list, arg2: list) -> list:
    return list(x ** 3 for x in set(arg1+arg2))
if __name__ == '__main__':
    arg1 = [3, 5, 7, 9, 10]
    arg2 = [1,23,4,5,11]
    print(zad_6(arg1,arg2))