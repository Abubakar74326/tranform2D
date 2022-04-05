from flask import Flask, request, send_from_directory

import function_methods

app = Flask(__name__)


@app.route("/rectangle")
def rectangle():
    """
    call the rectangle function from function_method file
    take length and width from user
    :return: plot the  image graph save in current directory
    """
    le = float(request.form["le"])
    wi = float(request.form["wi"])
    function_methods.rec(le, wi)
    return send_from_directory(".", "plot.png")


@app.route("/triangle")
def triangle():
    """
    call the triangle function from function_method file
    :return: plot the  image graph save in current directory
    """
    a = float(request.form["a"])
    b = float(request.form["b"])
    c = float(request.form["c"])
    d = float(request.form["d"])
    e = float(request.form["e"])
    f = float(request.form["f"])
    g = float(request.form["g"])
    h = float(request.form["h"])

    x = [a, b, c, d]
    y = [e, f, g, h]

    function_methods.tri(x, y)
    return send_from_directory(".", "plot.png")


@app.route("/circle")
def circle():
    """
    call the circle function from function_method file
    take radius from user
    :return: plot the  image graph save in current directory
    """
    radius = float(request.form["radius"])
    function_methods.cir(radius)
    return send_from_directory(".", "plot.png")


@app.route("/square")
def square():
    """
    call the square function from function_method file
    take same length and width from user
    :return: plot the  image graph save in current directory
    """
    le = float(request.form["le"])
    wi = float(request.form["wi"])
    function_methods.square(le, wi)
    return send_from_directory(".", "plot.png")


if __name__ == "__main__":
    app.run(host="127.0.0.7", port=5007, debug=True)
