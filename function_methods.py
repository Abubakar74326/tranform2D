import matplotlib
import matplotlib.backend_tools
import matplotlib.pyplot as plt

def rec(le,wi):
    fig = plt.figure()
    ax = fig.add_subplot()
    rect = matplotlib.patches.Rectangle((1, 1), le, wi,color='green')
    ax.add_patch(rect)
    plt.savefig('plot.png')
    plt.xlim([0, 10])
    plt.ylim([0, 10])
    plt.show()

def tri():




rec(3,4)