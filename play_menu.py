import arcade
import arcade.gui
import random

questions = [
    "Before people discovered that Mount Everest was the tallest mountain, what was the tallest mountain?"
    "are you sus?"
]


def create_play_menu(manager):
    vertical_box = arcade.gui.UIBoxLayout()

    question = arcade.gui.UITextArea(
        text=random.choice(questions)
    )

    vertical_box.add(question)

    manager.add(
        arcade.gui.UIAnchorWidget(
            anchor_x="center_x",
            anchor_y="center_y",
            child=vertical_box)
        )