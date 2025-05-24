import config
import pygame


class Render:
    """
    A class responsible for rendering all game elements on the screen,
    including the background, snake, food, score, and game-over message.
    """

    def __init__(self, screen):
        """
        Initialize the Render class with the game screen and related attributes.
        
        Args:
            screen (pygame.Surface): The game screen where elements will be drawn.
        """
        self.screen = screen  # The game screen to draw on
        
        # Colors for game elements, loaded from the config module
        self.background_color = config.COLORS["background_color"]  # Background color
        self.snake_color = config.COLORS["snake_color"]  # Snake color
        self.food_color = config.COLORS["food_color"]  # Food color
        self.game_over_color = config.COLORS["game_over_color"]  # "Game Over" text color
        self.score_color = config.COLORS["score_color"]  # Score text color
        
        # Font sizes for rendering text
        self.font_size = config.FONT_SIZE  # Font size for displaying the score
        self.game_over_font_size = config.GAME_OVER_FONT_SIZE  # Font size for "Game Over"
        
        # Pygame font objects
        self.font = pygame.font.Font(None, self.font_size)  # Font for displaying the score
        
        # Block size for snake and food (from config)
        self.block_size = config.BLOCK_SIZE

    def draw_background(self):
        """
        Draw the background of the game.
        Fills the entire screen with the background color.
        """
        self.screen.fill(self.background_color)  # Fill the screen with the background color

    def draw_snake(self, snake):
        """
        Draw the snake on the screen.

        Args:
            snake (Snake): The Snake object containing the list of blocks to draw.
        """

        
        # Iterate through each block of the snake and draw it as a rectangle
        for x, y in snake.snake_blocks:
            pygame.draw.rect(
                self.screen,  # Draw on the game screen
                self.snake_color,  # Use the snake color
                [x, y, self.block_size, self.block_size]  # Position and size of the block
            )

    def draw_food(self, food):
        """
        Draw the food on the screen.

        Args:
            food (Food): The Food object containing the current position of the food.
        """
        pygame.draw.rect(
            self.screen,  # Draw on the game screen
            self.food_color,  # Use the food color
            [food.position[0], food.position[1], self.block_size, self.block_size]  # Food position and size
        )

    def draw_score(self, score):
        """
        Draw the player's current score on the screen.

        Args:
            score (int): The player's current score.
        """
        # Render the score text using the font
        text = self.font.render(f"Score: {str(score)}", True, self.score_color)
        
        # Display the score text on the top-left corner of the screen
        self.screen.blit(text, (10, 10))  # Position at (10, 10)

    def draw_game_over(self):
        """
        Display the "Game Over" message in the center of the screen.
        """
        # Create a new font for the "Game Over" message
        game_over_font = pygame.font.Font(None, self.game_over_font_size)
        
        # Render the "Game Over" text
        text = game_over_font.render("Game Over", True, self.game_over_color)
        
        # Calculate the center position for the "Game Over" text
        center_x = self.screen.get_width() // 2 - text.get_width() // 2
        center_y = self.screen.get_height() // 2 - text.get_height() // 2
        
        # Display the "Game Over" text on the screen
        self.screen.blit(text, (center_x, center_y))