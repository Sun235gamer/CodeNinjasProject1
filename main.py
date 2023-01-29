import arcade

SCREEN_WIDTH = 720
SCREEN_HEIGHT= 480


class GameWindow(arcade.Window):
    def __init__(self):
       super().__init__(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)




    def on_draw(self):
        pass

window = GameWindow()
arcade.run()