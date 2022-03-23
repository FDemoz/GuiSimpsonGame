from guizero import Box, Text, PushButton, Drawing
from utils.page import Page
from utils.character import Character


class Game_play(Page):
    def __init__(self, base, next_page):
        super().__init__(base, next_page, padding=False)
        self.next_page = next_page

        self.p1_username = None
        self.p2_username = None
        self.p1_character: Character = None
        self.p2_character: Character = None
        self.coin_toss_winner_is_p1 = None
        self.game_stats = None

        self.hide()

    def begin(self, p1_username, p2_username, p1_character, p2_character, coin_toss_winner_is_p1):
        self.p1_username = p1_username
        self.p2_username = p2_username
        self.p1_character = p1_character
        self.p2_character = p2_character
        self.coin_toss_winner_is_p1 = coin_toss_winner_is_p1
        self.game_stats = {}

        self.build()
        self.show()
        how_to_play_file = open('assets/how_to_play.txt', 'r')
        how_to_play = how_to_play_file.read()
        self.app.info("How to Play", how_to_play)

    def next(self):
        self.hide()
        self.next_page(self.p1_username, 
                       self.p2_username,
                       self.p1_character,
                       self.p2_character,
                       self.game_stats)

    def on_key_press(self, event):
        key = event.key.lower()
    
        if key == "a":
            self.p1_character.move("left", self.p2_character)
        elif key == "d":
            self.p1_character.move("right", self.p2_character)
        elif key == "j":
            self.p2_character.move("left", self.p1_character)
        elif key == "l":
            self.p2_character.move("right", self.p1_character)
        elif key == "w":
            print("special move not implemented for p1")
        elif key == "i":
            print("special move not implemented for p2")


    def build(self):
        canvas = Drawing(self, width=600, height=500)
        canvas.image(0, 0, "assets/simpsons_house.jpeg", width=600, height=500)

        
        self.p1_character.build(canvas)
        self.p2_character.build(canvas)
        # image_path, width, hight, box_grid = self.p1_character.get_image('action')
        # canvas.image(10, 240, image_path, width=width, height=hight)

        # image_path, width, hight, box_grid = self.p2_character.get_image('action')
        # canvas.image(460, 240, image_path, width=width, height=hight)

        # HERE
        
        # canvas.rectangle(10, 5, 200, 30, color="black")
        # canvas.rectangle(5, 5, 150, 30, color="yellow")

        # canvas.rectangle(550, 5,300, 30, color="blue")
        # canvas.rectangle(400, 5,220, 30, color="green")

        self.app.when_key_pressed = self.on_key_press
        
        # HERE
      

        
        

  