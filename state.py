class State:
    players = 0

    @classmethod
    def set_player(cls, number_of_guests):
        cls.players = number_of_guests
            