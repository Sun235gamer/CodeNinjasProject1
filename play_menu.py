import arcade
import arcade.gui
import random

questions = [
    ("Before people discovered that Mount Everest was the tallest mountain, what was the tallest mountain?",
     "Mt.Everest"),
    ("are you sus?", "yes"), 
    ("why are you the imposter", "i just am")
]


def create_play_menu(manager):
    vertical_box = arcade.gui.UIBoxLayout()

    chosen_question = random.choice(questions)
    question_text = chosen_question[0]
    answer_text = chosen_question[0]

    question = arcade.gui.UITextArea(
        text=question_text
    )

    input_box = arcade.gui.UIInputText(
        text="I AM OVER HERE",
        text_color=arcade.color.WHITE,
        width=400
    )

    submit_button = arcade.gui.UIFlatButton()
    
    @submit_button.event("on_click")
    def on_click_submit(event):
        if input_box.text.lower() == answer_text.lower():
            print("correct!!")
        else:
            print("That is very incorrect")
        arcade.close_window()

    

    vertical_box.add(question)
    vertical_box.add(input_box)
    vertical_box.add(submit_button)
   
    manager.add(
        arcade.gui.UIAnchorWidget(
            anchor_x="center_x",
            anchor_y="center_y",
            child=vertical_box)
        )