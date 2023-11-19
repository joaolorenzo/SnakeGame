import pyxel

class UI:
    def __init__(self):
        pass

    def draw_menu_screen(self):
        pyxel.cls(0)  
        
        pyxel.text(50, 40, "Bem-vindo ao Snake Game!", pyxel.COLOR_YELLOW)
        
        pyxel.text(50, 60, "Aperte", pyxel.COLOR_WHITE)
        pyxel.text(90, 60, "ENTER", pyxel.COLOR_GREEN)
        pyxel.text(130, 60, "para começar", pyxel.COLOR_WHITE)
        
        pyxel.text(50, 80, "Regras:", pyxel.COLOR_ORANGE)
        pyxel.text(50, 100, "- Nao saia do tabuleiro", pyxel.COLOR_WHITE)
        pyxel.text(50, 120, "- Nao passe por cima de si mesmo", pyxel.COLOR_WHITE)

    def draw_game_over_screen(self):
        pyxel.cls(0) 
        pyxel.text(50, 50, "G A M E   O V E R", pyxel.COLOR_RED)
        pyxel.text(50, 70, "Aperte R para reiniciar", pyxel.COLOR_WHITE)
        pyxel.text(50, 80, "Q para fechar", pyxel.COLOR_WHITE)

    def draw_score(self, score):
        # Método atualizado para desenhar a pontuação na tela, recebendo score como parâmetro
        pyxel.text(5, 5, f"Score: {score}", 7)
