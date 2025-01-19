import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [guess, setGuess] = useState('');
  const [name, setName] = useState('');
  const [message, setMessage] = useState('');
  const [highScores, setHighScores] = useState([]);

  const handleGuess = async () => {
    try {
      const response = await axios.post('http://localhost:7000/guess', { name, guess: parseInt(guess) });
      setMessage(response.data.message);
    } catch (error) {
      if (error.response) {
        setMessage(error.response.data.message || 'An error occurred.');
      } else {
        setMessage('Unable to connect to the server.');
      }
    }
  };
  const updateLeaderboard = async (name, score) => {
    try {
      const response = await axios.post(
        'http://localhost:7001/update_leaderboard',
        { name, score },
        { headers: { 'Content-Type': 'application/json' } } // Ensure correct header
      );
      console.log(response.data.message);
    } catch (error) {
      console.error(error.response ? error.response.data.message : 'An error occurred.');
    }
  };
  
  const fetchHighScores = async () => {
    try {
      const response = await axios.get('http://localhost:7000/highscores');
      setHighScores(response.data);
    } catch (error) {
      setMessage('Unable to fetch leaderboard.');
    }
  };

  return (
    <div className="App">
      <h1>Number Guessing Game</h1>
      <input
        type="text"
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Enter your name"
      />
      <input
        type="number"
        value={guess}
        onChange={(e) => setGuess(e.target.value)}
        placeholder="Enter your guess"
      />
      <button onClick={handleGuess}>Submit Guess</button>
      <p>{message}</p>

      <button onClick={fetchHighScores}>View High Scores</button>
      <ul>
        {highScores.length > 0 ? (
          highScores.map((score, index) => (
            <li key={index}>{score.name}: {score.score}</li>
          ))
        ) : (
          <li>No scores available</li>
        )}
      </ul>
    </div>
  );
}

export default App;
