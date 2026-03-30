from math import sqrt

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    @staticmethod
    def distancia(p1, p2):
        distX = p1.getX() - p2.getX()
        distY = p1.getY() - p2.getY()
        dist = sqrt(distX ** 2 + distY ** 2)
        return dist


    
