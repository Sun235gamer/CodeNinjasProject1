import arcade


class Assets:
    sounds = {
        "drumroll": None
    }

    @classmethod
    def load(cls):
        Assets.sounds["drumroll"] = arcade.load_sound("assets/drumroll.wav")