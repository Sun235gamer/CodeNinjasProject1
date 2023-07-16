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
    
class QuestionState:
    def __init__(self) -> None:
        self.new_question()
    def new_question(self):
        self.question_answer_pair = random.choice(questions)
    def get_question_text(self):
        return self.question_answer_pair[0]
    


    def get_answer_text(self):
        return self.question_answer_pair[1]





def create_play_menu(manager, display_correct, display_incorrect):
    vertical_box = arcade.gui.UIBoxLayout()

    question_state = QuestionState()
    

    question = arcade.gui.UITextArea(
        text=question_state.get_question_text()
    )

    input_box = arcade.gui.UIInputText(
        text="Click on me to answer",
        text_color=arcade.color.WHITE,
        width=400
    )

    submit_button = arcade.gui.UIFlatButton(text="Submit!")
    
    @submit_button.event("on_click")
    def on_click_submit(event):
        is_correct = input_box.text.lower() == question_state.get_answer_text().lower()
        print(is_correct)
        print(f"got: {input_box.text}")
        display_result(is_correct)

        if is_correct:
            display_correct()
            question_state.new_question()
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