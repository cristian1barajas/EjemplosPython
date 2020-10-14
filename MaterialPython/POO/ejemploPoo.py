from numpy import hypot, sqrt

class Figura(object):
    def __init__(self, _dim1, _dim2):
        self.dim1 = _dim1
        self.dim2 = _dim2

class Rectangulo(Figura):
    def __init__(self, _dim1, _dim2):
        super(Rectangulo, self).__init__(_dim1, _dim2)
    def area(self):
        if self.dim1 != self.dim2:
            print("El area del rectangulo es: ")
        else:
            print("El area del cuadrado es: ")
        return(self.dim1 * self.dim2)
    def perimetro(self):
        print("El perimetro del rectangulo es: ")
        return(2 * self.dim1 + 2 * self.dim2)

class Triangulo(Figura):
    def __init__(self, _dim1, _dim2, _base, _altura):
        super(Triangulo, self).__init__(_dim1, _dim2)
        self.base = _base
        self.altura = _altura
    def area(self):
        print("El area del triangulo es: ")
        return ((self.base * self.altura) / 2)
    def perimetro(self):
        print("El perimetro del triangulo es: ")
        return (self.dim1 + self.dim2 + self.base)
    def hipotenusa(self):
        print("La hipotenusa es: ")
        return (hypot(self.base, self.altura))

def main():
    F = Figura(5, 5)
    R = Rectangulo(6, 5)
    T = Triangulo(7, 6, 5, 4)
    print(R.area())
    print(R.perimetro())
    print(T.area())
    print(T.perimetro())

if __name__ == '__main__':
    main()
