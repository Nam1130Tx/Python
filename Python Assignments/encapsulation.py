#Python:     3.9.0
#Author:     Nicholas Mireles
#Assignment: Encapsulation

class Car:
    def __init__(self, model, year=1886):
        self._model = model
        self.__year = year

    def show(self):
        print(self._model)
        print(self.__year)

    def getYear(self):
        print(self.__year)

    def setYear(self, year):
        self.__year = year

if __name__ == "__main__":
    VW = Car('GTI',"")
    VW.show()
    VW.setYear(2017)
    VW.getYear()
