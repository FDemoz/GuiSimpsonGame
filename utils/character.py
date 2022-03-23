class Character (object):
    def __init__(self, name, power, health, assault, defence, special_move, images):
        self.power = power
        self.health = health
        self.hp = self.health
        self.name = name
        self.assault = assault
        self.defence = defence
        self.special_move = special_move
        #####
        self.image_path = f"assets/images/characters/{name}/"
        self.images = images

        #### game play variables
        self.canvas = None
        self.image = None
        self.width = None
        self.hight = None
        self.is_player_1 = False
        self.is_player_2 = False

        self.is_dead = False

        self.sprite_x = None
        self.sprite_y = None

        self.sprite_ref = None
        self.hbf_ref = None

    def build(self, canvas):
        self.canvas = canvas
        hbb_x = 0 if self.is_player_1 else 400
        self.canvas.rectangle(hbb_x, 0, hbb_x + 200, 30, "black")

        self.image, self.width, self.hight, box_grid = self.get_image('action')
        self.sprite_x = 0 if self.is_player_1 else 600 - self.width
        self.sprite_y = 500 - self.hight
        
        self.draw_sprite()
        self.draw_health_bar()

    def draw_sprite(self):
        if self.sprite_ref:
            self.canvas.delete(self.sprite_ref)
        self.sprite_ref = self.canvas.image(self.sprite_x, self.sprite_y,
                                            self.image, self.width, self.hight)

    def draw_health_bar(self):
        if self.hbf_ref:
            self.canvas.delete(self.hbf_ref)

        hbf_w = max(0, 200 * self.hp // self.health)
        hbf_x = 0 if self.is_player_1 else 400 + (200 - hbf_w)
        hbf_y = 0
        self.hbf_ref = self.canvas.rectangle(hbf_x, hbf_y, hbf_x + hbf_w,
                                             hbf_y + 30, "yellow")
    def get_image(self, image_name):
        full_path = self.image_path + self.images[image_name]["path"]
        image_width = self.images[image_name]["width"]
        image_hight = self.images[image_name]["hight"]
        image_box_grid = self.images[image_name].get("box_grid")

        return full_path, image_width, image_hight, image_box_grid

    def move(self, direction, opponent):
        if self.is_dead:
            return
        stride = 10

        starting_x = self.sprite_x

        if self.is_player_1 and direction == "left":
            self.sprite_x = max(0, self.sprite_x - stride)
        elif self.is_player_1 and direction == "right":
            self.sprite_x = min(opponent.sprite_x - self.width,
                                self.sprite_x + stride)
        elif self.is_player_2 and direction == "left":
            self.sprite_x = max(opponent.sprite_x + opponent.width,
                                self.sprite_x - stride)
        elif self.is_player_2 and direction == "right":
            self.sprite_x = min(600 - self.width, self.sprite_x + stride)

        if self.sprite_x != starting_x:
            self.take_damage(0.2)
            self.draw_sprite()
        
    def get_power(self):
        return self.power

    def get_health(self):
        return self.health
      
    def get_name(self):
        return self.name

    def get_assault(self):
        return self.assault

    def get_defence(self):
        return self.defence

    def set_power(self, power):
        self.power = power

    def set_health(self, health):
        self.health = health

    def set_name(self,name):
        self.name = name

    def set_assault (self,assault):
        self.assault = assault 

    def set_defence(self,defence):
        self.defence = defence

    # Function to take damage (used for the fight)
    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)
        if self.hp == 0:
            self.is_dead = True
            self.image, self.width, self.hight, box_grid = self.get_image('dead')
            self.draw_sprite()
        self.draw_health_bar()
