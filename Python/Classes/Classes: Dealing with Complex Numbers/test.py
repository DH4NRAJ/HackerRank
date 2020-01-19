import math
from math import sqrt
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        if self.imaginary + no.imaginary<0:
            return("%.2f-%.2fi"%(self.real+no.real,abs(self.imaginary + no.imaginary)))
        else:
            return("%.2f+%.2fi"%(self.real+no.real,self.imaginary + no.imaginary))
    def __sub__(self, no):
        if self.imaginary - no.imaginary <0:
            return("%.2f-%.2fi"%(self.real-no.real,abs(self.imaginary - no.imaginary)))
        else:
            return("%.2f+%.2fi"%(self.real-no.real,self.imaginary - no.imaginary))
        
    def __mul__(self, no):
        if self.real*no.imaginary+self.imaginary*no.real <0:
            return("%.2f-%.2fi"%(self.real*no.real- self.imaginary*no.imaginary,abs(self.real*no.imaginary+self.imaginary*no.real)))
        else:
            return("%.2f+%.2fi"%(self.real*no.real- self.imaginary*no.imaginary,abs(self.real*no.imaginary+self.imaginary*no.real)))
    def __truediv__(self, no):
        diiv = no.real*no.real+no.imaginary*no.imaginary
        if self.imaginary*no.real - self.real*no.imaginary<0:
            return("%.2f-%.2fi"%((self.real*no.real + self.imaginary*no.imaginary)/diiv,abs((self.imaginary*no.real - self.real*no.imaginary))/diiv))
        else:
            return("%.2f+%.2fi"%((self.real*no.real + self.imaginary*no.imaginary)/diiv,abs((self.imaginary*no.real - self.real*no.imaginary))/diiv))


    def mod(self):
        return("%.2f+0.00i"%((sqrt(self.real*self.real + self.imaginary*self.imaginary))))
        

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
