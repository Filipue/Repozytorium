#Lab2_zad2bi
def zad_2bi(liczby):
    pomnozone = []
    for x in liczby:
        pomnozone.append(x*2)
    return pomnozone
if __name__=='__main__':
    liczby = [1, 2, 3, 4, 5]
    print(zad_2bi(liczby))
