import random
from GameElement import GameElement

class Apple(GameElement):
    def __init__(self, board_width, board_height):
        x = random.randint(0, board_width - 1)
        y = random.randint(0, board_height - 1)
        super().__init__(x, y)

    def reposition(self, snake_body, board_width, board_height):
        try:
            while True:
                new_x = random.randint(0, board_width - 1)
                new_y = random.randint(0, board_height - 1)
                if self.is_within_bounds(new_x, new_y, board_width, board_height) and \
                not any(part.x == new_x and part.y == new_y for part in snake_body):
                    self.x = new_x
                    self.y = new_y
                    break
        except ValueError:
            print('Erro ao reposicionar a maçã.')