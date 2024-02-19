# Turtle_crossing game

This is a simple Turtle Crossing game implemented in Python, primarily using the tkinter module for the graphical interface.

The objective of the game is to guide the turtle player from the bottom to the top of the screen without colliding with the moving cars. Each successful crossing increases the game level and speeds up the vehicles.

The game consists of four main Python files:

**player.py:** This file defines the turtle player and handles its movement when buttons are pressed.

**car_manager.py:** Responsible for generating a randomized pattern of colorful rectangles on the right side of the player interface and moving them along the x-axis to simulate moving cars.

**scoreboard.py:** Keeps track of the current game level and updates the scoreboard accordingly.

**main.py:** The main file where all other files are connected. It controls the game's functionality, timings, and functions.
