from guizero import App

from pages.sign_in import Sign_in
from pages.coin_flip import Coin_flip
from pages.character_selection import Character_selection
from pages.game_play import Game_play
from pages.leaderboard import Leaderboard
from pages.result import Result
from config.charecters import characters


app = App(title="The Simpsons' Game", width=600, height=500)
app.bg = "yellow"

lb_page = Leaderboard(app)
rs_page = Result(app, next_page=lb_page.begin)
gp_page = Game_play(app, next_page=rs_page.begin)
cs_page = Character_selection(app, next_page=gp_page.begin)
cf_page = Coin_flip(app, next_page=cs_page.begin)
si_page = Sign_in(app, next_page=cf_page.begin)

# si_page.begin()

cs_page.begin("Rupal", "Fasega", "Fasega")
player_character = characters["Marge"]
player2_character = characters["Lisa"]

# gp_page.begin("Rupal", "Fasega", player_character, player2_character)

#sorry sis is chatting to me again, i just wanna focus 

app.display()

#my laptop made a noise when u deleted that 
# when u backspace it makes noise just like i did it 
#hello?