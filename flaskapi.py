from flask import Flask, jsonify
import sqlite3
app = Flask(__name__)


@app.route('/data', methods=['GET'])
def get_data():
    connection = sqlite3.connect('db.sqlite3')

    cursor = connection.cursor()

    data = cursor.execute('SELECT * FROM quotes')

    return jsonify({'data': data.fetchall()})


@app.route('/data/<int:id>', methods=['GET'])
def get_id(id):
    connection = sqlite3.connect('db.sqlite3')

    cursor = connection.cursor()

    data = cursor.execute(f'SELECT * FROM quotes where id={id}')

    return jsonify({'data': data.fetchall()})


if __name__ == '__main__':
    app.run(debug=True)
