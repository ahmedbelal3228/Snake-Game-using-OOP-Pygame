import _01_game_logic  # Import the main game logic class

# Entry point for the game
if __name__ == "__main__":
    # Create an instance of the GameLogic class to manage the game
    game = _01_game_logic.GameLogic()
    
    # Start the game loop
    game.run()