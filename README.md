# Tic Tac Toe Game

This project is a simple implementation of the classic Tic Tac Toe game using Python and the Pygame library. It uses MiniMax algorithm in a way that you can never win, either the computer wins, or it's a Tie. It includes the game logic module, a testing module, and a runner script to start the game.
- Video link: https://mega.nz/folder/jtUjTCrL#6I74bg9fwaRecLkDTxzNzg/file/Cglj3TyC
## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Modules](#modules)
  - [tictactoe.py](#tictactoepy)
  - [pytesting.py](#pytestingpy)
  - [runner.py](#runnerpy)
- [Requirements](#requirements)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/benwhoiam/TicTacToe-using-Minimax-algorithm.git
   cd tictactoe
   ```
2. Install the required dependencies:
  ```bash
    pip install -r requirements.txt
  ```
## Usage
To start the Tic Tac Toe game, run the following command:
  ```bash
  python runner.py
  ```
## Project Structure
- `tictactoe.py`: Contains the game logic for Tic Tac Toe.
- `pytesting.py`: Includes unit tests for the game logic.
- `runner.py`: The main script to run the game.
- `requirements.txt`: Lists the dependencies required to run the project.
## Modules
### tictactoe.py
This module includes the core functionality of the Tic Tac Toe game:
- Setting up the game board.
- Handling player moves.
- Checking for win conditions.
- Displaying the game status.
### pytesting.py
This module contains unit tests to ensure the correctness of the game logic implemented in tictactoe.py.
### runner.py
This script initializes the game and runs the main game loop. It uses the Pygame library to handle the game interface and user interactions.

## Requirements
The project depends on the following packages:
-pygame
You can find all dependencies listed in the requirements.txt file.


## Side Note:
I wrote this file using the aide of AI:
- ChatGPT
- OpenAI
- [Website](https://www.openai.com)
