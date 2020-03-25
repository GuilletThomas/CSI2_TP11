class Duree:
    def __init__(self, heure, minute, seconde):
        self.__h = heure
        self.__m = minute
        self.__s = seconde

    def __str__(self):
        return str(self.__h)+"h"+str(self.__m)+"m"+str(self.__s)+"s"

    def __add__(self, other):
        return Duree(self.__h+other.__h, self.__m+other.__m, self.__s+other.__s)

    def afficher(self):
        if self.__m >= 60:
            d = self.__m // 60
            self.__h += d
            self.__m -= d * 60
        if self.__s >= 60:
            k = self.__s // 60
            self.__m += k
            self.__s -= k * 60
        print(str(self.__h) + "h" + str(self.__m) + "min" + str(self.__s) + "s")

if __name__ == '__main__':
    h1 = Duree(13,26,50)
    h2 = Duree(1,35,14)
    h3 = h1 + h2
    h3.afficher()


