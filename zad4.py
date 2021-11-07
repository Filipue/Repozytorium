#Lab3_zad4
def zad_4(arg1: int, arg2: int, arg3: int) -> bool:
    if arg1+arg2 >= arg3:
        return True
    else:
        return False
if __name__ == '__main__':
    print(zad_4(0,3,4))