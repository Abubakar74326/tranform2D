from flask import Flask, request,send_from_directory

import function_methods
app = Flask(__name__)

#post method for rect
@app.route("/rectangle")
def rectangle():
    le = float(request.form['le'])
    wi = float(request.form['wi'])
    function_methods.rec(le,wi)
    return send_from_directory('.','plot.png')

@app.route("/tri")
def triangle():
    function_methods.tri()
    return send_from_directory('.', 'plot.png')

@app.route("/circle")
def circle():
    radius = float(request.form['radius'])
    function_methods.cir(radius)
    return send_from_directory('.', 'plot.png')

@app.route("/square")
def square():
    le = float(request.form['le'])
    wi = float(request.form['wi'])
    function_methods.square(le,wi)
    return send_from_directory('.','plot.png')



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5007, debug=True)
