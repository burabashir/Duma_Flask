# importing flask
from flask import *

# initializing the flask app
app = Flask(__name__)

# defining a simple route/endpoint
# designated endpoint for our web application function
@app.route("/api/home")
# function for our web application
def home():
    return jsonify ({"Message": "Welcome to the home api"})


# defining a simple route/endpoint
@app.route("/api/products")
# corresponding function for our web application
def products():
    return jsonify ({"Message" : "Welcome to the products api"})

@app.route("/api/services")
# corresponding function for our web application
def services():
    return jsonify ({"Message": "Welcome to the services api"})




# run the app when this file is executed
app.run(debug= True)