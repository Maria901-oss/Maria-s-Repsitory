# Number Guessing Game with Attractive Interface

## Description
This project is a number guessing game with a React.js frontend, Flask backend, and a separate leaderboard service. The backend handles game logic, and the leaderboard service manages high scores stored in an SQLite database. The application is containerized using Docker.

## Setup Instructions
1. Ensure Docker and Docker Compose are installed on your system.
2. Clone the repository.
3. Navigate to the project directory.
4. Run `docker-compose up --build` to build and start all services.

## Accessing the Application
- Open the frontend in your browser at `http://localhost:7002`.
- Play the game and view high scores.

## Notes
- Ensure ports 7000, 7001, and 7002 are available on your system.
