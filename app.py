from flask import Flask, render_template, jsonify
import mysql.connector
from config import DB_CONFIG

app = Flask(__name__)

def get_data(query):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/skills')
def skills():
    query = """
    SELECT skills, COUNT(*) as freq 
    FROM jobs 
    GROUP BY skills 
    ORDER BY freq DESC LIMIT 10;
    """
    result = get_data(query)
    labels = [row[0] for row in result]
    data = [row[1] for row in result]
    return jsonify({'labels': labels, 'data': data})

if __name__ == '__main__':
    app.run(debug=True)