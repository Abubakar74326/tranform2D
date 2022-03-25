from matplotlib import pyplot as plt
from matplotlib import style
plt.rcParams["figure.figsize"] = [7, 3]
plt.rcParams["figure.autolayout"] = True
import transformations
x=2
y=2

def ploting(x, y, xnew, ynew):
    plt.xlim(0, 7)
    plt.ylim(0, 7)

    plt.grid()
    # plt.title("scaling")
    # st = input("enter the tittle")
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    xpoints = [x, xnew]
    ypoints = [y, ynew]
    plt.plot(xpoints, ypoints, "*" )
    #myplot = plt.plot(xpoints, ypoints, marker="o", markersize=10, markeredgecolor="blue", markerfacecolor="red")
    plt.plot(x,y, "o")
    plt.show()

xnew, ynew = transformations.translation(x, y, 2, 4)
#xnew, ynew = transformations.scaling(x, y, 3, 2)
#xnew, ynew = transformations.rotation(x,y,0.4)



ploting(x, y, xnew, ynew)
