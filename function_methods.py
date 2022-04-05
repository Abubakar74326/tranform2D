import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def rec(le, wi):
    """
    this function take two input length le,width wi as parameter and return
    the graph of rectangle
    :param le: length
    :param wi: width
    :return: plot graph of rectangle
    """
    fig = plt.figure()
    ax = fig.add_subplot()
    rect = matplotlib.patches.Rectangle((0, 0), le, wi, color="green")
    ax.add_patch(rect)
    plt.xlim([0, 10])
    plt.ylim([0, 10])
    plt.savefig("plot.png")
    plt.show()


def tri(x, y):
    """
    x,y coordinates of triangle
    :return: plot graph of triangle
    """
    # x = np.array([1, 4, 4, 1])
    # y = np.array([1, 1, 3, 1])
    if len(x) == 4 and len(y) == 4:
        a = np.array(x)
        b = np.array(y)
        plt.plot(a, b, color="green")
        plt.savefig("plot.png")
        plt.xlim([0, 10])
        plt.ylim([0, 10])
        plt.show()
    else:
        print("this triangle offer four coordinates of x and y")


def cir(radius):
    """
    this function take the radius of circle as input and return circle graph
    :param radius: input radius
    :return: plot graph of circle
    """
    fig = plt.figure()
    ax = fig.add_subplot()
    circle = Circle((0, 0), radius, color="green")
    ax.add_patch(circle)
    plt.xlim([-10, 10])
    plt.ylim([-10, 10])
    plt.savefig("plot.png")
    plt.show()


def square(le):
    """
    it take length and width as input and return graph of square
    :param le: length
    :param wi: width
    :return: plot square graph
    """

    fig = plt.figure()
    ax = fig.add_subplot()
    rect = matplotlib.patches.Rectangle((1, 1), le, le, color="green")
    ax.add_patch(rect)
    plt.xlim([-10, 10])
    plt.ylim([-10, 10])
    plt.savefig("plot.png")
    plt.show()


if __name__ == "__main__":
    """testing"""
    # square(3)
    # tri([1,4,4,1],[1,1,3,1])
