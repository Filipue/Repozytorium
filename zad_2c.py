#Lab2_zad2c
def Zad_2c(liczby):
    for x in range(len(liczby)):
        if liczby[x] % 2 == 0:
            print(f"liczby parzyste {liczby[x]}")
if __name__=='__main__':
    liczby = [1,2,3,4,5,6,7,8,9,10]
    Zad_2c(liczby)