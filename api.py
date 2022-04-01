from flask import Flask, request

import function_methods
from code import Transformation
"""import class whose name is Transformaton from code file"""

app = Flask(__name__)

#post method for rotate
@app.route("/rect")
def rectangle():

    x = float(request.form['le'])
    y = float(request.form['wi'])


    function_methods.rect(x,y)
    return






if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5007, debug=False)
