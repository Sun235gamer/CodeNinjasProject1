import arcade
import arcade.gui
import random
from asset_manager import Assets
import time
import threading

questions = [
    ("Before people discovered that Mount Everest was the tallest mountain, what was the tallest mountain?",
     "Trick Question"),
    ("are you sus?", "yes"), 
    ("why are you the imposter", "i just am")
]

def display_result(correct : bool):
   
    sound = Assets.sounds["drumroll"]
    sound.play()

    time.sleep(sound.get_length())
    if correct:
        print("correct!!")
    else:
        print("That is very incorrect")
    



def create_play_menu(manager, display_correct, display_incorrect):
    vertical_box = arcade.gui.UIBoxLayout()

    chosen_question = random.choice(questions)
    question_text = chosen_question[0]
    answer_text = chosen_question[0]

    question = arcade.gui.UITextArea(
        text=question_text
    )

    input_box = arcade.gui.UIInputText(
        text="Click on me to answer",
        text_color=arcade.color.WHITE,
        width=400
    )

    submit_button = arcade.gui.UIFlatButton(text="Submit!")
    
    @submit_button.event("on_click")
    def on_click_submit(event):
        is_correct = input_box.text.lower() == answer_text.lower()
        print(is_correct)
        print(f"got: {input_box.text}")
        display_result(is_correct)

        if is_correct:
            display_correct()
        else:
            display_incorrect()
          
    

      
   
      

    

    vertical_box.add(question)
    vertical_box.add(input_box)
    vertical_box.add(submit_button)
   
    manager.add(
        arcade.gui.UIAnchorWidget(
            anchor_x="center_x",
            anchor_y="center_y",
            child=vertical_box)
        )