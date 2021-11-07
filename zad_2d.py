#Lab2_zad2d
def zad_2d(liczby):
    for count, x in enumerate(liczby,0):
        if count % 2 >0:
            print ('Iteracja nr.', count, ' Wartosc:' ,x)
if __name__ == '__main__':
    liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(zad_2d(liczby))