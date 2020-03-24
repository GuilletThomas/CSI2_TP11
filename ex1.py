class Cercle:
    def __init__(self, rayon):
        self.__rayon = rayon

    def GetRayon(self):
        return self.__rayon

    def __add__(self, other):
        return Cercle(self.__rayon+other.__rayon)

    def __lt__(self, other):
        return self.__rayon < other.__rayon

    def __gt__(self, other):
        return self.__rayon > other.__rayon

if __name__ == '__main__':
    c1 = Cercle(2)
    c2 = Cercle(3)
    c3 = c1 + c2
    c4 = c1 < c2
    c5 = c2 > c3
    print(c3)
    print(c4)
    print(c5)