class Kurs:
    __dlugosc = 0
    __czas_startu = "10:50"
    __marka_pojazdu = "Renault"
    __kierowca = "Mariusz"
    __spalanie = 12
    def __init__(self,dlugosc: int, czas_startu: str,marka_pojazdu: str, kierowca: str, spalanie: int):
        self.dlugosc = dlugosc
        self.czas_startu = czas_startu
        self.marka_pojazdu = marka_pojazdu
        self.kierowca = kierowca
        self.spalanie = spalanie


    def __str__(self):
        return f'Długość trasy: {self.dlugosc}, czas startu: {self.czas_startu}, marka pojazdu {self.marka_pojazdu}, kierowca: {self.kierowca}, spalanie: {self.spalanie}, '

    @property
    def dlugosc(self):
        return self.__dlugosc

    @dlugosc.getter
    def dlugosc(self):
        return "Dlugosc: " + str(self.__dlugosc)

    @dlugosc.setter
    def dlugosc(self, value):
        self.__dlugosc = value

    @property
    def czas_startu(self):
        return self.__czas_startu

    @czas_startu.getter
    def czas_startu(self):
        return "Czas startu: " + str(self.__czas_startu)

    @czas_startu.setter
    def czas_startu(self, value):
        self.__czas_startu = value

    @property
    def marka_pojazdu(self):
        return self.__marka_pojazdu

    @marka_pojazdu.getter
    def marka_pojazdu(self):
        return "Marka pojazdu: " + str(self.__marka_pojazdu)

    @marka_pojazdu.setter
    def marka_pojazdu(self, value):
        self.__marka_pojazdu = value

    @property
    def kierowca(self):
        return self.__kierowca

    @kierowca.getter
    def kierowca(self):
        return "Kierowca: " + str(self.__kierowca)

    @kierowca.setter
    def kierowca(self, value):
        self.__kierowca = value

    @property
    def spalanie(self):
        return self.__spalanie

    @spalanie.getter
    def spalanie(self):
        return "Spalanie: " + str(self.__spalanie)

    @spalanie.setter
    def spalanie(self, value):
        self.__spalanie= value

    def Suma_kilometrow(self):
        return float(int(round(self.__dlugosc, 2)))

    def Marka(self):
        return f'Marka pojazdu: {self.__marka_pojazdu}'

class Pojazd(Kurs):
    def __init__(self,dlugosc, czas_startu ,marka_pojazdu, kierowca , spalanie , pojazd: str ):
        super().__init__(dlugosc, czas_startu ,marka_pojazdu, kierowca, spalanie)
        self.pojazd = pojazd
    def __str__(self):
        return f'Długość trasy: {self.dlugosc}, czas startu: {self.czas_startu}, marka pojazdu {self.marka_pojazdu}, kierowca: {self.kierowca}, spalanie: {self.spalanie},pojazd:{self.pojazd} '

class FirmaTransportowa(Kurs):
    def __init__(self,dlugosc, czas_startu ,marka_pojazdu, kierowca , spalanie, nazwa_firmy: str ):
        super().__init__(dlugosc, czas_startu, marka_pojazdu, kierowca, spalanie)
        self.nazwa_firmy = nazwa_firmy

    def __str__(self):
        return f'Długość trasy: {self.dlugosc}, czas startu: {self.czas_startu}, marka pojazdu {self.marka_pojazdu}, kierowca: {self.kierowca}, spalanie: {self.spalanie},nazwa firmy: {self.nazwa_firmy} '
class Odcinek(Kurs):
    def __init__(self,dlugosc, czas_startu ,marka_pojazdu, kierowca , spalanie, nazwa_odcinka:str ):
        super().__init__(dlugosc, czas_startu, marka_pojazdu, kierowca, spalanie)
        self.nazwa_odcinka = nazwa_odcinka
    def __str__(self):
        return f'Długość trasy: {self.dlugosc}, czas startu: {self.czas_startu}, marka pojazdu {self.marka_pojazdu}, kierowca: {self.kierowca}, spalanie: {self.spalanie},nazwa odcinka {self.nazwa_odcinka}'

class FirmaSpozywcza(Kurs):
    def __init__(self, dlugosc, czas_startu ,marka_pojazdu, kierowca , spalanie, nazwa_firmy:str):
        super().__init__(dlugosc, czas_startu,marka_pojazdu , kierowca, spalanie)
        self.nazwa_firmy = nazwa_firmy



if __name__ == '__main__':
    kurs1 = Kurs(55, "10:30", "Renault", "Mariusz", 12)
    print(kurs1.dlugosc)
    print(kurs1.Suma_kilometrow())
    print(kurs1.Marka())