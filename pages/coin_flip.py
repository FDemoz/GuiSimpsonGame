import random

from guizero import Text, PushButton, ListBox, Box, Picture
from utils.page import Page


class Coin_flip(Page):
    def __init__(self, base, next_page):
        super().__init__(base, next_page)

        self.p1_username = None
        self.p2_username = None
        self.coin_toss_winner = None

        self.hide()

    def begin(self, p1_username, p2_username):
        self.p1_username = p1_username
        self.p2_username = p2_username

        self.build()
        self.show()

    def next(self):
        self.hide()
        self.next_page(self.p1_username, self.p2_username,
                       self.coin_toss_winner)

    def flip_coin(self):
        if self.p1_choice.value == self.p2_choice.value:
            self.app.warn(
                    "D'oh!",
                    "Can't pick the same side, I am afraid!")
            return

        result = random.randint(0, 1)

        if result == 1:
            if self.p1_choice.value == "Heads":
                self.coin_toss_winner = self.p1_username
            else:
                self.coin_toss_winner = self.p2_username
        else:
            if self.p1_choice.value == "Tails":
                self.coin_toss_winner = self.p1_username
            else:
                self.coin_toss_winner = self.p2_username
        self.app.info("Winner", f"{self.coin_toss_winner} wins coin toss!")

        self.next()
        

    def build(self):

        Text(self, text="Coin toss for first character selection")
        Picture(self,
                image="assets/family.png",
                width=200,
                height=200,
                align="top")
        coin_box = Box(self, width=600, height=100, align="top")
        left_box = Box(coin_box, width=300, height=70, align="left")
        Text(left_box, text=self.p1_username, size=13)
        self.p1_choice = ListBox(left_box,
                            items=["Heads", "Tails"],
                            selected="Heads",
                            width=100,
                            height=50)

        right_box = Box(coin_box, width=300, height=70, align="right")
        Text(right_box, text=self.p2_username, size=13)
        self.p2_choice = ListBox(right_box,
                            items=["Heads", "Tails"],
                            selected="Tails",
                            width=100,
                            height=50)

        Picture(self,
                image="assets/coin_flip.gif",
                width=200,
                height=100,
                align="top")
        
        PushButton(self, text="Flip coin", command=self.flip_coin)

