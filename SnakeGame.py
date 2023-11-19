import pyxel
from Snake import Snake
from Apple import Apple
from UI import UI  

class SnakeGame:
    def __init__(self):
        self.snake = Snake(10, 10)
        self.apple = Apple(25, 25) 
        self.game_state = 'MENU' 
        self.score = 0
        self.update_counter = 0
        self.update_interval = 5  
        self.board_width = 25
        self.board_height = 25
        self.game_over = False
        self.ui = UI()  
        pyxel.init(256, 256, 'Snake Game')
        pyxel.run(self.update, self.draw)


    def update(self):
        if self.game_state == 'MENU':
        # Código para o menu inicial
            if pyxel.btnp(pyxel.KEY_RETURN): 
                self.game_state = 'PLAYING'
        elif self.game_state == 'GAME_OVER':
            if pyxel.btnp(pyxel.KEY_R): 
                self.reset_game()
            if pyxel.btnp(pyxel.KEY_Q): 
                pyxel.quit()
        else:  
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()
            if pyxel.btnp(pyxel.KEY_R):
                self.reset_game()
            if self.game_over:
                self.game_state = 'GAME_OVER'
                return

            self.update_counter += 1
            if self.update_counter < self.update_interval:
                return
            self.update_counter = 0

            self.change_snake_direction()

            self.snake.update()

            if self.check_collision():
                self.snake.grow()
                self.apple.reposition(self.snake.body, self.board_width, self.board_height)
                self.score += 10

            if self.is_out_of_bounds(self.snake.body[0]):
                self.game_over = True

            # Adicionado verificação para colisão com o próprio corpo
            if any(segment == self.snake.body[0] for segment in self.snake.body[1:]):
                self.game_over = True
                self.game_state = 'GAME_OVER'

    def change_snake_direction(self):
        if pyxel.btn(pyxel.KEY_UP) and self.snake.direction != 'DOWN':
            self.snake.direction = 'UP'
        elif pyxel.btn(pyxel.KEY_DOWN) and self.snake.direction != 'UP':
            self.snake.direction = 'DOWN'
        elif pyxel.btn(pyxel.KEY_LEFT) and self.snake.direction != 'RIGHT':
            self.snake.direction = 'LEFT'
        elif pyxel.btn(pyxel.KEY_RIGHT) and self.snake.direction != 'LEFT':
            self.snake.direction = 'RIGHT'

    def check_collision(self):
        head = self.snake.body[0]
        return head.x == self.apple.x and head.y == self.apple.y

    def is_out_of_bounds(self, point):
        return point.x < 0 or point.y < 0 or point.x >= 25 or point.y >= 25

    def reset_game(self):
        self.snake = Snake(10, 10)
        self.apple = Apple(self.board_width, self.board_height)
        self.score = 0
        self.update_counter = 0
        self.game_over = False
        self.game_state = 'PLAYING'  

    def draw(self):
        pyxel.cls(0)
        if self.game_state == 'MENU':
            self.ui.draw_menu_screen()  # Desenha a tela do menu
        elif self.game_state == 'GAME_OVER':
            self.ui.draw_game_over_screen()  # Desenha a tela de game over
            self.ui.draw_score(self.score)  # Desenha a pontuação na tela de game over
        else:
            # Desenha a cobra e a maçã
            for segment in self.snake.body:
                pyxel.rect(segment.x * 10, segment.y * 10, 9, 9, pyxel.COLOR_GREEN)
            pyxel.rect(self.apple.x * 10, self.apple.y * 10, 9, 9, pyxel.COLOR_RED)

            # Desenha a pontuação
            self.ui.draw_score(self.score)  # Atualizado para passar o score

            # Instruções de controle
            pyxel.text(5, 246, "Q to Quit, R to Reset", pyxel.COLOR_WHITE)



    def draw_score(self):
        pyxel.text(200, 240, f"Score: {self.score}", pyxel.COLOR_WHITE)

if __name__ == "__main__":
    SnakeGame()
