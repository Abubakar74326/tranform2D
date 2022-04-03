import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.patches import Rectangle




def rec(le,wi):
    fig = plt.figure()
    ax = fig.add_subplot()
    rect = matplotlib.patches.Rectangle((0,0), le, wi,color='green')
    ax.add_patch(rect)
    plt.xlim([0, 10])
    plt.ylim([0, 10])
    plt.savefig('plot.png')
    plt.show()

def tri():
    #fig =plt.figure()
    #ax=fig.add_subplot

    x = np.array([1, 4, 4, 1])
    y = np.array([1, 1, 3, 1])
    plt.plot(x,y,color='green')
    plt.xlim([0, 10])
    plt.ylim([0, 10])
    plt.show()

def cir(radius):
    fig =plt.figure()
    ax= fig.add_subplot()
    circle = Circle((0,0),radius, color = "green")
    ax.add_patch(circle)
    plt.xlim([-10,10])
    plt.ylim([-10,10])
    plt.show()


#cir(5)
tri()
#rec(2,3)