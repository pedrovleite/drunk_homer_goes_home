class Drunk:
    def __init__(self,name, posy, posx, el_time, char):
        self.name = name
        self.posy = posy
        self.posx = posx
        self.el_time = el_time
        self.char = char

    def walk(self, ymove, xmove):
        self.posy = self.posy + ymove
        self.posx = self.posx + xmove
        self.el_time += 1
