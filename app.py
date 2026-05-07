from flask import *
import pymysql
import pymysql.cursors
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = 'static/images'


def get_connection():
    return pymysql.connect(
        user='dumabashir',
        host='mysql-dumabashir.alwaysdata.net',
        password='modcom1234',
        database='dumabashir_dumasokogarden',
        cursorclass=pymysql.cursors.DictCursor
    )


@app.route("/api/signup", methods=['POST'])
def signup():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    phone = request.form.get('phone')
    role = request.form.get('role')

    if role not in ['student', 'school']:
        return jsonify({"Error": "Invalid role"}), 400

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users(username, password, email, phone, role) VALUES(%s, %s, %s, %s, %s)",
        (username, password, email, phone, role)
    )
    conn.commit()
    return jsonify({"Success": "Account created successfully"})


@app.route("/api/signin", methods=['POST'])
def signin():
    email = request.form.get('email')
    password = request.form.get('password')

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE email=%s AND password=%s",
        (email, password)
    )
    user = cursor.fetchone()

    if not user:
        return jsonify({"Error": "Invalid login"}), 401

    return jsonify({
        "Success": "Login successful",
        "user": user,
        "role": user['role']
    })


@app.route("/api/add_product", methods=['POST'])
def add_product():
    role = request.form.get('role')
    if role != "school":
        return jsonify({"Error": "Only school can add"}), 403

    name = request.form['product_name']
    desc = request.form['product_description']
    cost = request.form['product_cost']
    photo = request.files['product_photo']
    filename = photo.filename
    photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO product_details(product_name, product_description, product_cost, product_photo) VALUES(%s, %s, %s, %s)",
        (name, desc, cost, filename)
    )
    conn.commit()
    return jsonify({"Message": "Talent added"})


@app.route("/api/add_clothes", methods=['POST'])
def add_clothes():
    role = request.form.get('role')
    if role != "school":
        return jsonify({"Error": "Only school can upload clothes"}), 403

    name = request.form['name']
    desc = request.form['description']
    price = request.form['price']
    photo = request.files['photo']
    filename = photo.filename
    photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO clothes(name, description, price, photo) VALUES(%s, %s, %s, %s)",
        (name, desc, price, filename)
    )
    conn.commit()
    return jsonify({"Message": "Clothes added"})


@app.route("/api/add_instruments", methods=['POST'])
def add_instruments():
    role = request.form.get('role')
    if role != "school":
        return jsonify({"Error": "Only school can upload instruments"}), 403

    name = request.form['name']
    desc = request.form['description']
    price = request.form['price']
    photo = request.files['photo']
    filename = photo.filename
    photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO instruments(name, description, price, photo) VALUES(%s, %s, %s, %s)",
        (name, desc, price, filename)
    )
    conn.commit()
    return jsonify({"Message": "Instrument added"})


@app.route("/api/get_products_details")
def get_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product_details")
    return jsonify(cursor.fetchall())


@app.route("/api/get_clothes")
def get_clothes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clothes")
    return jsonify(cursor.fetchall())


@app.route("/api/get_instruments")
def get_instruments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM instruments")
    return jsonify(cursor.fetchall())


@app.route("/api/contact", methods=['POST'])
def contact():
    email = request.form.get('email')
    message = request.form.get('message')

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO messages(email, message) VALUES(%s, %s)",
        (email, message)
    )
    conn.commit()
    return jsonify({"Success": "Message received"})


if __name__ == "__main__":
    app.run(debug=True)