import sqlite3

# Connect to the SQLite database (game.db)
conn = sqlite3.connect('game.db')
cursor = conn.cursor()

# Create the 'scores' table if it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS scores (
    name TEXT NOT NULL,
    score INTEGER NOT NULL
)
''')

# Insert sample data to test the leaderboard (optional)
cursor.execute('INSERT INTO scores (name, score) VALUES (?, ?)', ('Alice', 25))
cursor.execute('INSERT INTO scores (name, score) VALUES (?, ?)', ('Bob', 15))
cursor.execute('INSERT INTO scores (name, score) VALUES (?, ?)', ('Charlie', 20))

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database initialized successfully.")
