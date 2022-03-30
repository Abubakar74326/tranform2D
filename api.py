from flask import Flask, request, render_template
from functionalities import Transformation
# import visualization
app = Flask(__name__)
#OBJECT of Class
transformer = Transformation()
# post method for rotate
@app.route("/rotate/", methods=['POST'])
def rotate():
    """
    This function take x,y,angle value as an input and operation implemented by rotation function calling of class
    Transformation and return the new x,y coordinates.
    :return: it returns the new coordinates after rotational transformation in post method
    """
    x = float(request.form['x'])
    y = float(request.form['y'])
    angle = float(request.form['angle'])
    x, y = transformer.rotation(x, y, angle)
    return {'x': x, 'y': y}


# Post method for translational
@app.route("/translations", methods=['POST'])
def translation():
    x = float(request.form['x'])
    y = float(request.form['y'])
    tx = float(request.form['tx'])
    ty = float(request.form['ty'])
    x, y = transformer.translation(x, y, tx, ty)
    return {'x': x, 'y': y}


#     """
#     This function take initial  x,y coordinates an as an input and operation implemented along_with add new coordinates value of Tx,Ty by translation function calling of class
#     Transformation and return the new x,y coordinates.
#     :return: it return new coordinates of object after translation
#     """
#     request_data = request.get_json()
#     x = request_data['x']
#     y = request_data['y']
#     Tx = request_data['Tx']
#     Ty = request_data['Ty']
#     transformer = Transformation()
#     x, y = transformer.translation(x, y, Tx, Ty)
#     # print(x,y)
#     return {"x":x, "y":y}


# Post method for scaling
@app.route("/scaling/", methods=['POST'])
def scaling():
    """
    This function take initial  x,y coordinates an as an input and operation implemented by multiplying new coordinates value of Sx,Sy by scaling  function calling from class
    Transformation and return the new x,y coordinates.
    :return: it return new coordinates of object after scaling
    """
    x = float(request.form['x'])
    y = float(request.form['y'])
    Sx = float(request.form['Sx'])
    Sy = float(request.form['Sy'])

    x, y = transformer.scaling(x, y, Sx, Sy)
    return {'x': x, 'y': y}


# Post method for shering
@app.route("/shearing/", methods=['POST'])
def shering():
    """
     This function take initial  x,y coordinates an as an input and operation implemented by shearing  function calling from class
    Transformation and return the new x,y coordinates.
    :return: it return new coordinates of object after shering transformation
    """
    x = float(request.form['x'])
    y = float(request.form['y'])
    Shx = float(request.form['Shx'])
    Shy = float(request.form['Shy'])

    x = transformer.shering(x, y, Shx,Shy)
    return {'x': x, 'y': y}

'''#ploting function
@app.route('/plot_translation/')
def plot():
    """
     this is self practice to take the translation graph as an output from ploting function of visualization file by api
    :return:
    """
    x = float(request.form['x'])
    y = float(request.form['y'])
    Tx = float(request.form['Tx'])
    Ty = float(request.form['Ty'])
    xnew, ynew = transformer.translation(x, y, Tx, Ty)
    plot, url = visualization.ploting(x, y, xnew,ynew)
    return render_template(plot, plot_url=url)
#
# '''
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5007, debug=True)
