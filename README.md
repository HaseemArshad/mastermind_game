# Mastermind Game

A Python implementation of the classic **Mastermind** game where players guess a secret color code within a limited number of tries. This version includes added features such as hints and the ability to give up.

## Features

- **Classic Gameplay**: Guess the correct sequence of colors within a set number of tries.
- **Customizable**: Adjust the number of tries, code length, and available colors in the game.
- **Hint Option**: Players can request a hint to reveal one of the colors in the code.
- **Give Up Option**: Players can give up and see the solution at any time.

## How to Play

1. The game randomly generates a secret color code of 4 colors (default).
2. Players have 10 attempts to guess the code.
3. Enter your guess as 4 space-separated colors (e.g., `R G B Y`).
4. After each guess, the game provides feedback:
   - `Correct Positions`: Number of colors in the correct position.
   - `Incorrect Positions`: Number of correct colors in the wrong position.
5. You can type:
   - **`HINT`**: Get a hint revealing one color in the code.
   - **`GIVE UP`**: End the game and reveal the code.

### Example Gameplay:
Welcome to Mastermind! You have 10 tries to guess the code.
The valid colors are: R G B Y W O

Guess (or type 'GIVE UP' to quit, 'HINT' for help): R G B Y
Correct Positions: 2 | Incorrect Positions: 1

Guess (or type 'GIVE UP' to quit, 'HINT' for help): HINT
Hint: One of the colors in the code is B.

Guess (or type 'GIVE UP' to quit, 'HINT' for help): GIVE UP
You gave up! The code was: B Y G O

###Requirements

- Python 3.x

## How to Run

1. Clone the repository:
2. Run the game
