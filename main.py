import arcade
import arcade.gui
from main_menu import create_main_menu
from play_menu import create_play_menu

SCREEN_WIDTH = 720
SCREEN_HEIGHT= 480


class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

        # create the UI manager
        self.main_menu_manager = arcade.gui.UIManager()
        self.play_manager = arcade.gui.UIManager()

        create_main_menu(self.main_menu_manager, play_function=self.play)
        create_play_menu(self.play_manager)

        self.current_menu = self.main_menu_manager
        self.main_menu_manager.enable()

    def on_draw(self):
        self.clear()
        self.current_menu.draw()

    def select_menu(self, manager):
        self.current_menu.disable()
        self.current_menu = manager
        self.current_menu.enable()

        print("finish selecting menu")

    def play(self):
        self.select_menu(self.play_manager)

window = GameWindow()
arcade.run()