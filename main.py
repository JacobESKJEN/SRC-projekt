import arcade
import math

class slangebosse:
    def __init__(self, start_position):
        self.position = start_position
        self.mus_position = start_position
    def update(self, delta_tid, mouse_position):
        self.mus_position = mouse_position
    def tegn(self):
        arcade.draw_rectangle_outline(*self.position, 40, 80, arcade.csscolor.BROWN, 5)

class Fugl:
    def __init__(self, start_koordinat, vinkel, start_hastighed, tyngdeacceleration=70, sporlaengde=100):
        self.start_x, self.start_y = start_koordinat
        self.tid = 0
        self.vinkel = vinkel
        self.hastighed = start_hastighed
        self.tyngdeacceleration = tyngdeacceleration
        self.spor = list()
        self.har_aktiveret = False
        self.sporlaengde = sporlaengde

    def opdater(self, delta_tid):
        self.tid += delta_tid
        x = self.hastighed * math.cos(self.vinkel) * self.tid + self.start_x
        y = -(1 / 2) * self.tyngdeacceleration * self.tid ** 2 + self.hastighed * math.sin(
            self.vinkel) * self.tid + self.start_y
        self.koordinat = (x, y)
        self.spor.append(self.koordinat)
        if len(self.spor) > self.sporlaengde:
            self.spor.pop(0)

    def ny_funktion(self, start_koordinat, vinkel, start_hastighed, tyngdeacceleration=70):
        if not Vindue.fugl_affyret or not self.har_aktiveret:
            self.start_x, self.start_y = start_koordinat
            self.tid = 0
            self.vinkel = vinkel
            self.hastighed = start_hastighed
            self.tyngdeacceleration = tyngdeacceleration
            if Vindue.fugl_affyret:
                self.har_aktiveret = True
            self.er_affyret = True

    def tegn(self):
        x, y = self.koordinat
        arcade.draw_circle_filled(x, y, 5, arcade.csscolor.RED)
        if self.er_affyret:
            for punkt in self.spor:
                arcade.draw_circle_filled(*punkt, 2, arcade.csscolor.RED)

class Vindue(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.csscolor.LIGHT_SKY_BLUE)

    def setup(self):
        self.fugl = Fugl()
    def on_key_press(self, symbol: int, modifiers: int):
        pass
    def on_mouse_drag(self, x: int, y: int, dx: int, dy: int, buttons: int, modifiers: int):
    def update(self, delta_time: float):
        pass
    def on_draw(self):
        pass

def main():

if __name__ == "__main__":
    main()