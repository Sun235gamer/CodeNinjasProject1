import arcade

SCREEN_WIDTH = 720
SCREEN_HEIGHT= 480


class GameWindow(arcade.Window):
    def __init__(self):
       super().__init__(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

       self.title_text = arcade.create_text_sprite(text="The best Trivia Questions",
            start_x=10,
            start_y=SCREEN_HEIGHT - 10,
            color=(255,255,255),
            font_size=14,
            anchor_y="top"
       )        



    def on_draw(self):
        self.title_text.draw()

        button_width = 80
        button_height = 20
        arcade.draw_rectangle_filled(
            center_x=10 + (button_width/2),
            center_y=SCREEN_HEIGHT - 34 - (button_height/2),
            width=button_width,
            height=button_height,
            color=arcade.color.WHITE
        )

window = GameWindow()
arcade.run()