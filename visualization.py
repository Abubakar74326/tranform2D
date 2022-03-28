import base64

from matplotlib import pyplot as plt
from io import BytesIO

import transformations
plt.rcParams["figure.figsize"] = [7, 3]
plt.rcParams["figure.autolayout"] = True
x=4
y=2

def ploting(x, y, xnew, ynew):
    plt.xlim(0, 7)
    plt.ylim(0, 7)
    plt.grid()
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    xpoints = [x, xnew]
    ypoints = [y, ynew]
    plt.plot(xpoints, ypoints, "*" )
    #myplot = plt.plot(xpoints, ypoints, marker="o", markersize=10, markeredgecolor="blue", markerfacecolor="red")
    plt.plot(x,y, "o")
    img = BytesIO()
    plt.savefig(img, format='png')
    plt.show()
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return 'plot.html', plot_url

xnew, ynew = transformations.translation(x, y, 2, 4)
#xnew, ynew = transformations.scaling(x, y, 3, 2)
#xnew, ynew = transformations.rotation(x,y,0.4)



ploting(x, y, xnew, ynew)
