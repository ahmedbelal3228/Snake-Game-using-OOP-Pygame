## 🐍 Snake Game using OOP

A classic Snake Game built with Python and Pygame, structured using Object-Oriented Programming (OOP). The game logic is cleanly separated into multiple files and classes, making the codebase modular, readable, and easy to extend.

---

### 🎯 Key Highlights

* Built with OOP principles: encapsulation, responsibility separation
* Split across multiple well-organized files (snake, food, rendering, logic)
* Easy to update and scale with new features

---

### 📁 Project Structure

```
.
├── main.py            # Entry point for the game
├── config.py          # Centralized configuration (colors, screen size, speed)
├── game_logic.py      # Main game loop, input handling, collision logic
├── snake.py           # Snake class: handles movement and block management
├── food.py            # Food class: generates valid food positions
├── render.py          # Render class: draws game elements on the screen
```

This modular design follows the Single Responsibility Principle, making each file/class responsible for a distinct part of the game.

---

### 🎮 Features

* Snake grows after eating food
* Random food generation avoiding overlap
* Wall and self collision detection
* Score tracking
* Game over screen
* Clean, object-oriented structure

---

### 🛠️ Installation & Running

#### Requirements

* Python 3.x
* Pygame

#### Setup

```bash
pip install pygame
```

#### Run

```bash
python main.py
```

---

### 🚀 Ideas for Future Improvements

* Add levels, obstacles, or power-ups
* Sound effects and music
* Game pause/restart functionality
* Save and display high scores
