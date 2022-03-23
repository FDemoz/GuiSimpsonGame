from guizero import Text, PushButton
from utils.page import Page


class Result(Page):
    def __init__(self, base, next_page):
        super().__init__(base, next_page)

        self.p1_username = None
        self.p2_username = None
        self.p1_character = None
        self.p2_character = None
        self.game_stats = {
            "p1_point": 321,
            "p2_point": 23
        }

        self.hide()

    def begin(self, p1_username, p2_username, p1_character, p2_character, game_stats):
        self.p1_username = p1_username
        self.p2_username = p2_username
        self.p1_character = p1_character
        self.p2_character = p2_character
        self.game_stats = game_stats

        self.build()
        self.show()

    def next(self):
        self.hide()
        self.next_page(self.p1_username, 
                       self.p2_username, 
                       self.p1_character,
                       self.p2_character,
                       self.game_stats
                      )

    def build(self):
        Text(self, text="Result page")
        PushButton(self, text="Next", command=self.next)
        print("The winner is")
    