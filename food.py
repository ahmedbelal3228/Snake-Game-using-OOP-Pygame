import random


class Food:
    """
    Represents the food in the game. The food appears at random positions on the screen,
    ensuring it does not overlap with the snake.
    """

    def __init__(self, color, block_size, snake_blocks, width, height):
        """
        Initializes the food object and places it at a random position.

        Args:
            color (str): The color of the food.
            block_size (int): The size of the food block (in pixels).
            snake_blocks (list of tuples): The current positions of the snake blocks to avoid overlap.
            width (int): The width of the game screen (in pixels).
            height (int): The height of the game screen (in pixels).
        """
        self.color = color  # The color of the food (used for rendering)
        
        # Generate the initial position of the food
        self.position = self.generate_food(block_size, snake_blocks, width, height)

    def generate_food(self, block_size, snake_blocks, width, height):
        """
        Generates a random position for the food, ensuring it does not overlap with the snake.

        Args:
            block_size (int): The size of the food block (and the snake blocks) in pixels.
            snake_blocks (list of tuples): The current positions of the snake blocks to avoid overlap.
            width (int): The width of the game screen in pixels.
            height (int): The height of the game screen in pixels.

        Returns:
            tuple: A random (x, y) position for the food.
        """
        while True:
            # Generate random x and y coordinates within the game screen's grid
            food_x = random.randint(0, (width - block_size) // block_size) * block_size
            food_y = random.randint(0, (height - block_size) // block_size) * block_size
            
            # Ensure the food's position does not overlap with any of the snake blocks
            if (food_x, food_y) not in snake_blocks:
                return (food_x, food_y)  # Return a valid food position