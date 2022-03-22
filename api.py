from flask import Flask, request

from code import Transformation

app = Flask(__name__)

#post method for rotate
@app.route("/rotate/", methods=['POST'])
def rotate():
    x = float(request.form['x'])
    y = float(request.form['y'])
    angle = float(request.form['angle'])

    transformer = Transformation()

    x, y = transformer.rotation(x, y, angle)
    return {'x': x, 'y': y}


@app.route("/translation/", methods=['POST'])
def translation():
    x = float(request.form['x'])
    y = float(request.form['y'])
    Tx = float(request.form['Tx'])
    Ty = float(request.form['Ty'])
    transformer = Transformation()

    x, y = transformer.translation(x, y, Tx, Ty)
    return {'x': x, 'y': y}


@app.route("/scaling/", methods=['POST'])
def scaling():
    x = float(request.form['x'])
    y = float(request.form['y'])
    Sx = float(request.form['Sx'])
    Sy = float(request.form['Sy'])
    transformer = Transformation()
    x, y = transformer.scaling(x, y, Sx, Sy)
    return {'x': x, 'y': y}


@app.route("/shering/", methods=['POST'])
def shering():
    x = float(request.form['x'])
    y = float(request.form['y'])
    Shx = float(request.form['Sx'])
    Shy = float(request.form['Sy'])
    transformer = Transformation()
    x = transformer.sheringX(x, y, Shx)
    x = transformer.sheringY(x, y, Shy)
    return {'x': x, 'y': y}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5007, debug=False)
