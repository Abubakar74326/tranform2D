import math

import matplotlib.pyplot as plt
from pylab import imread, imshow, show
class Transformation:

    def ploting(self, x, y, xnew, ynew, title_):
        plt.grid()
        plt.title(title_)
        plt.xlabel("X-Axis")
        plt.ylabel("Y-Axis")
        plt.xlim(0,30)
        plt.ylim(0,30)
        plt.plot(x, y, "o", markersize=10)
        plt.plot(xnew, ynew, "*", markersize=10)

        plt.savefig('plot.png')
        # image = plt.imread('plot.png')
        # plt.imshow(image)
        plt.show()

    def rotation(self, x, y, angle, graph = True):
        """

        :param x: it take the input x coordinates
        :param y: it take the input y coordinates
        :param angel: it tells at which degree object will  rotate
        :return: it returns the new x and y coordinate after rotation transformation
        """
        pi = 22/7
        radian = angle * (pi/180)
        xnew = ((x * (math.cos(radian))) - (y * (math.sin(radian))))
        ynew = ((y * (math.cos(radian))) + (x * (math.sin(radian))))



        if graph == True:
            self.ploting(x, y, xnew, ynew,'rotation'+"  x=%.2f y=%.2f angle =%.2f" % (x, y, angle))

        return xnew, ynew

    def translation(self, x, y, Tx, Ty, graph = False):
        """
        summary line:
        In 2D translation object moves from one position to another in a two dimensional plane.
        :parameters:
        :param x: initial x coordinate taken by user
        :param y: old  y coordinate taken by user
        :param Tx: translation vector that will be added in initial coordinates.
        :param Ty:shift vector or translational vector
        :return:
         it return new coordinates of object after translation
        """
        xnew = x + Tx
        ynew = y + Ty
        if graph == True:
             self.ploting(x, y, xnew, ynew, 'translation'+"  Tx=%.2f Ty=%.2f" % (Tx, Ty))
        else:
            return xnew, ynew

    def scaling(self, x, y, Sx, Sy, graph=True):
        """
        summary line:
        In scaling we modifying or altering the size of objects.
        parameter:
        :param graph:
        :param x:initial x coordinates of the object
        :param y:initial y coordinates of the object
        :param Sx:Scaling factor for X-axis
        :param Sy:Scaling factor for Y-axis
        :return:
        it return new coordinates of object after scaling
        """
        xnew = x * Sx
        ynew = y * Sy
        if graph==True:
            self.ploting(x,y,xnew,ynew,'Scaling'+"  Sx=%.2f Sy=%.2f" % (Sx, Sy))
        return xnew, ynew


    def shering(self, x, y, Shx, Shy, graph=True):
        """

        :param y:  initial y coordinates of the object
        :param x:  initial x coordinates of the object
        :param Shy: Shearing parameter towards Y direction
        :return: return New coordinates of the object after shearing
        """
        xnew = x + (Shx * y)
        ynew = y + (Shy * x)
        if graph==True:
         self.ploting(x,y,xnew,ynew, 'Shearing'+"  Shx=%.2f Shy=%.2f" % (Shx, Shy))

        return xnew,ynew

'''if __name__ == "__main__":
    t = Transformation()
    xnew, ynew = t.rotation(1, 2, -45, graph=True)
    print(xnew, ynew)
    # Transformation.ploting(1, 2, xnew, ynew )
'''