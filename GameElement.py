class GameElement:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_within_bounds(self, x, y, width, height):
        return 0 <= x < width and 0 <= y < height
