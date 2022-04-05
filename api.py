from flask import Flask, send_from_directory, request
from functionalities import Transformation

app = Flask(__name__)

transformer = Transformation()


@app.route("/rotate")
def rotate():

    """
    This function take x,y,angle value as an input and operation implemented by
    rotation function calling of class Transformation and return the new x,y coordinates.
    :return: it returns the new coordinates after rotational
             transformation in post method
    """
    x = float(request.form["x"])
    y = float(request.form["y"])
    angle = float(request.form["angle"])
    graph = eval(request.form["graph"])
    if graph:
        transformer.rotation(x, y, angle, graph)
        return send_from_directory(".", "plot.png")
    else:
        x, y = transformer.rotation(x, y, angle, graph)
    return {"x": x, "y": y}


@app.route("/translation")
def translation():
    """
    #     This function take initial  x,y coordinates an as an input and operation implemented along_with add new coordinates value of tx,ty by translation function calling of class
    #     Transformation and return the new x,y coordinates.
    #     :return: it return new coordinates of object after translation
    #"""
    x = float(request.form["x"])
    y = float(request.form["y"])
    tx = float(request.form["tx"])
    ty = float(request.form["ty"])
    graph = eval(request.form["graph"])
    if graph:
        transformer.translation(x, y, tx, ty, graph)
        return send_from_directory(".", "plot.png")
    else:
        xnew, ynew = transformer.translation(x, y, tx, ty, graph)
        return {"x": xnew, "y": ynew}


@app.route("/scaling")
def scaling():
    """
    This function take initial  x,y coordinates an as an input and operation implemented by multiplying new
    coordinates value of Sx,Sy by scaling  function calling from class
    Transformation and return the new x,y coordinates.
    :return: it return new coordinates of object after scaling
    """
    x = float(request.form["x"])
    y = float(request.form["y"])
    Sx = float(request.form["Sx"])
    Sy = float(request.form["Sy"])
    graph = eval(request.form["graph"])
    if graph:
        transformer.scaling(x, y, Sx, Sy, graph)
        return send_from_directory(".", "plot.png")
    else:
        transformer.scaling(x, y, Sx, Sy, graph)
    return {"x": x, "y": y}


@app.route("/shering")
def shering():

    """
     This function take initial  x,y coordinates an as an input and operation implemented by shearing  function calling from class
    Transformation and return the new x,y coordinates.
    :return:it return new coordinates of object after shering transformation
    """
    x = float(request.form["x"])
    y = float(request.form["y"])
    Shx = float(request.form["Shx"])
    Shy = float(request.form["Shy"])
    graph = eval(request.form["graph"])
    if graph:
        transformer.shering(x, y, Shx, Shy, graph)
        return send_from_directory(".", "plot.png")
    else:
        xnew, ynew = transformer.shering(x, y, Shx, Shy, graph=True)
    return {"x": xnew, "y": ynew}


if __name__ == "__main__":
    app.run(host="127.0.0.4", port=5007, debug=True)


#     request_data = request.get_json()
#     x = request_data['x']
#     y = request_data['y']
#     Tx = request_data['Tx']
#     Ty = request_data['Ty']
#     transformer = Transformation()
#     x, y = transformer.translation(x, y, Tx, Ty)
#         if graph == True:
#               self.ploting(x, y, xnew, ynew, 'translation' + "  Tx=%.2f Ty=%.2f" % (Tx, Ty))
#         else:
#            return xnew, ynew
#
#     return {"x":x, "y":y}
