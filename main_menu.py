import arcade
import arcade.gui

def create_main_menu(manager, play_function): 
    # create the vertical box where we will store widgets
    vertical_box = arcade.gui.UIBoxLayout()

    title_text = arcade.gui.UITextArea(
    text="My Trivia Game",
    width=200,
    height=40,
    font_size=22,
    font_name="sans-serif"
    )
    quit_button = arcade.gui.UIFlatButton(text="quit")
    @quit_button.event("on_click")
    def on_click_quit(event):
        arcade.close_window()
    
    quit_button_container = arcade.gui.UIPadding(
        child=quit_button, 
        padding=(10,0,10,0)
    )

   
    play_button = arcade.gui.UIFlatButton(text="play")
    @play_button.event("on_click")
    def on_click_play(event):
        play_function

    play_button_container = arcade.gui.UIPadding(
        child=play_button, 
        padding=(10,0,10,0)
    )

    vertical_box.add(title_text)
    vertical_box.add(play_button_container)
    vertical_box.add(quit_button_container)

    manager.add(
        arcade.gui.UIAnchorWidget(
            anchor_x="center_x",
            anchor_y="center_y",
            child=vertical_box)
        )