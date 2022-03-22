from flask import Flask, request

from code import Transformation
"""import class whose name is Transformaton from code file"""

app = Flask(__name__)

#post method for rotate
@app.route("/rotate/", methods=['POST'])
def rotate():
    """

    :return: it returns the new coordinates after rotational transformation in post method
    """
    x = float(request.form['x'])
    y = float(request.form['y'])
    angle = float(request.form['angle'])

    transformer = Transformation()

    x, y = transformer.rotation(x, y, angle)
    return {'x': x, 'y': y}

#Post method for translational
@app.route("/translation/", methods=['POST'])
def translation():
    """

    :return: it return new coordinates of object after translation
    """
    x = float(request.form['x'])
    y = float(request.form['y'])
    Tx = float(request.form['Tx'])
    Ty = float(request.form['Ty'])

    transformer = Transformation()
    """object of Transformational class """
    x, y = transformer.translation(x, y, Tx, Ty)
    return {'x': x, 'y': y}

#Post method for scaling
@app.route("/scaling/", methods=['POST'])
def scaling():
    """

    :return: it return new coordinates of object after scaling
    """
    x = float(request.form['x'])
    y = float(request.form['y'])
    Sx = float(request.form['Sx'])
    Sy = float(request.form['Sy'])
    transformer = Transformation()
    """object of Transformation class"""
    x, y = transformer.scaling(x, y, Sx, Sy)
    """function call"""
    return {'x': x, 'y': y}

#Post method for shering
@app.route("/shering/", methods=['POST'])
def shering():
    """

    :return: it return new coordinates of object after shering transformation
    """
    x = float(request.form['x'])
    y = float(request.form['y'])
    Shx = float(request.form['Sx'])
    Shy = float(request.form['Sy'])
    transformer = Transformation()
    x = transformer.sheringX(x, y, Shx)
    """functional call for x coordinate"""
    y = transformer.sheringY(y, x, Shy)
    """functional call for y coordinate"""

    return {'x': x, 'y': y}
    """return the value of new coordinates of x ,y"""


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5007, debug=False)
