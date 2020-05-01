import matplotlib.pyplot as plt  # grafica

from random import randint


def toList(x):  # ineficiente ???
    if isinstance(x, list):
        return x
    else:
        return [x]


class Skyline:

    """ height = []
    start = []
    width = [] """

    def __init__(self, start=[], height=[], width=[]):
        """ Creadora de Skylines """
        self.start = toList(start)
        self.width = toList(width)
        self.height = toList(height)
        # funcion borrar negativos.

    @classmethod
    def random(cls, n, h, w, xmin, xmax):
        """ Devueve una instancia de Skyline con los edificios aleatorios indicados """
        start = []
        height = []
        width = []
        for _ in range(n):
            while True:
                wb = randint(1, w)
                sb = randint(xmin, xmax)
                if sb+wb <= xmax:
                    break
            tb = randint(0, h)
            start.append(sb)
            width.append(wb)
            height.append(tb)
        return cls(start, height, width)

    @classmethod
    def single(cls, xmin, top, xmax):
        """ Devuelve una instancia de Skyline del edificio indicado """
        start = [xmin]
        width = [xmax-xmin]
        height = [top]
        return cls(start, height, width)

    def plot(self):
        """ crea un plot para representar por pantalla. Elimina edificios sin area, y de la parte negativa """
        xMin, xMax = self.minNmax()
        left = max(0,xMin)
        normal = self.normalize(left,xMax) #ahorra mucho tiempo al generar el plot
        
        start, height, width  = self.simplify(normal,left)

        start.append(1)
        height.append(0)
        width.append(1)
        
        plt.bar(start, height, width, align='edge')

    # demasiado lento
    """ def plot2(self):
        start = [1]
        height = [0]
        width = [1]
        for i in range(len(self.start)):
            if (self.height[i] > 0) and (self.width[i] > 0):
                if self.start[i] >= 0:
                    start.append(self.start[i])
                    width.append(self.width[i])
                    height.append(self.height[i])
                elif self.start[i] + self.width[i] > 0:
                    start.append(0)
                    width.append(self.start[i] + self.width[i])
                    height.append(self.height[i])
        plt.bar(start, height, width, align='edge') """

    def simplify(self, normal, offset):
        """ Genera minimo numero de edificios a partir de un vector normalizado """
        start = []
        height = []
        width = []

        s = w = h =  0
        for i in range(len(normal)):
            if normal[i] == h:
                w += 1
            else:
                if h != 0:
                    start.append(offset+s)
                    height.append(h)
                    width.append(w)
                s = i
                w = 1
                h = normal[i]

        start.append(offset+s)
        height.append(h)
        width.append(w)

        return start, height, width



    def __add__(self, other):
        if isinstance(other, int):  # desplaçament n posicions
            start = [x+other for x in self.start]
            return Skyline(start, self.height, self.width)
        elif isinstance(other, Skyline):  # unio
            start = self.start + other.start
            height = self.height + other.height
            width = self.width + other.width
            return Skyline(start, height, width)
        print("Error: en la suma")

    def __mul__(self, other):
        if isinstance(other, int):
            xMin, xMax = self.minNmax()
            offset = xMax - xMin
            start = self.start.copy()
            for i in range(1, other):
                start.extend([(i*offset) + x for x in self.start])
            return Skyline(start, self.height * other, self.width * other)

        elif isinstance(other, Skyline):
            a, b = self.minNmax()
            c, d = other.minNmax()
            left = max(a, c)
            right = min(b, d)
            if right <= left:  # no hay interseccion!
                return Skyline()

            normal1 = self.normalize(left,right)
            normal2 = other.normalize(left,right)

            """ print(normal1)
            print(normal2) """

            inter = []
            for n1, n2 in zip(normal1, normal2):
                inter.append(min(n1,n2))

            #print(inter)
            start, height, width  = self.simplify(inter,left)
            return Skyline(start,height,width)

        print("Error: en la multiplicacion")

    def normalize(self, left, right):
        """ normaliza seccion del Skyline devolviendo una lista con la altura en cada posición del intervalo """
        normal = [0]*(right-left)
        for i in range(len(self.start)):
                s = self.start[i]
                w = self.width[i]
                if s < right and left < s+w:
                    h = self.height[i]
                    pos = s-left
                    for j in range(w):
                        #if 0 <= pos+j < len(inter):
                        if left <= s+j < right:
                            normal[pos+j] = max(normal[pos+j], h)
        return normal

    def minNmax(self):
        xMin = 0
        if self.start:
            xMin = min(self.start)
        xMax = xMin
        for s, w in zip(self.start, self.width):
            if s+w > xMax:
                xMax = s+w
        return xMin, xMax

    def __sub__(self, other):
        if isinstance(other, int):  # desplaçament esquerra
            start = [x-other for x in self.start]
            return Skyline(start, self.height, self.width)

    def __neg__(self):  # mejorar con minNmax
        start = []
        xMin, xMax = self.minNmax()
        for s, w in zip(self.start, self.width):
            start.append(xMin - (s+w-xMin))
        offset = abs(xMin - min(start)) #error! MEJORAAAAAR!!!
        start = [offset+x for x in start]
        return Skyline(start, self.height, self.width)

    def getArea(self):
        xMin, xMax = self.minNmax()
        normal = self.normalize(xMin,xMax) #ahorra mucho tiempo al generar el plot
        return sum(normal)




#Test Skyline * Skyline
a = Skyline.single(1,2,3)
b = Skyline.single(2,3,3)
""" print( (a*b).start ) """
a * b

a = Skyline([2,5,4],[2,3,7],[2,2,1])
b = Skyline(3,4,3)
a * b
b * a






""" x = Skyline.random(10000,20,3,10,10000)
#z = Skyline.random(100,20,3,1,100)


x.plot()
fitxer = "%d.png" % randint(1000000, 9999999)
plt.savefig(fitxer, bbox_inches='tight')

(x*x).plot()
fitxer = "%d.png" % randint(1000000, 9999999)
plt.savefig(fitxer, bbox_inches='tight')

(x*x).plot()
x.plot()
fitxer = "%d.png" % randint(1000000, 9999999)
plt.savefig(fitxer, bbox_inches='tight') """


