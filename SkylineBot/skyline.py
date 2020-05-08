import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from random import randint


class Skyline:

    def __init__(self, start=[], height=[], width=[]):
        """ Creadora de Skyline """
        self.start = start
        self.width = width
        self.height = height

    @classmethod
    def random(cls, n, h, w, xmin, xmax):
        """ Retorna una instància de Skyline amb edificis aleatoris. """
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
        """ Retorna una instància de Skyline amb l'edificio indicat """
        start = [xmin]
        width = [xmax-xmin]
        height = [top]
        return cls(start, height, width)

    def plot(self):
        """ Genera un plot de barres per representar el Skyline. 
            Retorna l'area i l'altura màxima. """
        xMin, xMax = self.minNmax()
        left = max(0, xMin)
        normal = self.normalize(left, xMax)

        area = sum(normal)
        if normal:
            top = max(normal)
        else:
            top = 0

        start, height, width = self.simplify(normal, left)

        start.extend([1, 1])
        height.extend([0, 1])
        width.extend([1, 0])

        ax = plt.figure().gca()
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.bar(start, height, width, align='edge')
        return area, top

    def __add__(self, other):
        """ Operació 'unió' i 'desplaçament a la dreta' """
        if isinstance(other, int):  # desplaçament a la dreta
            start = [x+other for x in self.start]
            return Skyline(start, self.height, self.width)

        elif isinstance(other, Skyline):  # unió
            start = self.start + other.start
            height = self.height + other.height
            width = self.width + other.width
            return Skyline(start, height, width)
        print("Error: Suma incorrecte")

    def __mul__(self, other):
        """ Operació 'replicació' i 'intersecció' """
        if isinstance(other, int):  # replicació
            xMin, xMax = self.minNmax()
            offset = xMax - xMin
            start = self.start.copy()
            for i in range(1, other):
                start.extend([(i*offset) + x for x in self.start])
            return Skyline(start, self.height * other, self.width * other)

        elif isinstance(other, Skyline):  # intersecció
            a, b = self.minNmax()
            c, d = other.minNmax()
            left = max(a, c)
            right = min(b, d)
            if right <= left:  # no hi ha intersecció
                return Skyline()

            normal1 = self.normalize(left, right)
            normal2 = other.normalize(left, right)

            inter = []
            for n1, n2 in zip(normal1, normal2):
                inter.append(min(n1, n2))

            start, height, width = self.simplify(inter, left)
            return Skyline(start, height, width)
        print("Error: Multiplicació incorrecte")

    def __sub__(self, other):
        """ Desplaçament a l'esquerra """
        if isinstance(other, int):
            start = [x-other for x in self.start]
            return Skyline(start, self.height, self.width)
        print("Error: Resta incorrecte")

    def __neg__(self):  # mirall
        """ Operació mirall """
        start = []
        xMin, xMax = self.minNmax()
        for s, w in zip(self.start, self.width):
            start.append(xMax + xMin - (s+w))
        return Skyline(start, self.height, self.width)

    def getArea(self):
        """ Retorna l'àrea del Skyline """
        xMin, xMax = self.minNmax()
        left = max(0, xMin)
        normal = self.normalize(left, xMax)
        return sum(normal)

    def minNmax(self):
        """ Retorna  la posició inicial i final del Skyline"""
        xMin = 0
        if self.start:
            xMin = min(self.start)
        xMax = xMin
        for s, w in zip(self.start, self.width):
            if s+w > xMax:
                xMax = s+w
        return xMin, xMax

    def normalize(self, left, right):
        """ Retorna la llista normalitzada de l'interval del Skyline que va de 'left' a 'right' """
        normal = [0]*(right-left)
        for i in range(len(self.start)):
            s = self.start[i]
            w = self.width[i]
            if s < right and left < s+w:
                h = self.height[i]
                pos = s-left
                for j in range(w):
                    if left <= s+j < right:
                        normal[pos+j] = max(normal[pos+j], h)
        return normal

    def simplify(self, normal, offset):
        """ Retorna el mínim d'edificis a partir d'una llista normalitzada """
        start = []
        height = []
        width = []

        s = w = h = 0
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
