# import math
# class Transformation:
#     """
#     this is class whose name is Transformation.
#     """
#
#     def rotation(self, x, y, angel):
#         """
#
#         :param x: it take the input x coordinates
#         :param y: it take the input y coordinates
#         :param angel: it tells at which degree object will  rotate
#         :return: it returns the new x and y coordinate after rotation transformation
#         """
#         xnew = ((x * (math.cos(angel))) - (y * (math.sin(angel))))
#         ynew = ((y * (math.cos(angel))) + (x * (math.sin(angel))))
#         return xnew, ynew
#
#
#     def translation(self,x,y,Tx,Ty):
#         """
#         summary line:
#         In 2D translation object moves from one position to another in a two dimensional plane.
#         :parameters:
#         :param x: initial x coordinate taken by user
#         :param y: old  y coordinate taken by user
#         :param Tx: translation vector that will be added in initial coordinates.
#         :param Ty:shift vector or translational vector
#         :return:
#          it return new coordinates of object after translation
#         """
#         xnew = x + Tx
#         ynew = y + Ty
#         return xnew, ynew
#
#     def scaling(self,x,y,Sx, Sy):
#         """
#         summary line:
#         In scaling we modifying or altering the size of objects.
#         parameter:
#         :param x:initial x coordinates of the object
#         :param y:initial y coordinates of the object
#         :param Sx:Scaling factor for X-axis
#         :param Sy:Scaling factor for Y-axis
#         :return:
#         it return new coordinates of object after scaling
#         """
#         xnew = x * Sx
#         ynew = y * Sy
#         return xnew, ynew
#
#
#     def sheringX(self,x,y,Shx):
#         """
#
#         :param x: initial x coordinates of the object
#         :param y: initial x coordinates of the object
#         :param Shx:Shearing parameter towards X direction
#         :return:return New coordinates of the object after shearing
#         """
#         return x + (Shx * y)
#
#
#     def sheringY(self,y,x,Shy):
#         """
#
#         :param y:  initial y coordinates of the object
#         :param x:  initial x coordinates of the object
#         :param Shy: Shearing parameter towards Y direction
#         :return: return New coordinates of the object after shearing
#         """
#         return y + (Shy * x)
#
#
#
#
#
#
#
#
#
