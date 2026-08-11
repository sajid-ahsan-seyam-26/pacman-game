import pygame
import sys
import random
pygame.init()

#Gmae setting
TILE=28
COLS=21
ROWS=22

WIDTH=COLS*TILE
GAME_HEIGHT=ROWS* TILE
HEIGHT=GAME_HEIGHT+70
screen=pygame.display.set_mode(
    (WIDTH,HEIGHT)
)
screen=pygame.display.set_mode(
    "EASY PACKMAN GAME"
)
CLOCK=pygame.time.Clock()

#color

BLACK=(0,0,0)
WHITE=(255,255,255)
YELLOW=(255,220,0)
BLUE=(30,60,220)
RED=(255,5,50)
PINK=(255,120,180)
CYAN=(0,220,255)
ORANGE=(255,150,30)
SCARED_BLUE=(40,80,255)


#MAZE

level = [

    "#####################",
    "#.........#.........#",
    "#.###.###.#.###.###.#",
    "#o###.###.#.###.###o#",
    "#...................#",
    "#.###.#.#####.#.###.#",
    "#.....#...#...#.....#",
    "#####.### # ###.#####",
    "    #.#       #.#    ",
    "#####.# ##G## #.#####",
    "     .  #GGG#  .     ",
    "#####.# ##### #.#####",
    "    #.#       #.#    ",
    "#####.# ##### #.#####",
    "#.........#.........#",
    "#.###.###.#.###.###.#",
    "#o..#.....P.....#..o#",
    "###.#.#.#####.#.#.###",
    "#.....#...#...#.....#",
    "#.#######.#.#######.#",
    "#...................#",
    "#####################"

]
#game object 
for row in range (len(level)):
    for col in range(len(level[row])):
        character=level[row][col]
        x=col*TILE
        Y=col*TILE

        #wall
        if character =="#":
            wall=pygame.Rect(
                 x,
                y,
                TILE,
                TILE
            )
            walls.append(wall)



