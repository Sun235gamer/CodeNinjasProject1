import arcade
import arcade.gui
from state import State



def create_choose_play_menu(manager, play_menu_function):
    vertical_box = arcade.gui.UIBoxLayout()

    

    question = arcade.gui.UITextArea(
        text="how many peeps are playing?"
    )

    input_box = arcade.gui.UIInputText(
        text="WRITE YOUR RESPONSE HERE ",
        text_color=arcade.color.WHITE,
        width=400
    )

    submit_button = arcade.gui.UIFlatButton(text="Submit!")
    
    @submit_button.event("on_click")
    def on_click_submit(event):
        print("submitted!")


        if input_box.text.isnumeric():
            State.set_player(int(input_box.text))
            play_menu_function()    
   
      

    

    vertical_box.add(question)
    vertical_box.add(input_box)
    vertical_box.add(submit_button)
   
    manager.add(
        arcade.gui.UIAnchorWidget(
            anchor_x="center_x",
            anchor_y="center_y",
            child=vertical_box)
        )