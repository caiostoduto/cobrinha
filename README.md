# Cobrinha
#### Video Demo:  https://youtu.be/tAhvhnIRTkA
#### Description:

A Player vs. Player Pygame (a Python library for creating games) implementation of the original Snake Game ('Jogo da Cobrinha' in Portuguese), popularized by Nokia on its mobile phones in 1998.

## Summary
- [❤️ Inspiration](#-Inspiration)
- [📲 Tech used](#-Tech-used)
- [🐍 Objective](#-Objective)
- [🤓 Install](#-install)
- [😎 How to run](#-how-to-run)
- [🥳 How to play](#-how-to-play)
- [🥸 Why?](#-why)

## ❤️ Inspiration

I was inspired to create Cobrinha by the legacy of the Snake Game, which continues to evoke nostalgia among those who played it as teenagers or children. The Snake Game was an immensely fun and memorable game, particularly because it came pre-installed on thousands of Nokia mobile phones starting in 1998. Originally, it was a single-player survival game with the objective of accumulating as much food as possible to increase your score, all while avoiding collisions with yourself or the game's borders. As the snake grew longer with each meal, the available space for movement decreased, making the game progressively more challenging.

Nowadays, since the original game has not been ported to modern hardware, there are dozens, if not hundreds, of different versions of the game. As an example, Google's game titled 'Snake' shares the same basic mechanics as the original game but adds various visual features. There is also a famous game inspired by the Snake Game and Agar.io, called 'Slither.io,' which features a different style of gameplay, involving multiplayer competition against online players.

## 📲 Tech used

- I used [Miniconda](https://docs.conda.io/en/latest/miniconda.html), one of [Anaconda](https://www.anaconda.com/)'s products, to create a Python 3.11.4 environment, as it helps organize different dependencies in various projects.
- The main, and only, library I used in this project was Pygame, as it was implemented in one of the CS50AI problem sets, and I wanted to become familiar with it since I had never developed any kind of game before.
- As an editor, I used VS Code, an open-source IDE maintained by Microsoft and used in CS50X and GitHub's Codespace.

## 🐍 Objective

Cobrinha's objective is to defeat your opponent by making the opponent's snake hit the side of your snake. There are food blocks that the player can consume to make its snake longer, so it may be a strategy to help defeat the oponnent. To play it, use WASD, player0, or arrow keys, player1.

## 🤓 Install

To install all requirements, you need Python3. To check your Python's version, use:
```bash
python -v
```

You can install all the requirements, mainly [Pygame](https://www.pygame.org/), by using the following command:
```bash
python -m pip install -r requirements.txt
```

## 😎 How to run
To run, simply use the following command:
```bash
python runner.py
```

## 🥳 How to play
- Use the WASD keys to move player0;
- Use the arrow keys to move player1;
- Try to eat as much food as possible not hitting the borders or any snake body;
- Use your snake's body to corner your opponent;
- Have fun!!

## 🥸 Why?
[Harvard CS50X](https://cs50.harvard.edu/x/) Final Project.
