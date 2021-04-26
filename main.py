from flask import Flask, redirect, url_for, render_template
from flask import jsonify

app = Flask(__name__)

#app= flask.Flask(_name_)
app.config["DEBUG"]= True

@app.route('/')
def index():
    return render_template('index.html')

products= [
    {
        'id': 0,
        'P_name': "Eple",
        'bilde': "Et bilde"
    }
]
@app.route('/products')
def get_drinks():
    return jsonify(products)


if __name__ == '__main__':
    app.run(debug=True)