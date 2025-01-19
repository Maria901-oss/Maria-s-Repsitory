from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Initialize SQLite database (use the same 'game.db')
conn = sqlite3.connect('game.db', check_same_thread=False)
cursor = conn.cursor()
@app.route('/')
@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    try:
        # Fetch the top 10 scores ordered by the highest score
        cursor.execute('SELECT name, score FROM scores ORDER BY score DESC LIMIT 10')
        scores = cursor.fetchall()
        
        if scores:
            # Return the scores as JSON
            return jsonify([{"name": row[0], "score": row[1]} for row in scores]), 200
        else:
            return jsonify({"message": "No scores available."}), 200
    except Exception as e:
        return jsonify({"message": f"Alice has the highest score"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7001)
