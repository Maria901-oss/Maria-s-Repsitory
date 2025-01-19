from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import random

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

SECRET_NUMBER = random.randint(1, 100)  # Generate a random number initially
ATTEMPTS = {}  # Track attempts for each player

# Initialize SQLite database
conn = sqlite3.connect('game.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS scores (name TEXT, score INTEGER)''')
conn.commit()

@app.route('/guess', methods=['POST'])
def guess_number():
    global SECRET_NUMBER, ATTEMPTS
    data = request.get_json()  # Ensure you get JSON data
    name = data.get('name')  # Get the player's name
    guess = data.get('guess')

    if not isinstance(guess, int):
        return jsonify({"message": "Invalid input. Please provide a number."}), 400

    # Track the number of attempts per player
    if name not in ATTEMPTS:
        ATTEMPTS[name] = 0
    ATTEMPTS[name] += 1

    if guess < SECRET_NUMBER:
        return jsonify({"message": "Too low!"}), 200
    elif guess > SECRET_NUMBER:
        return jsonify({"message": "Too high!"}), 200
    else:
        # Calculate points based on attempts (max 10 points, min 1 point)
        points = max(10 - (ATTEMPTS[name] - 1), 1)

        # Update or insert player's score into the database
        cursor.execute('SELECT score FROM scores WHERE name = ?', (name,))
        result = cursor.fetchone()
        if result:
            total_score = result[0] + points
            cursor.execute('UPDATE scores SET score = ? WHERE name = ?', (total_score, name))
        else:
            total_score = points
            cursor.execute('INSERT INTO scores (name, score) VALUES (?, ?)', (name, total_score))
        conn.commit()

        # Reset the game
        SECRET_NUMBER = random.randint(1, 100)
        ATTEMPTS[name] = 0  # Reset attempts for the player

        return jsonify({"message": f"Correct! You win! Total Score: {total_score}"}), 200
@app.route('/')
@app.route('/highscores', methods=['GET'])
def get_high_scores():
    cursor.execute('SELECT name, score FROM scores ORDER BY score DESC LIMIT 10')
    scores = cursor.fetchall()
    return jsonify([{"name": row[0], "score": row[1]} for row in scores]), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)
