class Complex:
    def __init__(self, realPart, imPart):
        self.__realPart = realPart
        self.__imPart = imPart

    def __add__(self, other):
        return Complex(self.__realPart + other.__realPart, self.__imPart + other.__imPart)

    def __sub__(self, other):
        return Complex(self.__realPart - other.__realPart, self.__imPart - other.__imPart)

    def __mul__(self, other):
        return Complex(self.__realPart * other.__realPart - self.__imPart * other.__imPart, self.__realPart * other.__imPart+ self.__imPart * other.__realPart)

    def __truediv__(self, other):
        return Complex(self.__realPart / other.__realPart, self.__imPart / other.__imPart)

    def __abs__(self):
        return [(self.__realPart)**2 + (self.__imPart)**2]**(1/2)

    def __eq__(self, other):
        return self.__realPart == other.__realPart and self.__imPart == other.__imPart

    def __ne__(self, other):
        return self.__realPart != other.__realPart or self.__imPart != other.__imPart

    def getRe(self):
        return self.__realPart
    def getIm(self):
        return self.__imPart

if __name__ == '__main__':
    c1 = Complex(2,3)
    c2 = Complex(4,5)
    c3 = c1 +c2
    print(str(c3.getRe())+"+"+str(c3.getIm())+"i")
    c4 = c1 - c2
    print(str(c4.getRe())+"+"+str(c4.getIm())+"i")
    c5 = c1 * c2
    print(str(c5.getRe())+"+"+str(c5.getIm())+"i")
    c6 = c1/c2
    print(str(c6.getRe())+"+"+str(c6.getIm())+"i")
    c7 = abs(c1)
    print(str(c4.getRe())+"+"+str(c4.getIm())+"i")
    c1 == c2
    c1 != c2


