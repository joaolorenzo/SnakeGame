from Point import Point

class Snake:
    def __init__(self, x, y):
        self.body = [Point(x, y)]  # Inicializa com um objeto Point
        self.direction = 'RIGHT'
        self.growing = False  # 
        # Outros atributos necessários

    def update(self):
        if len(self.body) > 0:
            # Calcula a nova cabeça com base na direção atual
            head = self.body[0]
            if self.direction == 'UP':
                new_head = Point(head.x, head.y - 1)
            elif self.direction == 'DOWN':
                new_head = Point(head.x, head.y + 1)
            elif self.direction == 'LEFT':
                new_head = Point(head.x - 1, head.y)
            elif self.direction == 'RIGHT':
                new_head = Point(head.x + 1, head.y)
            
            # Adiciona a nova cabeça ao início do corpo
            self.body.insert(0, new_head)
            
            # Se a cobra não estiver crescendo, remove o último segmento
            if not self.growing:
                self.body.pop()
            
            self.growing = False  

    def grow(self):
        # Pega a posição do último segmento
        last_segment = self.body[-1]
        # Cria um novo segmento como uma instância de Point
        new_segment = Point(last_segment.x, last_segment.y)
        # Adiciona o novo segmento ao corpo da cobra
        self.body.append(new_segment)

    def check_collision_with_self(self):
        head = self.body[0]
        return any(segment == head for segment in self.body[1:])