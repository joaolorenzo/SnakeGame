import random
from GameElement import GameElement

class Apple(GameElement):
    def __init__(self, board_width, board_height):
        x = random.randint(0, board_width - 1)
        y = random.randint(0, board_height - 1)
        super().__init__(x, y)

    def reposition(self, snake_body, board_width, board_height):
        while True:
            new_x = random.randint(0, board_width - 1)
            new_y = random.randint(0, board_height - 1)
            if not any(part.x == new_x and part.y == new_y for part in snake_body):
                self.x = new_x
                self.y = new_y
                break

    def reposition(self, snake_body, board_width, board_height):
        if board_width <= 0 or board_height <= 0:
            raise ValueError("Dimensões do tabuleiro devem ser positivas e maiores que zero.")
        while True:
            new_x = random.randint(0, board_width - 1)
            new_y = random.randint(0, board_height - 1)
            if not any(part.x == new_x and part.y == new_y for part in snake_body):
                self.x = new_x
                self.y = new_y
                break