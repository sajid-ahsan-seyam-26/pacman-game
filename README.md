# pacman-game

# pacman-game
# 🎮 Easy Pac-Man Game

A simple **Pac-Man-style maze game** built with **Python and Pygame**.

The player controls Pac-Man, collects dots and power pellets, avoids ghosts, and tries to clear the entire maze. The project is designed as a beginner-friendly introduction to **2D game development with Pygame**.

## 🕹️ Game Features

* 🟡 Pac-Man player character
* 👻 Four colorful ghosts
* 🧱 Maze-based level design
* ⚪ Collectible dots
* 🔵 Power pellets
* ⚡ Temporary Power Mode
* ❤️ 3 player lives
* 🏆 Score system
* 💥 Ghost collision system
* 🔄 Restart functionality
* 🎉 Win and Game Over screens
* 🎯 Ghosts move using random direction selection
* 🔁 Screen wrap-around on the left and right sides
* ⌨️ Arrow key and WASD controls
* 🖥️ 60 FPS gameplay

## 🛠️ Technologies Used

* **Python**
* **Pygame**
* **Random module**
* **Sys module**

The game initializes Pygame and uses a tile-based maze system with a tile size of 28 pixels.

## 🎯 How to Play

Your objective is simple:

> **Collect all the dots and power pellets while avoiding the ghosts.**

### Scoring

| Item                                | Points |
| ----------------------------------- | -----: |
| ⚪ Dot                               |    +10 |
| 🔵 Power Pellet                     |    +50 |
| 👻 Ghost while Power Mode is active |   +200 |

Power pellets activate **Power Mode for approximately 6 seconds**, allowing Pac-Man to defeat ghosts.

## ⌨️ Controls

| Key            | Action                      |
| -------------- | --------------------------- |
| ⬆️ Arrow Up    | Move Up                     |
| ⬇️ Arrow Down  | Move Down                   |
| ⬅️ Arrow Left  | Move Left                   |
| ➡️ Arrow Right | Move Right                  |
| W              | Move Up                     |
| S              | Move Down                   |
| A              | Move Left                   |
| D              | Move Right                  |
| R              | Restart after Win/Game Over |

The game supports both **Arrow keys and WASD** for movement.

## 💙 Power Mode

When Pac-Man collects a power pellet:

* Power Mode becomes active.
* Ghosts turn blue.
* Pac-Man can defeat ghosts.
* Defeating a ghost awards **200 points**.
* Power Mode lasts around **6 seconds**.

## 👻 Ghost System

The game contains four ghosts with different colors:

* 🔴 Red
* 🩷 Pink
* 🩵 Cyan
* 🟠 Orange

Ghosts choose possible movement directions randomly while avoiding walls. They also avoid immediately reversing direction when multiple movement options are available.

## ❤️ Lives & Game Over

The player starts with **3 lives**.

If Pac-Man touches a ghost:

* Without Power Mode → loses one life.
* With Power Mode → defeats the ghost and gains 200 points.

When all lives are lost, the game displays **GAME OVER**.

## 🏆 Winning the Game

You win when all dots and power pellets have been collected.

The game checks:

```python
if len(dots) == 0 and len(power_pellets) == 0:
    win = True
```

After winning, you can press **R** to play again.

## 📂 Project Structure

```text
Easy-Pac-Man-Game/
│
├── pacman.py
└── README.md
```

> You can rename `pacman.py` to whatever filename you use for the Python game.

## 🚀 Installation

### 1. Install Python

Make sure Python is installed on your computer.

Check your Python version:

```bash
python --version
```

### 2. Install Pygame

```bash
pip install pygame
```

### 3. Clone the Repository

```bash

```

### 4. Enter the Project Folder

```bash
cd easy-pacman-game
```

### 5. Run the Game

```bash
python pacman.py
```

## 🧩 How the Game Works

The maze is represented using characters:

```text
# = Wall
. = Dot
o = Power Pellet
P = Player
G = Ghost
```

The game reads the maze row by row and converts each character into the corresponding game object.

For example:

```text
#####################
#.........#.........#
#.###.###.#.###.###.#
#o..#.....P.....#..o#
#.....#...#...#.....#
#...................#
#####################
```

## 🧠 Main Programming Concepts

This project demonstrates several important Python and game-development concepts:

* Variables
* Lists
* Dictionaries
* Functions
* Loops
* Conditional statements
* Event handling
* Collision detection
* Object positioning
* Random movement
* Game states
* Keyboard input
* Pygame rectangles
* Drawing shapes
* Game loop
* Frame-rate control

The game uses `pygame.Rect` objects for the player, walls, dots, pellets, and ghosts, making collision detection easier.

## 🔧 Future Improvements

Possible features that could be added in future versions:

* 🎵 Background music and sound effects
* 🧠 Smarter ghost AI
* 🗺️ Multiple levels
* 🏅 High-score system
* 💾 Save/load game progress
* ⏱️ Timer system
* 🍒 Bonus fruits
* 👻 Different ghost behaviors
* 🎨 Improved graphics and animations
* 📱 Better UI
* 🎮 Controller support
* 🚪 More advanced Pac-Man tunnel behavior

## 📸 Screenshots





```text
Easy-Pac-Man-Game/
│
├── pacman.py
├── README.md
└── screenshots/
    └── game.png
```

## 📚 Learning Purpose

This project was created as a beginner-friendly **2D game development project using Pygame**.

It is useful for learning:

> **Python → Pygame → Game Loop → Collision Detection → Player Movement → Enemy AI → Game States**

## 👨‍💻 Author

**Sajid Ahsan Seyam**

Computer Science & Engineering Student
Bangladesh

## ⭐ Support

If you like this project, consider giving the repository a ⭐ on GitHub!

---

### 🎮 Enjoy the game and collect them all! 🟡👻
