from Point import Point
from GameElement import GameElement

class Snake(GameElement):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.body = [Point(x, y)] 
        self.direction = 'RIGHT'
        self.growing = False

    def update(self):
        if not self.body:
            raise ValueError("O corpo da cobra não pode estar vazio.")
        
        if len(self.body) > 0:
            head = self.body[0]
            if self.direction == 'UP':
                new_head = Point(head.x, head.y - 1)
            elif self.direction == 'DOWN':
                new_head = Point(head.x, head.y + 1)
            elif self.direction == 'LEFT':
                new_head = Point(head.x - 1, head.y)
            elif self.direction == 'RIGHT':
                new_head = Point(head.x + 1, head.y)
            
            self.body.insert(0, new_head)
            
            if not self.growing:
                self.body.pop()
            
            self.growing = False  

    def grow(self):
        last_segment = self.body[-1]
        new_segment = Point(last_segment.x, last_segment.y)
        self.body.append(new_segment)

    def check_collision_with_self(self):
        head = self.body[0]
        for segment in self.body[1:]:
            if head == segment:
                return True
        return False