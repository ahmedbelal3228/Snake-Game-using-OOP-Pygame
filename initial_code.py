"""
WINDOW PART : 
    1 -Importing PYGAME 
    2- Initialize pygame 
    3- Setting the window height and width
    4- Setting the window title 
    5- Creating a loop to open the window unitll quit
    6- Choosing the colors of the element and set it as variables
    

DISPLAYING AND MOVING THE SNAKE  : 
    1- Making a list consist of 3 bolcks (the snake's head , body and tail)
    2- Give the snake initail position when the game starts 
    3- Conroling the movement of the snake when press the keys 
    4- Making the snake move by adding new_head with the new coordinates and remove the tail .

THE FOOD : 
    1- Creating the food block (the same size as the snake block)
    2- Initial position of the food
        - Appears in random postion but with condition : 
            1- Be within the screen boundaries
            2- Not overlap with the snake's current position.
            3- Disappear when the snake touch it 
            4- Appears again in random position with the same conditions
COLLISION DETECTION:
    1- The snake eats the foof -> the snake grow
    2- The snake hits any border of the screen -> game over

DISPALY 
    1- Display the score on the screen 
    2- Display game over when lose
"""

import pygame
import random

pygame.init()
# creating a clock object to set the speed of the game
clock = pygame.time.Clock()

# ======================== CONSTANT VARIABLES  ========================
# Colors
background_color = "#212f49"  # Dark Blue
snake_color = "#4caf50"  # Green
food_color = "#e9633a"  # Orange
score_color = "#ffffff"  # White
game_over_color = "#ffffff"
# Size
height = 480
width = 640
# Snake -> 3 blocks | Food -> 1 block
block_size = 10
# Initial speed
speed = 10
# Initial score
score = 0

# SNAEKE'S BLOCK POSITION
initial_x = width // 2
initial_y = height // 2

# defining the snake by its blocks
snake = [
    (initial_x, initial_y),  # first block
    (initial_x - 10, initial_y),  # second block
    (initial_x - 20, initial_y),  # third block
]

# setting the initial direction of the snake (when the game starts)
direction = "right"


# FOOD
# Food Positioning
# Generating the food so that it doesn't overlap with the snake's position
def generate_food(snake, width, height, block_size):

    while True:
        # The link below to the explanation for food block positioning logic of the (x,y):
        # https://drive.google.com/file/d/1BCGK4u8qW1rExSRf_pgoykjrp7FNKwwb/view?usp=sharing
        food_x = random.randint(0, (width - block_size) // block_size) * block_size
        food_y = random.randint(0, (height - block_size) // block_size) * block_size
        if (food_x, food_y) not in snake:
            return food_x, food_y


# Assigning the food x and y from the function (making them global to pass to the draw.rect)
food_x, food_y = generate_food(snake, width, height, block_size)


# =======================================================================


# setting the height and width
screen = pygame.display.set_mode((width, height))  # 640 -> width , 480 -> height
title = pygame.display.set_caption("Snake Game")

# The running trigger (to determine to display to window or quit)
running = True

# The game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Controllong The Snake Movement
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "down":
                direction = "up"
            elif event.key == pygame.K_DOWN and direction != "up":
                direction = "down"
            elif event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"
            elif event.key == pygame.K_LEFT and direction != "right":
                direction = "left"

    # moving the snake
    head = snake[0]  # snake[0][0] -> x | snake[0][1] -> y
    if direction == "up":
        new_head = (head[0], head[1] - block_size)
    elif direction == "down":
        new_head = (head[0], head[1] + block_size)
    elif direction == "right":
        new_head = (head[0] + block_size, head[1])
    elif direction == "left":
        new_head = (head[0] - block_size, head[1])
    # Add the new head to the front of the snake
    snake.insert(0, new_head)

    # Wheen the snake eats the food
    if snake[0] == (food_x, food_y):
        score += 1  # Adding one to the score
        food_x, food_y = generate_food(snake, width, height, block_size)
    # the snake moving normally (no collision)
    else:
        # removing the tail
        snake.pop()

    if (
        snake[0][0] < 0
        or snake[0][0] >= width - block_size
        or snake[0][1] < 0
        or snake[0][1] >= height - block_size
        or snake[0] in snake[1:]
    ):
        running = False
    # filling the screen with a color
    screen.fill(background_color)

    # Drawing the objects
    for x, y in snake:
        pygame.draw.rect(screen, snake_color, [x, y, block_size, block_size])

    pygame.draw.rect(screen, food_color, [food_x, food_y, block_size, block_size])

    # Displaying the score
    score_font = pygame.font.Font(None, 20)
    text = score_font.render(f"Score: {str(score)}", True, score_color)
    screen.blit(text, (10, 10))

    # Displaying the Game Over message
    if not running : 
        game_over_font = pygame.font.Font(None, 35)
        text = game_over_font.render("Game Over" , True ,game_over_color )
        screen.blit(text ,( width//2 - text.get_width() //2 , height//2 - text.get_height()//2))
        pygame.display.flip()
        pygame.time.wait(2000)

    # putting all the setup i˜nto work
    pygame.display.flip()
    # setting the game's speed by controlling the time delay before the next frame update
    clock.tick(speed)

pygame.quit()
