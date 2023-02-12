class Audi:
    def __init__(self, kolor, info_o_kondycji, vin):
        self.kolor = kolor   #poprawne nazewnictwo
        self.przebieg = 10
        self.kondycja = info_o_kondycji   #słabe
        self.__vin = vin

    def aktualizuj_przebieg(self, o_ile):
        self.przebieg += o_ile

    def pokaz_vin(self):
        print(self.__vin)

    def zmien_vin(self, nowy_vin):
        print('sprawdzam, czy nowy vin poprawny')
        print('sprawdzam, czy nowy vin wolny')
        print('sprawdzam, czy jest pozwolenie')
        self.__vin = nowy_vin

moje_auto = Audi('czerwony', 'dobra', 12345)
print(moje_auto.kolor)
moje_auto.kolor = 'niebieski'
print(moje_auto.kolor)
moje_auto.aktualizuj_przebieg(-50)
print(moje_auto.przebieg)
#print(moje_auto.__vin)  # nie zadzialamoje_auto.pokaz_vin()
moje_auto.zmien_vin(5675676)
moje_auto.pokaz_vin()