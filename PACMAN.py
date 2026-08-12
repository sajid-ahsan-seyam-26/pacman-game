import pygame
import sys
import random

pygame.init()



TILE = 28

COLS = 21
ROWS = 22

WIDTH = COLS * TILE
GAME_HEIGHT = ROWS * TILE

HEIGHT = GAME_HEIGHT + 70


screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "Easy Pac-Man Game"
)

clock = pygame.time.Clock()



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

YELLOW = (255, 220, 0)

BLUE = (30, 60, 220)

RED = (255, 50, 50)
PINK = (255, 120, 180)
CYAN = (0, 220, 255)
ORANGE = (255, 150, 30)

SCARED_BLUE = (40, 80, 255)



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


walls = []

dots = []

power_pellets = []

ghost_start_positions = []

player_start = (0, 0)

for row in range(len(level)):

    for col in range(len(level[row])):

        character = level[row][col]

        x = col * TILE
        y = row * TILE


        # WALL
        if character == "#":

            wall = pygame.Rect(
                x,
                y,
                TILE,
                TILE
            )

            walls.append(wall)


        # DOT
        if character == ".":

            dot = pygame.Rect(
                x + TILE // 2 - 3,
                y + TILE // 2 - 3,
                6,
                6
            )

            dots.append(dot)


        # POWER PELLET
        if character == "o":

            pellet = pygame.Rect(
                x + TILE // 2 - 7,
                y + TILE // 2 - 7,
                14,
                14
            )

            power_pellets.append(pellet)


        # PLAYER
        if character == "P":

            player_start = (
                x + 3,
                y + 3
            )


        # GHOST
        if character == "G":

            ghost_start_positions.append(
                (
                    x + 3,
                    y + 3
                )
            )



player = pygame.Rect(
    player_start[0],
    player_start[1],
    TILE - 6,
    TILE - 6
)

player_speed = 3


direction = "LEFT"

next_direction = "LEFT"



ghost_colors = [
    RED,
    PINK,
    CYAN,
    ORANGE
]


ghosts = []


for i in range(
    len(ghost_start_positions)
):

    ghost = {

        "rect": pygame.Rect(
            ghost_start_positions[i][0],
            ghost_start_positions[i][1],
            TILE - 6,
            TILE - 6
        ),

        "color": ghost_colors[i],

        "direction": random.choice(
            [
                "LEFT",
                "RIGHT",
                "UP",
                "DOWN"
            ]
        ),

        "start": ghost_start_positions[i]
    }

    ghosts.append(ghost)


ghost_speed = 2



score = 0

lives = 3



power_mode = False

power_end_time = 0



game_over = False

win = False



font = pygame.font.SysFont(
    "arial",
    25
)

big_font = pygame.font.SysFont(
    "arial",
    45,
    bold=True
)



def can_move(rect, move_direction, speed):

    test_rect = rect.copy()


    if move_direction == "LEFT":
        test_rect.x -= speed

    if move_direction == "RIGHT":
        test_rect.x += speed

    if move_direction == "UP":
        test_rect.y -= speed

    if move_direction == "DOWN":
        test_rect.y += speed


    for wall in walls:

        if test_rect.colliderect(wall):
            return False


    return True



def move_rect(rect, move_direction, speed):

    if move_direction == "LEFT":
        rect.x -= speed

    if move_direction == "RIGHT":
        rect.x += speed

    if move_direction == "UP":
        rect.y -= speed

    if move_direction == "DOWN":
        rect.y += speed



def reset_positions():

    global direction
    global next_direction


    player.x = player_start[0]
    player.y = player_start[1]

    direction = "LEFT"
    next_direction = "LEFT"


    for i in range(len(ghosts)):

        ghosts[i]["rect"].x = (
            ghosts[i]["start"][0]
        )

        ghosts[i]["rect"].y = (
            ghosts[i]["start"][1]
        )

        ghosts[i]["direction"] = (
            random.choice(
                [
                    "LEFT",
                    "RIGHT",
                    "UP",
                    "DOWN"
                ]
            )
        )



