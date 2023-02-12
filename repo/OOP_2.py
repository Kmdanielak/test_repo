class Data():
    def __init__(self, dzien, miesiac, rok):
        self.__dzień = dzien
        self.__miesiaca = miesiac
        self.__rok = rok


    def __str__(self):
        return f"Jest dzień {self.__dzień} i rok {self.__rok}"

moja_data = Data(12, 10, 2022)
print(moja_data)