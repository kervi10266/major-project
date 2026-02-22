from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('sales.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/sales', methods=['GET'])
def get_sales():
    conn = get_db_connection()
    sales = conn.execute('SELECT * FROM sales').fetchall()
    conn.close()

    sales_list = [dict(row) for row in sales]
    return jsonify(sales_list)

if __name__ == '__main__':
    app.run(debug=True)