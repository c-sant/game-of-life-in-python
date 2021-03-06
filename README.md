# The Game of Life in Python

<div>
  <img src="https://media.giphy.com/media/rMQOU5VHWbYOlemnIU/giphy.gif"/>
</div>

> An implementation of Conway's Game of Life in Python.

## The Game of Life

Devised by the British mathematician John Horton Conway in 1970, The Game of Life, or simply Life, is a "zero-player game" where the game keeps
playing by itself ad infinitum. Following a set of few and simple rules, the board keeps updating alone, creating new scenarios every update.
The player only sets the initial scenario just so Life can continue.

## :grey_question: How it works

There is a board that works as a 2D grid of cells. Each cell can be either dead or alive, and this state may or may not change every time the game
updates. For each update, the game evalutes a few rules for each cell:

- 1: if a dead cell has no living neighbours, it stays dead.
- 2: if a living cell has less than 2 living neighbours, it dies of "underpopulation".
- 3: if a living cell has more than 3 living neighbours, it dies of "overpopulation".
- 4: if a dead cell has exactly 3 living neighbours, it becomes alive out of "reproduction".

Each cell has at least 3 and at most 8 neighbours, and their fate in the next "age" depends on the disposition of the "current age".

<div align="center">
  <img src="https://i.imgur.com/TcIsyTX.png"/>
</div>

### Controls

- ``Left mouse click``: "spawns" (i.e. gives life to) clicked cell.
- ``Right mouse click``: "kills" clicked cell.
- ``T``: toggle colors.
- ``R``: reset board (kill all cells).
- ``Up``: increase game speed.
- ``Down``: decrease game speed.
- ``Space bar``: starts/stops the game. 

### The Python Implementation

There are two classes: ``Cell`` and ``Board``. Each cell stores its ``x`` and ``y`` coordinates, as well as its state. The state is 
represented by a property called ``alive``, which can be either **True** or **False**. Cells also store the coordinates of all of its 
neighbours, just so it can evaluate the game rules every update. Should its state change, the ``toggle`` function is called.

The ``Board`` is composed by cells and works as a list of lists of cells to emulate a 2D array in Python. When instantiated, the Board object
receives two values: ``rows`` and ``columns``, each representing the size of its axis in the board. It then creates a completely dead board
in the specified dimensions. 

It is possible to create custom boards by using the ``generate`` function. Once created, the Board object can call the function, receiving the
new board as a list of lists of integers that can be either 0 (dead) or 1 (alive). Based on that, a new Board with real Cell objects is going to
be generated.

One can also get/set values to the Board elements by using its row and column coordinates as: board_instance[row, column].

Finally, the Board's ``update`` method toggles every cell according to the game rules.

### The Visual Implementation

For the visual game I used Pygame and there are two new classes: ``VisualBoard`` and ``VisualCell``, each inheriting their non-graphical equivalent.

The ``Visual Board`` has a new ``render`` method which draws every cell into the Pygame window. Besides the graphic part, the Board is still a Python 
list of lists essentially. There is also the ``get_cell`` method, which returns the cell in the grid according to its coordinates in order to manipulate 
it once it gets clicked. 

The ``update`` method also has a new parameter: ``speed``. This value represents the amount of seconds the game is going to take to update the board.

The ``Visual Cell``'s method ``draw`` is called to draw it on the screen. The ``toggle`` method also sets the color corresponding to the cell state, in
order to reflect the change in the graphic board.

To run the visual game, all you have to do is import the ``run`` function from visual_life.py and execute it. A 480x480 screen will show up. The default
board has 48x48 cells. Since the goal of the project is mainly personal improvement with the Python language, there is not much customization of the game,
besides swapping the game colors by pressing ``T`` on the keyboard.

## Example:

The following is an example of the non-visual game:

```
from life import Board # life.py

b = Board(0, 0) # initialized an empty Board

my_pattern = [
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 1, 1, 1, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0]
]

b.generate(my_pattern)

print(b)

print('\n---------\n')

b.update()

print(b)
```

The output should be:

```
0 0 0 0 0
0 0 0 0 0
0 1 1 1 0
0 0 0 0 0
0 0 0 0 0

---------

0 0 0 0 0
0 0 1 0 0
0 0 1 0 0
0 0 1 0 0
0 0 0 0 0
```

To run the game, you just need the following code:

```
import visual_life # visual_life.py

visual_life.run()
```


## ???? Requirements

The following setup was used to make the source code on this repository:

* Windows 10
* Python 3.8.10
* Pygame
