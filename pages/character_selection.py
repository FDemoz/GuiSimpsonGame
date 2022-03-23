from guizero import Text, PushButton, Picture, Box
from utils.page import Page
from utils.spacer import Spacer
from config.charecters import characters


class Character_selection(Page):
    def __init__(self, base, next_page):
        super().__init__(base, next_page)

        self.p1_username = None
        self.p2_username = None
        self.p1_character = None
        self.p2_character = None
        self.coin_toss_winner_is_p1 = None

        self.hide()

    def begin(self, p1_username, p2_username, coin_toss_winner):
        self.p1_username = p1_username
        self.p2_username = p2_username
        self.coin_toss_winner = coin_toss_winner

        self.coin_toss_winner_is_p1 = coin_toss_winner == p1_username

        self.build()
        self.show()

    def next(self):
        if self.p1_character is None or self.p2_character is None:
            return

        self.hide()
        self.next_page(self.p1_username, self.p2_username, self.p1_character,
                       self.p2_character, self.coin_toss_winner_is_p1)

    def assign_character(self, is_p1, character_name):
        if is_p1:
            print(f"Player 1 selected {character_name}")
            self.p1_character = characters[character_name]
            self.p1_character.is_player_1 = True
        else:
            print(f"Player 2 selected {character_name}")
            self.p2_character = characters[character_name]
            self.p2_character.is_player_2 = True

        self.characters_select_buttons[character_name].hide()

    def select_character(self, name):
        if self.coin_toss_winner_is_p1:
            if self.p1_character is None:
                self.assign_character(True, name)
                self.banner.value = f"{self.p2_username} - It's your turn to select a character!"
            else:
                self.assign_character(False, name)
                self.banner.value = f"{self.p1_username} - It's your turn to select a character!"
        else:
            if self.p2_character is None:
                self.assign_character(False, name)
                self.banner.value = f"{self.p1_username} - It's your turn to select a character!"
            else:
                self.assign_character(True, name)
                self.banner.value = f"{self.p2_username} - It's your turn to select a character!"

        self.next()

    def build(self):
        # charectors

        self.banner = Text(
            self,
            text=
            f"{self.coin_toss_winner} - It's your turn to select a character!",
            size=16)
        Spacer(self, height=30)
        characters_box = Box(self, width=580, height=400, layout="grid")
        self.characters_select_buttons = {}

        for name, character in characters.items():
            image_path, width, hight, box_grid = character.get_image('character_selection')
            character_box = Box(characters_box,
                                          width=290,
                                          height=200,
                                          grid=box_grid)
            # homer_box.bg = "cornsilk"
            Picture(character_box,
                    image=image_path,
                    width=width,
                    height=hight,
                    align="left")
            Text(character_box, text=name, size=15)
            Spacer(character_box, height=10)
            Text(character_box, text=f"ATTACK: {character.power}")
            Text(character_box, text=f"HEALTH: {character.health}")
            Text(character_box, text=f"DEFENCE: {character.defence}")
            Text(character_box,
                 text=f"SPECIAL: {character.special_move}")
            Spacer(character_box, height=10)
            self.characters_select_buttons[name] = PushButton(
                character_box,
                text="Select",
                command=self.select_character,
                args=[name])

        # homer_box = Box(characters_box, width=290, height=200, grid=[0, 0])
        # # homer_box.bg = "cornsilk"
        # Picture(homer_box,
        #         image="assets/homer.png",
        #         width=100,
        #         height=200,
        #         align="left")
        # Text(homer_box, text="Homer", size=15)
        # Spacer(homer_box, height=10)
        # Text(homer_box, text="ATTACK: 10")
        # Text(homer_box, text="HEALTH: 10")
        # Text(homer_box, text="DEFENCE: 10")
        # Text(homer_box, text="SPECIAL: MOE's")
        # Spacer(homer_box, height=10)
        # self.homer_select = PushButton(homer_box,
        #                                text="Select",
        #                                command=self.select_character,
        #                                args=["homer"])

        # marge_box = Box(characters_box, width=290, height=200, grid=[1, 0])
        # # marge_box.bg = "lavender"

        # Picture(marge_box,
        #         image="assets/marge.png",
        #         width=80,
        #         height=200,
        #         align="left")
        # Text(marge_box, text="Marge", size=15)
        # Spacer(marge_box, height=10)
        # Text(marge_box, text="ATTACK: 10")
        # Text(marge_box, text="HEALTH: 10")
        # Text(marge_box, text="DEFENCE: 10")
        # Text(marge_box, text="SPECIAL: XXXXX")
        # Spacer(marge_box, height=10)
        # self.marge_select = PushButton(marge_box, text="Select",

        #                                command=self.select_character,
        #                                 args=["marge"])

        # bart_box = Box(characters_box, width=290, height=200, grid=[0, 1])
        # # bart_box.bg = "misty rose"

        # Picture(bart_box,
        #         image="assets/bart.png",
        #         width=85,
        #         height=155,
        #         align="left")
        # Text(bart_box, text="Bart", size="15")
        # Spacer(bart_box, height=10)
        # Text(bart_box, text="Attack: 10")
        # Text(bart_box, text="HEALTH: 10")
        # Text(bart_box, text="DEFENCE: 10")
        # Text(bart_box, text="SPEACIAL: Fly Kick")
        # Spacer(bart_box, height=10)
        # self.bart_select = PushButton(bart_box, text="Select", command=self.select_character,
        #                              args=["bart"])

        # lisa_box = Box(characters_box, width=290, height=200, grid=[1, 1])
        # # lisa_box.bg = "lavender blush"
        # Picture(lisa_box,
        #         image =  "assets/lisa.gif",
        #         width=85,
        #         height=150,
        #         align="left")
        # Text(lisa_box ,text="Lisa", size="15")
        # Spacer(lisa_box ,height=10)
        # Text(lisa_box ,text="ATTACK:10")
        # Text(lisa_box ,text="HEALTH:10")
        # Text(lisa_box, text="DEFENCE:10")
        # Text(lisa_box, text="SPECIAL: Books")
        # Spacer(lisa_box ,height=10)
        # self.lisa_select = PushButton(lisa_box ,text="Select",
        #                               command=self.select_character,args=["lisa"])
