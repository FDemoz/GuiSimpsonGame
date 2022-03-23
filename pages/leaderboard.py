from guizero import App, Box, Text, PushButton
from utils.page import Page


class Leaderboard(Page):
    def __init__(self, base, next_page=None):
        super().__init__(base, next_page)

        self.p1_username = None
        self.p2_username = None
        self.p1_character = None
        self.p2_character = None
        self.game_stats = None
        self.leaderboard = None

        self.hide()

    def begin(self, p1_username, p2_username, p1_character, p2_character, game_stats):
        self.p1_username = p1_username
        self.p2_username = p2_username
        self.p1_character = p1_character
        self.p2_character = p2_character
        self.game_stats = game_stats
        self.leaderboard = []

        self.build()
        self.show()

    def next(self):
        pass
        # self.next_page(self.p1_username, 
        #                self.p2_username,
        #                self.p1_character,
        #                self.p2_character,
        #                self.game_stats)

    def build(self):
        Text(self, text="Leaderboard")
        PushButton(self, text="Next", command=self.next)



# copied from naughts and crosses game


WIDTH = 500
HEIGHT = WIDTH

BAR_WIDTH = WIDTH / 2
CELL_WIDTH = int((WIDTH - 1 * BAR_WIDTH) // 2)

BAR_COLOUR = "black"
CELL_COLOUR = "azure"

is_X = True
cells = []


def map_grid(cells):
    mapped_cells = []
    for row in cells:
        mapped_row = []
        for item in row:
            mapped_row.append(item.value)
        mapped_cells.append(mapped_row)
    return mapped_cells