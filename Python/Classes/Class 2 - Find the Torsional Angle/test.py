import math
class Points(object):
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z

    def __sub__(self, no):
        cx= self.x-no.x
        cy= self.y-no.y
        cz= self.z-no.z
        return Points(cx,cy,cz)

    def dot(self, no):
        return self.x*no.x+self.y*no.y+self.z*no.z

    def cross(self, no):
       cx = self.y*no.z - self.z*no.y
       cy = self.z*no.x -self.x*no.z
       cz = self.x*no.y -self.y*no.x
       return Points(cx,cy,cz)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
