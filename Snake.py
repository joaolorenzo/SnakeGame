from Point import Point
from GameElement import GameElement

class Snake(GameElement):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.body = [Point(x, y)] 
        self.direction = 'RIGHT'
        self.growing = False

    def update(self, board_width, board_height, game_over_callback):
        if not self.body:
            raise ValueError("O corpo da cobra não pode estar vazio.")
        
        if len(self.body) > 0:
            head = self.body[0]
            new_x, new_y = head.x, head.y
            if self.direction == 'UP':
                new_y -= 1
            elif self.direction == 'DOWN':
                new_y += 1
            elif self.direction == 'LEFT':
                new_x -= 1
            elif self.direction == 'RIGHT':
                new_x += 1

            if not self.is_within_bounds(new_x, new_y, board_width, board_height):
                game_over_callback()
                return

            new_head = Point(new_x, new_y)
            self.body.insert(0, new_head)
            
            if not self.growing:
                self.body.pop()
            
            self.growing = False


    def grow(self):
        self.growing = True

    def check_collision_with_self(self):
        head = self.body[0]
        for segment in self.body[1:]:
            if head == segment:
                return True
        return False

    def reset(self, x, y):
        self.body = [Point(x, y)]
        self.direction = 'RIGHT'
        self.growing = False
