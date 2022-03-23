from guizero import Box, Text, PushButton, Picture, TextBox, Window
from utils.page import Page
from utils.spacer import Spacer
from utils import authonticate


class Sign_in(Page):
    def __init__(self, base, next_page):
        super().__init__(base, next_page)
        self.p1_username = None
        self.p2_username = None

        self.hide()

    def begin(self):
        self.build()
        self.show()

    def next(self):
        self.hide()
        self.next_page(self.p1_username, self.p2_username)

    def show_signup_window(self):
        #app.info("Sign up", "Please enter your name, username and password")
        print("Please sign up to play")
        self.signup_window.show()

    def register_user(self):
        name = self.name_box2.value
        password = self.password_box2.value
        singed_up, msg = authonticate.create_account(name, password)

        self.sign_up_msg_box.value = msg
        if singed_up is False:
            self.app.warn("D'oh!", msg)

    def sign_in(self):
        if self.p1_username_text_box.value == self.p2_username_text_box.value:
            self.p1_message_text_box.value = "Please fix"
            self.app.warn(
                "Uh oh!",
                "You can't play with your self, please come back when you have made some freinds"
            )
            return

        # player 1 authonticate
        p1_logged, msg = authonticate.login(self.p1_username_text_box.value,
                                            self.p1_passwd_text_box.value)
        self.p1_message_text_box.value = msg
        if p1_logged is True:
            self.p1_username = self.p1_username_text_box.value
        else:
            self.app.warn("Uh oh! Player 1", msg)

        # player 2 authonticate
        p2_logged, msg = authonticate.login(self.p2_username_text_box.value,
                                            self.p2_passwd_text_box.value)
        self.p2_message_text_box.value = msg
        if p2_logged is True:
            self.p2_username = self.p2_username_text_box.value
        else:
            self.app.warn("Uh oh! Player 2", msg)

        if self.p1_username is not None and self.p2_username is not None:
            self.next()

    def build(self):

        left_box = Box(self, width=300, height=480, align="left")
        Picture(left_box,
                image="assets/simpsons_logo.png",
                width=300,
                height=100)

        Picture(self,
                image="assets/lisa.gif",
                align="right",
                width=300,
                height=450)

        Spacer(left_box, height=15)
        p1_username_label = Box(left_box, width=300, height=30)
        Text(p1_username_label,
             text="Player one username",
             size=13,
             align="left")
        self.p1_username_text_box = TextBox(left_box, width=40)

        Spacer(left_box, height=10)
        p1_password_label = Box(left_box, width=300, height=30)
        Text(p1_password_label,
             text="Player one password",
             size=13,
             align="left")
        self.p1_passwd_text_box = TextBox(left_box, width=40, hide_text=True)
        Spacer(left_box, height=5)
        self.p1_message_text_box = Text(left_box, text="", size=9)

        Spacer(left_box, height=10)
        divider = Box(left_box, width=300, height=1)
        divider.bg = "black"

        Spacer(left_box, height=15)
        p2_username_label = Box(left_box, width=300, height=30)
        Text(p2_username_label,
             text="Player two username",
             size=13,
             align="left")
        self.p2_username_text_box = TextBox(left_box, width=40)

        Spacer(left_box, height=10)
        p2_password_label = Box(left_box, width=300, height=30)
        Text(p2_password_label,
             text="Player two password",
             size=13,
             align="left")
        self.p2_passwd_text_box = TextBox(left_box, width=40, hide_text=True)
        Spacer(left_box, height=5)
        self.p2_message_text_box = Text(left_box, text="", size=9)

        # Text(left_box, text="Player 2", size=13)
        # self.p2_username_text_box = TextBox(left_box, width=25)
        # Spacer(left_box, height=10)
        # Text(left_box, text="Password", size=13)
        # self.p2_passwd_text_box = TextBox(left_box, width=25, hide_text=True)
        # Spacer(left_box, height=5)
        # self.p2_message_text_box = Text(left_box, text="", size=9)

        Spacer(left_box, height=15)
        PushButton(left_box,
                   text="Sign up",
                   command=self.show_signup_window,
                   align="left")
        PushButton(left_box,
                   text="Sign in",
                   command=self.sign_in,
                   align="right")

        # Sign up button/pop up window
        self.signup_window = Window(self,
                                    "Sign Up",
                                    width=250,
                                    height=300,
                                    visible=False)
        self.signup_window.bg = "yellow"
        self.text5 = Text(self.signup_window,
                          text="Username",
                          size=10,
                          font="Arial")
        self.name_box2 = TextBox(self.signup_window, text="")
        self.text6 = Text(self.signup_window,
                          text="Password",
                          size=10,
                          font="Arial")
        self.password_box2 = TextBox(self.signup_window, hide_text=True)
        self.signup_button = PushButton(self.signup_window,
                                        text="Sign up",
                                        command=self.register_user)
        self.sign_up_msg_box = Text(self.signup_window, text="", size=9)
