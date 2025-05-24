import pygame
import snake
import food
import config
import render


class GameLogic:
    """
    Main class to manage the game logic, including initialization, event handling,
    rendering, and the game loop.
    """

    def __init__(self):
        """
        Initializes the game by setting up the screen, clock, and game objects 
        like the snake and food.
        """
        pygame.init()  # Initialize Pygame modules
        self.clock = pygame.time.Clock()  # Create a clock object to control frame rate
        self.screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))  # Create the game window
        pygame.display.set_caption("Snake Game")  # Set the game window title

        # Initialize the Render object to handle all drawing
        self.render = render.Render(self.screen)

        # Create a Snake object
        self.snake = snake.Snake(
            config.COLORS["snake_color"],  # Snake color
            config.BLOCK_SIZE,            # Snake block size
            config.WIDTH,                 # Screen width
            config.HEIGHT,                # Screen height
            config.WIDTH // 2,            # Snake's initial x-coordinate
            config.HEIGHT // 2,           # Snake's initial y-coordinate
            direction="right",            # Snake's initial direction
        )

        # Create a Food object
        self.food = food.Food(
            config.COLORS["food_color"],  # Food color
            config.BLOCK_SIZE,            # Food block size
            self.snake.snake_blocks,      # Snake's blocks (to avoid overlapping with food)
            config.WIDTH,                 # Screen width
            config.HEIGHT,                # Screen height
        )

        # Game loop running flag
        self.running = True

    def run(self):
        """
        Main game loop. Handles:
        - Event processing (keyboard inputs, quitting the game)
        - Game logic updates (snake movement, food collision, wall collision)
        - Rendering all game objects and updating the screen.
        """
        while self.running:
            # Handle user inputs and events
            self.handle_events()

            # Draw the background
            self.render.draw_background()

            # Move the snake
            self.snake.snake_move()


            # Check if the snake eats food
            if self.ate_food():
                config.SCORE += 1  # Increment the score
                # Generate a new food position
                self.food.position = self.food.generate_food(
                    config.BLOCK_SIZE,
                    self.snake.snake_blocks,
                    config.WIDTH,
                    config.HEIGHT,
                )
            else:
                self.snake.remove_tail()  # Remove the snake's tail if no food is eaten



            # Check for collisions (walls or snake itself)
            if self.collide():
                self.render.draw_game_over()  # Display "Game Over"
                pygame.display.flip()       # Update the screen with the "Game Over" text
                pygame.time.wait(2000)      # Wait 2 seconds before quitting
                self.running = False        # End the game loop


            # Render all game elements
            self.render.draw_snake(self.snake)  # Draw the snake
            self.render.draw_food(self.food)    # Draw the food
            self.render.draw_score(config.SCORE)  # Display the current score


            # Update the screen with the rendered elements
            pygame.display.flip()
            # Control the frame rate
            self.clock.tick(config.SPEED)

        pygame.quit()  # Quit Pygame when the game loop ends

    def handle_events(self):
        """
        Process user input events, including quitting the game and controlling the snake.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False  # Quit the game if the window is closed
            elif event.type == pygame.KEYDOWN:
                self.handle_key_press(event.key)  # Handle keyboard input

    def handle_key_press(self, key):
        """
        Change the snake's direction based on user keyboard input.
        Prevents the snake from reversing directly into itself.
        """
        if key == pygame.K_UP and self.snake.direction != "down":
            self.snake.direction = "up"
        elif key == pygame.K_DOWN and self.snake.direction != "up":
            self.snake.direction = "down"
        elif key == pygame.K_RIGHT and self.snake.direction != "left":
            self.snake.direction = "right"
        elif key == pygame.K_LEFT and self.snake.direction != "right":
            self.snake.direction = "left"



    def ate_food(self):
        """
        Check if the snake's head is at the same position as the food.
        Returns:
            bool: True if the snake eats the food.
        """
        # Check if the snake's head matches the food's position
        if self.snake.head == self.food.position:
            return True



    def collide(self):
        """
        Check if the snake collides with:
        - The screen boundaries
        - Itself
        Returns:
            bool: True if a collision is detected
        """
        # Check if the snake's head is outside the screen or intersects its body
        if (
            self.snake.head[0] < 0  # Hits the left wall
            or self.snake.head[0] >= config.WIDTH - config.BLOCK_SIZE  # Hits the right wall
            or self.snake.head[1] < 0  # Hits the top wall
            or self.snake.head[1] >= config.HEIGHT - config.BLOCK_SIZE  # Hits the bottom wall
            or self.snake.head in self.snake.snake_blocks[1:]  # Collides with itself
        ):
            return True