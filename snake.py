class Snake:
    """
    Represents the snake in the game, including its position, movement, and growth behavior.
    """

    def __init__(
        self, color, block_size, width, height, initial_x, initial_y, direction
    ):
        """
        Initializes the snake with its attributes and starting position.

        Args:
            color (str): The color of the snake.
            block_size (int): The size of each block in the snake (in pixels).
            width (int): The width of the game screen (in pixels).
            height (int): The height of the game screen (in pixels).
            initial_x (int): The x-coordinate of the snake's starting position.
            initial_y (int): The y-coordinate of the snake's starting position.
            direction (str): The initial direction of the snake's movement.
        """
        self.color = color  # The color of the snake (used for rendering)
        self.block_size = block_size  # The size of each block in the snake
        self.width = width  # The width of the game screen
        self.height = height  # The height of the game screen
        
        # The direction the snake is moving initially (e.g., "up", "down", "left", "right")
        self.direction = direction
        
        # Initial position of the snake (center of the screen by default)
        self.initial_x = self.width // 2
        self.initial_y = self.height // 2

        # Define the snake as a list of blocks (tuples of x, y positions)
        self.snake_blocks = [
            (self.initial_x, self.initial_y),  # Head (first block)
            (self.initial_x - 10, self.initial_y),  # Body (second block)
            (self.initial_x - 20, self.initial_y),  # Tail (third block)
        ]

        # Reference to the head of the snake (the first block in the list)
        self.head = self.snake_blocks[0]  # The head position as a tuple (x, y)

    def snake_move(self):
        """
        Moves the snake in the current direction by updating the position of its head
        and shifting the blocks accordingly.
        """
        # Determine the new position of the head based on the current direction
        if self.direction == "up":
            new_head = (self.head[0], self.head[1] - self.block_size)  # Move up
        elif self.direction == "down":
            new_head = (self.head[0], self.head[1] + self.block_size)  # Move down
        elif self.direction == "right":
            new_head = (self.head[0] + self.block_size, self.head[1])  # Move right
        elif self.direction == "left":
            new_head = (self.head[0] - self.block_size, self.head[1])  # Move left

        # Add the new head position to the front of the snake
        self.snake_blocks.insert(0, new_head)

        # Update the head reference to the new position
        self.head = self.snake_blocks[0]

    def remove_tail(self):
        """
        Removes the last block of the snake (used when the snake does not grow).
        """
        self.snake_blocks.pop()  # Remove the last block from the list