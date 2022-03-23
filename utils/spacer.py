from guizero import Box

class Spacer(Box):
    def __init__(self, base, width=None, height=None):
        w = width if width else base.width
        h = height if height else base.height
        super().__init__(base, width=w, height=h)