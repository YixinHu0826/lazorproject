# Introduction
In this assignment, our groups are going to  write a program that automatically finds solutions to the "Lazors'' game on Android and iPhone. It includes representing the game board and its elements, choosing a search algorithm, defining actions, implementing the logic to check for a solution and using GitHub to collaborate with group members.

## Lazors
The "Lazors" game is a puzzle game in which the objective is to manipulate blocks in order to guide laser beams to hit specific target points on a game board.  The game typically consists of a square grid-like board with different types of blocks, such as reflective blocks, opaque blocks, and refractive blocks, placed in various positions.

The laser beams are emitted from specific points on the board and travel in straight lines until they hit a block.  Reflective blocks change the direction of the laser beam, opaque blocks block the beam completely, and refractive blocks split the beam into multiple directions.  The goal is to strategically place and manipulate the blocks in order to ensure that the laser beams hit all the target points while obeying the rules of the game.

Block Types: The game incorporates different types of blocks, including reflective blocks, opaque blocks, and refractive blocks.  Each block type behaves in a specific way and affects the path of the laser beams differently. 
Grid-Based Layout: The game board is based on a grid-like layout, usually with a square shape.  The grid provides a structured environment where players must carefully place and adjust the blocks to create clear paths for the laser beams.  
Laser Behavior: The laser beams emitted from specific points on the grid travel in straight lines until they hit a block. Reflective blocks change the direction of the laser, opaque blocks block the laser completely, and refractive blocks split the laser beam into multiple paths.

# Methodology
## Read bff file 
Open the .bff file using the open() function, specifying the file path and the mode as "rb" (read binary).

Read the contents of the file using the read() function. 

Process the content of the .bff file according to its file structure and format. The specific steps will depend on the structure and purpose of the .bff file. 
## Classes identify
Block identify: A single Block class is identified by define the reflect, opaque and refract of the blocks 

Laser identify: The Laser class represents a laser beam in the game. It has attributes like position and direction and methods such as move to move the laser in the current direction and hit_target to check if it hits a target point.

Game board identify: The GameBoard class represents the game board itself. It has methods like place_block and remove_block to add or remove blocks from specific positions on the board, and check_solution to verify if the laser beams hit all target points and solve the level.

## Solve
Generate the board and grid for loop
Shoot laser by iterating through multiple laser steps
Check if solution is reached
While loop that repeats steps 2 & 3
Output results in graphical format

# File organization
All the codes were written in parts and assembled into the final file then, the file structure could be 
block,py
laser.py
board.py
solver.py
solution output.py
docstring.py
comments.py
tests.py
error.py

# Authors information
Yixin Hu
yhu134@jh.edu
https://github.com/YixinHu0826

Keng Zhang
kengzhang1998@gmail.com
https://github.com/kengzhang1998

Yuankun Li
yuankunli37@gmail.com
https://github.com/Yuankun12
