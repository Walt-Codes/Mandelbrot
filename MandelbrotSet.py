import numpy as np

FILENAME = "M_depth_"


class MandelbrotSet:
    val_of = {}
    hits = 0
    misses = 0
    baseDepth = 30
    scale = 15/16
    res = 30





    def __init__(self):

        f = open(self.fullFilename(), "a")
        f.close()

        f = open(self.fullFilename(), "r")
        for line in f:
            x, y, z = [float(r) for r in line.split()]
            self.val_of[str(x)+" "+str(y)] = z
        f.close()

    def has(self, x, y):
        return str(x)+" "+str(y) in self.val_of

    def calc_value(self, x, y, depth, num):
        x = round(x, num)
        y = round(y, num)
        s = str(x)+" "+str(y)
        if s in self.val_of:
            self.hits += 1
            return self.val_of[s]
        self.misses += 1
        originalx = x
        originaly = y
        for i in range(self.baseDepth+depth):
            tempx = x**2 - y**2 + originalx
            tempy = 2*x*y + originaly
            x = tempx
            y = tempy

            magnitude = np.sqrt(x**2+y**2)

            if magnitude > 20:
                self.val_of[s] = 1
                f = open(self.fullFilename(), "a")
                f.write(s+" "+str(magnitude)+"\n")
                f.close()
                return magnitude

        val = magnitude
        self.val_of[s] = val
        f = open(self.fullFilename(), "a")
        f.write(s + " " + str(val)+"\n")
        f.close()
        return val

    def fullFilename(self):
        return FILENAME+str(self.baseDepth)

