from flask import Flask, render_template
from flask import jsonify
import mysql.connector

app = Flask(__name__)

# app= flask.Flask(_name_)
app.config["DEBUG"] = True


my_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kirakira22",
        database="potet"
    )


my_cursor = my_db.cursor()

my_cursor.execute("select * from products")

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

def connect_db():
    my_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kirakira22",
        database="potet"
    )
    print(my_db)

    my_cursor = my_db.cursor()

    my_cursor.execute("select * from products")

    for x in my_cursor:
        print(x)

    my_cursor.execute("select navn from products")

    for y in my_cursor:
        print(y)

products = [
    {
        'id': 0,
        'P_name': "Eple",
        'bilde': "Et bilde"
    }
]


@app.route('/products', methods=['GET'])
def get_drinks():
    return render_template("products.html")


if __name__ == '__main__':


    connect_db()

    app.run(debug=True)


