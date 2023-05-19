![Snake (1)](https://github.com/Ahmedabbas75/AI-Project/assets/119451645/afb825e5-f9d1-4a06-87ca-8e3fe12edecb)


# Snake Game 
The player controls a long, thin creature, resembling a snake, which roams around on a bordered plane, picking up food (or some other item), trying to avoid hitting its own tail or the edges of the playing area. Each time the snake eats a piece of food, its tail grows longer, making the game increasingly difficult

# Characteristics
### The following are some basic rules followed by our implementation:
1. Goal - the snake tries to eat as many apples as possible, within ﬁnite steps.
The ﬁrst priority for the snake is to not colliding itself while the second is to increase the score.

2. There are four possible directions the snake can move: left, right, up and down
However, because of the placement of its tail some directions may not be available.
The most clear example is that the snake can never swap to an opposite direction i.e. left to right, up to down, etc.

3. The snake grows by one unit when eating an food.
The growth is immediately reﬂected by the gained length of the tail, i.e. the tip of the tail occupies the square on which the apple was.

4. The board size is ﬁxed to square.

5. After an food is eaten by the snake, another food is placed randomly with uniform probability on one available squares of the board.

# Game Flow-chart
<img src='resources/Snake game state.png'/>

# Requirements
1. Python.
2. Pygame.
3. Numpy. 
4. PyQt5.

# How to execute game
- MainWindow Run the Game.

![main window](https://github.com/Ahmedabbas75/AI-Project/assets/119451645/4adaa350-9d8d-4f78-aebd-5096792a2661)

# Some screen 

<p float="left">
  <img src='resources/screen 3.png' width='400'/>
  <img src='resources/screen 1.png' width='400'/>
  <img src='resources/screen 2.png' width='400', height="415px"/>
  <img src='resources/screen 4.png' width='400'/>
</p>

# Why this Project

#### Project done under supervision of  Prof. [@Sara El-Metwally](https://github.com/SaraEl-Metwally) by :

[@Ahmed Mohmmed abbas](https://github.com/Ahmedabbas75) | section 2






