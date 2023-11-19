import pyxel

class GameBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        # Desenhar a grade do jogo com linhas mais visíveis
        for x in range(self.width):
            for y in range(self.height):
                pyxel.rect(x * 10, y * 10, 9, 9, 5)  # Células do tabuleiro