def draw_pacman():

    center = player.center

    radius = 11


    pygame.draw.circle(
        screen,
        YELLOW,
        center,
        radius
    )


    # Mouth
    if direction == "RIGHT":

        mouth = [
            center,
            (
                player.right + 3,
                player.centery - 7
            ),
            (
                player.right + 3,
                player.centery + 7
            )
        ]


    elif direction == "LEFT":

        mouth = [
            center,
            (
                player.left - 3,
                player.centery - 7
            ),
            (
                player.left - 3,
                player.centery + 7
            )
        ]


    elif direction == "UP":

        mouth = [
            center,
            (
                player.centerx - 7,
                player.top - 3
            ),
            (
                player.centerx + 7,
                player.top - 3
            )
        ]


    else:

        mouth = [
            center,
            (
                player.centerx - 7,
                player.bottom + 3
            ),
            (
                player.centerx + 7,
                player.bottom + 3
            )
        ]


    pygame.draw.polygon(
        screen,
        BLACK,
        mouth
    )


def draw_ghost(ghost):

    rect = ghost["rect"]


    if power_mode:

        ghost_color = SCARED_BLUE

    else:

        ghost_color = ghost["color"]


    # BODY
    pygame.draw.rect(
        screen,
        ghost_color,
        (
            rect.x,
            rect.y + 10,
            rect.width,
            rect.height - 10
        )
    )


    # HEAD
    pygame.draw.circle(
        screen,
        ghost_color,
        (
            rect.centerx,
            rect.y + 10
        ),
        rect.width // 2
    )


    # EYES
    pygame.draw.circle(
        screen,
        WHITE,
        (
            rect.x + 7,
            rect.y + 9
        ),
        4
    )

    pygame.draw.circle(
        screen,
        WHITE,
        (
            rect.x + 16,
            rect.y + 9
        ),
        4
    )


    # PUPILS
    pygame.draw.circle(
        screen,
        BLUE,
        (
            rect.x + 7,
            rect.y + 9
        ),
        2
    )

    pygame.draw.circle(
        screen,
        BLUE,
        (
            rect.x + 16,
            rect.y + 9
        ),
        2
    )


running = True


