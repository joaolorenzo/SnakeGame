import random

class Apple:
    def __init__(self, board_width, board_height):
        self.x = random.randint(0, board_width - 1)
        self.y = random.randint(0, board_height - 1)

    def reposition(self, snake_body, board_width, board_height):
        while True:
            new_x = random.randint(0, board_width - 1)
            new_y = random.randint(0, board_height - 1)
            if not any(part.x == new_x and part.y == new_y for part in snake_body):
                self.x = new_x
                self.y = new_y
                break
