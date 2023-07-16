from state import State
import arcade
import arcade.gui
from main_menu import create_main_menu
from play_menu import create_play_menu
from asset_manager import Assets
from choose_player_menu import create_choose_play_menu

SCREEN_WIDTH = 720
SCREEN_HEIGHT= 480

background_timer_duration = 10

class GameWindow(arcade.Window):  
    def __init__(self):
        super().__init__(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

        # create the UI manager
        self.main_menu_manager = arcade.gui.UIManager()
        self.play_manager = arcade.gui.UIManager()

        self.choose_player_manager = arcade.gui.UIManager()

        create_main_menu(self.main_menu_manager, play_function=self.choose_players)
        create_play_menu(self.play_manager, self.display_correct, self.display_incorrect)

        create_choose_play_menu(self.choose_player_manager, play_menu_function=self.play)

        self.current_menu = self.main_menu_manager
        self.main_menu_manager.enable()
  
        self.bg = arcade.color.GRAY
        self.is_displaying = False
        self.background_display_timer = 0
        Assets.load()
    
    def on_draw(self):
        self.clear(self.bg)
        self.current_menu.draw()
    def on_update(self, delta_time: float):
        if self.is_displaying:
            self.background_display_timer += 1
        if self.background_display_timer == background_timer_duration:
            self.background_display_timer = 0
            self.is_displaying = False
            self.bg = arcade.color.GRAY    

    def display_correct(self):
        self.bg = arcade.color.GREEN

        self.is_displaying = True

    def display_incorrect(self):
        self.bg = arcade.color.RED

        self.is_displaying = True


    def select_menu(self, manager):
        self.current_menu.disable()
        self.current_menu = manager
        self.current_menu.enable()

        print("finish selecting menu")

    def play(self):
        self.select_menu(self.play_manager)

    def choose_players(self):
        self.select_menu(self.choose_player_manager)
window = GameWindow()
arcade.run()