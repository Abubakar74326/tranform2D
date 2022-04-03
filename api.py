from flask import Flask, request,send_from_directory

import function_methods
app = Flask(__name__)

#post method for rotate
@app.route("/rect")
def rectangle():
    x = float(request.form['le'])
    y = float(request.form['wi'])
    function_methods.rect(x,y)
    return send_from_directory('.','plot.png')






if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5007, debug=True)