while running:

    clock.tick(60)


    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False


        if event.type == pygame.KEYDOWN:


            # UP
            if event.key == pygame.K_UP:

                next_direction = "UP"


            # DOWN
            if event.key == pygame.K_DOWN:

                next_direction = "DOWN"


            # LEFT
            if event.key == pygame.K_LEFT:

                next_direction = "LEFT"


            # RIGHT
            if event.key == pygame.K_RIGHT:

                next_direction = "RIGHT"


            # W
            if event.key == pygame.K_w:

                next_direction = "UP"


            # S
            if event.key == pygame.K_s:

                next_direction = "DOWN"


            # A
            if event.key == pygame.K_a:

                next_direction = "LEFT"


            # D
            if event.key == pygame.K_d:

                next_direction = "RIGHT"


            # -------------------------
            # RESTART GAME
            # -------------------------
            if event.key == pygame.K_r:

                if game_over or win:

                    walls.clear()
                    dots.clear()
                    power_pellets.clear()
                    ghost_start_positions.clear()


                    # Rebuild level
                    for row in range(
                        len(level)
                    ):

                        for col in range(
                            len(level[row])
                        ):

                            character = (
                                level[row][col]
                            )

                            x = col * TILE
                            y = row * TILE


                            if character == "#":

                                walls.append(
                                    pygame.Rect(
                                        x,
                                        y,
                                        TILE,
                                        TILE
                                    )
                                )


                            if character == ".":

                                dots.append(
                                    pygame.Rect(
                                        x + TILE // 2 - 3,
                                        y + TILE // 2 - 3,
                                        6,
                                        6
                                    )
                                )


                            if character == "o":

                                power_pellets.append(
                                    pygame.Rect(
                                        x + TILE // 2 - 7,
                                        y + TILE // 2 - 7,
                                        14,
                                        14
                                    )
                                )


                    score = 0

                    lives = 3

                    power_mode = False

                    game_over = False

                    win = False

                    reset_positions()



    if not game_over and not win:



        if can_move(
            player,
            next_direction,
            player_speed
        ):

            direction = next_direction



        if can_move(
            player,
            direction,
            player_speed
        ):

            move_rect(
                player,
                direction,
                player_speed
            )


 
        if player.right < 0:

            player.left = WIDTH


        if player.left > WIDTH:

            player.right = 0



        for dot in dots[:]:

            if player.colliderect(dot):

                dots.remove(dot)

                score += 10



        for pellet in power_pellets[:]:

            if player.colliderect(pellet):

                power_pellets.remove(
                    pellet
                )

                score += 50

                power_mode = True

                power_end_time = (
                    pygame.time.get_ticks()
                    + 6000
                )


 
        if power_mode:

            if (
                pygame.time.get_ticks()
                > power_end_time
            ):

                power_mode = False



        for ghost in ghosts:

            ghost_rect = ghost["rect"]

            ghost_direction = (
                ghost["direction"]
            )



            center_x = (
                ghost_rect.centerx
                % TILE
            )

            center_y = (
                ghost_rect.centery
                % TILE
            )


            near_center = (

                abs(
                    center_x
                    - TILE // 2
                ) <= ghost_speed

                and

                abs(
                    center_y
                    - TILE // 2
                ) <= ghost_speed
            )


 
            if (
                near_center
                or
                not can_move(
                    ghost_rect,
                    ghost_direction,
                    ghost_speed
                )
            ):

                possible = []


                for test_direction in [

                    "LEFT",
                    "RIGHT",
                    "UP",
                    "DOWN"

                ]:

                    if can_move(
                        ghost_rect,
                        test_direction,
                        ghost_speed
                    ):

                        possible.append(
                            test_direction
                        )


                opposite = {

                    "LEFT": "RIGHT",

                    "RIGHT": "LEFT",

                    "UP": "DOWN",

                    "DOWN": "UP"
                }


                if (
                    len(possible) > 1
                    and
                    opposite[
                        ghost_direction
                    ] in possible
                ):

                    possible.remove(
                        opposite[
                            ghost_direction
                        ]
                    )


                if len(possible) > 0:

                    ghost["direction"] = (
                        random.choice(
                            possible
                        )
                    )


            
            if can_move(
                ghost_rect,
                ghost["direction"],
                ghost_speed
            ):

                move_rect(
                    ghost_rect,
                    ghost["direction"],
                    ghost_speed
                )


            if ghost_rect.right < 0:

                ghost_rect.left = WIDTH


            if ghost_rect.left > WIDTH:

                ghost_rect.right = 0



        for ghost in ghosts:

            if player.colliderect(
                ghost["rect"]
            ):



                if power_mode:

                    score += 200


                    ghost["rect"].x = (
                        ghost["start"][0]
                    )

                    ghost["rect"].y = (
                        ghost["start"][1]
                    )


                else:

                    lives -= 1


                    if lives <= 0:

                        game_over = True


                    else:

                        reset_positions()


                    break


   
        if (
            len(dots) == 0
            and
            len(power_pellets) == 0
        ):

            win = True


    screen.fill(BLACK)

    for wall in walls:

        pygame.draw.rect(
            screen,
            BLUE,
            wall,
            3
        )

    for dot in dots:

        pygame.draw.circle(
            screen,
            WHITE,
            dot.center,
            3
        )

    for pellet in power_pellets:

        pygame.draw.circle(
            screen,
            WHITE,
            pellet.center,
            7
        )

    draw_pacman()

    for ghost in ghosts:

        draw_ghost(ghost)

    score_text = font.render(
        "SCORE: " + str(score),
        True,
        WHITE
    )

    screen.blit(
        score_text,
        (20, GAME_HEIGHT + 15)
    )

    lives_text = font.render(
        "LIVES: " + str(lives),
        True,
        WHITE
    )

    screen.blit(
        lives_text,
        (220, GAME_HEIGHT + 15)
    )

    if power_mode:

        power_text = font.render(
            "POWER!",
            True,
            CYAN
        )

        screen.blit(
            power_text,
            (430, GAME_HEIGHT + 15)
        )

    if game_over:

        game_over_text = big_font.render(
            "GAME OVER",
            True,
            RED
        )

        screen.blit(
            game_over_text,
            (
                WIDTH // 2
                - game_over_text.get_width() // 2,

                HEIGHT // 2 - 40
            )
        )


        restart_text = font.render(
            "Press R to Restart",
            True,
            WHITE
        )

        screen.blit(
            restart_text,
            (
                WIDTH // 2
                - restart_text.get_width() // 2,

                HEIGHT // 2 + 20
            )
        )

    if win:

        win_text = big_font.render(
            "YOU WIN!",
            True,
            YELLOW
        )

        screen.blit(
            win_text,
            (
                WIDTH // 2
                - win_text.get_width() // 2,

                HEIGHT // 2 - 40
            )
        )


        restart_text = font.render(
            "Press R to Play Again",
            True,
            WHITE
        )

        screen.blit(
            restart_text,
            (
                WIDTH // 2
                - restart_text.get_width() // 2,

                HEIGHT // 2 + 20
            )
        )



    pygame.display.update()


pygame.quit()

sys.exit()
