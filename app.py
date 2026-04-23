# import flask
from flask import *

# importing pymysql
import pymysql
import pymysql.cursors

# initialize the flask app
app = Flask(__name__)
import os
app.config['UPLOAD_FOLDER'] = 'static/images'

# define the route for corresponding web application function
@app.route("/api/signup", methods = ['POST'])

# function corresponding to the route
def signup():
    # getting user inputs
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    phone = request.form['phone']
    # establishing a connection to our database
    connection = pymysql.connect (user = 'root', host = 'localhost', password = '', database = 'dumasokogarden')
    # defining the cursor
    cursor = connection.cursor()
    # sql query to insert data into the database
    sql = "insert into users(username, password, email, phone) values(%s, %s, %s, %s)"
    # defining the data to replace the placeholders
    data = (username, password, email, phone)
    # execute the sql query
    cursor.execute(sql, data)
    # commiting changes to database
    connection.commit()
    # return response to user
    return jsonify({"Success": "Thank you for signing up"})









# define the route for corresponding web application function
@app.route("/api/signin", methods = ['POST'])

# function corresponding to the route
def signin():
    # getting user inputs
    email = request.form['email']
    password = request.form['password']
    # establishing a connection to our database
    connection = pymysql.connect (user = 'root', host = 'localhost', password = '', database = 'dumasokogarden')
    # defining the cursor
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    # sql query to insert data into the database
    sql = "select * from users where email = %s and password = %s"
    # defining the data to replace the placeholders
    data = ( email,  password)
    # execute the sql query
    cursor.execute(sql, data)
    # check numbers of rows returned
    count = cursor.rowcount
    # if condition to check row number
    if count == 0 :
        return jsonify ({"Error": "Sign in failed"})
    else:
        user = cursor.fetchone()
        return jsonify ({"Success": "Sign in successful" , "user" : user})




# add_product api
# creating the route
@app.route("/api/add_product", methods = ['POST'])
# defining the corresponding web application function
def add_product():
    # get user inputs
    product_name = request.form['product_name']
    product_description = request.form['product_description']
    product_cost = request.form['product_cost']
    # extracting the imge data
    photo = request.files['product_photo']
    # extracting file
    filename = photo.filename
    # defining the photo's file path
    photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    # saving the filepath
    photo.save(photo_path)

    
    # establish the connection to the database
    connection = pymysql.connect (user = 'root', host = 'localhost', password = '', database = 'dumasokogarden')
    # defining the cursor
    cursor = connection.cursor()
    # defining the sql query
    sql = "insert into product_details(product_name, product_description, product_cost, product_photo) values (%s, %s, %s, %s)"
    # defining the data
    data = (product_name, product_description, product_cost, filename)
    # execute the sql query
    cursor.execute(sql, data)
    # commit/save to the database
    connection.commit()
    # return a response to the user
    return jsonify ({"Message": "Product added successfully"})




# get_product_details api
# definig the route
@app.route("/api/get_products_details")
# define the corresponding web application function
def get_product_details():
    # establishing connection to database
    connection = pymysql.connect(user = 'root', host = 'localhost', password = '', database = 'dumasokogarden')
    # defining the cursor
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    # defing the sql query
    sql = "select * from product_details"
    # execute the sql query
    cursor.execute(sql)
    # fetching all rows retrieved by the sql query
    product_details = cursor.fetchall()
    # closing the database connection
    connection.close()
    # return a response to the user
    return jsonify (product_details)



# Mpesa Payment Route/Endpoint 
import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth

@app.route('/api/mpesa_payment', methods=['POST'])
def mpesa_payment():
    if request.method == 'POST':
        amount = request.form['amount']
        phone = request.form['phone']
        # GENERATING THE ACCESS TOKEN
        # create an account on safaricom daraja
        consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
        consumer_secret = "amFbAoUByPV2rM5A"

        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"  # AUTH URL
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

        data = r.json()
        access_token = "Bearer" + ' ' + data['access_token']

        #  GETTING THE PASSWORD
        timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
        passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
        business_short_code = "174379"
        data = business_short_code + passkey + timestamp
        encoded = base64.b64encode(data.encode())
        password = encoded.decode('utf-8')

        # BODY OR PAYLOAD
        payload = {
            "BusinessShortCode": "174379",
            "Password": "{}".format(password),
            "Timestamp": "{}".format(timestamp),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": "1",  # use 1 when testing
            "PartyA": phone,  # change to your number
            "PartyB": "174379",
            "PhoneNumber": phone,
            "CallBackURL": "https://modcom.co.ke/api/confirmation.php",
            "AccountReference": "account",
            "TransactionDesc": "account"
        }

        # POPULAING THE HTTP HEADER
        headers = {
            "Authorization": access_token,
            "Content-Type": "application/json"
        }

        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"  # C2B URL

        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
        return jsonify({"message": "Please Complete Payment in Your Phone and we will deliver in minutes"})



# run the app
app.run(debug= True)