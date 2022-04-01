import matplotlib
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.patches import  Rectangle
#import matplotlib.backend_tools




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

#tri()
rec(2,3)