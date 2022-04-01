import matplotlib
import matplotlib.pyplot as plt

def rec(le,wi):
    fig = plt.figure()
    ax = fig.add_subplot()
    pl
    rect = matplotlib.patches.Rectangle((1, 1), le, wi,color='green')
    ax.add_patch(rect)
    plt.xlim([0, 10])
    plt.ylim([0, 10])

    plt.show()
rec(3,4)