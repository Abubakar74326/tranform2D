import math
class Transformation:

    def rotation(self, x, y, angel):
        xnew = ((x * (math.cos(angel))) - (y * (math.sin(angel))))
        ynew = ((y * (math.cos(angel))) + (x * (math.sin(angel))))
        return xnew, ynew


    def translation(self,x,y,Tx,Ty):
        xnew = x + Tx
        ynew = y + Ty
        return xnew, ynew

    def scaling(self,x,y,Sx, Sy): # *scal
        xnew = x * Sx
        ynew = y * Sy
        return xnew, ynew


    def sheringX(self,x,y,Shx):
        return x + (Shx * y)


    def sheringY(self,y,x,Shy):
        return y + (Shy * x)









