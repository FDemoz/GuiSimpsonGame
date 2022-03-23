from guizero import Box

class Page(Box):
    def __init__(self, base, next_page, padding=True):
        super().__init__(base, width=600, height=500)
        self.app = base
        self.next_page = next_page

        if padding:
            Box(self, width=10, height=500, align="left")
            Box(self, width=10, height=500, align="right")
            Box(self, width=580, height=10, align="top")
            Box(self, width=580, height=10, align="bottom")