#Lab2_zad2bii
def zad_2bii(liczby):
    pomnozone = [x*2 for x in liczby]
    return pomnozone
if __name__=='__main__':
    liczby = [1, 2, 3, 4, 5]
    print(zad_2bii(liczby))