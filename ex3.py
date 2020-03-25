class Rational:
    def __init__(self, numerateur, denominateur):
        self.__num = numerateur
        self.__den = denominateur

    def __add__(self, other):
        num = self.__num * other.__den + self.__den * other.__num
        den = self.__den * other.__den
        pgcd = self.__pgcd(num, den)
        return Rational(num/pgcd, den/pgcd)


    def __sub__(self, other):
        num = self.__num * other.__den - self.__den * other.__num
        den = self.__den * other.__den
        pgcd = self.__pgcd(num, den)
        return Rational(num / pgcd, den / pgcd)

    def __mul__(self, other):
        num = self.__num * other.__num
        den = self.__den * other.__den
        pgcd = self.__pgcd(num, den)
        return Rational(num / pgcd, den / pgcd)

    def __truediv__(self, other):
        num = self.__num * other.__den
        den = self.__den * other.__num
        pgcd = self.__pgcd(num, den)
        return Rational(num / pgcd, den / pgcd)

    def __pgcd(self, n, d):
        if d == 0:
            return False
        reste = n % d
        while reste != 0:
            n = d
            d = reste
            reste = n % d
        return d

    def getNum(self):
        return self.__num

    def getDen(self):
        return self.__den



if __name__ == '__main__':
    frac1 = Rational(5,2)
    frac2=Rational(10,2)
    frac3 = frac1 + frac2
    print(str(frac3.getNum())+"/"+str(frac3.getDen()))
    frac4 = frac1 * frac2
    print(str(frac4.getNum()) + "/" + str(frac4.getDen()))
