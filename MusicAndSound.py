class MusicAndSound:
    def __init__(self):
        # Aqui iria a inicialização dos sons
        pass

    def play_sound_effect(self, effect):
        try:
            if effect == 'apple':
                # Tocar som de coleta da maçã
                pyxel.play(0, 1)
            elif effect == 'death':
                # Tocar som de morte
                pyxel.play(0, 2)
        except Exception as e:
            print(f"Error playing sound: {e}")

    # Outros métodos para iniciar e parar a música
