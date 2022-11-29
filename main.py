import arcade
import math


MAX_AFSTAND = 100

class Slangebosse:
    def __init__(self, start_position):
        self.position = start_position
        self.mus_position = start_position
    def update(self, mouse_position):
        self.mus_position = mouse_position
    def tegn(self):
        arcade.draw_rectangle_outline(*self.position, 40, 80, arcade.csscolor.BROWN, 5)

class Fugl():
    def __init__(self, start_koordinat, vinkel, start_hastighed, tyngdeacceleration=70, sporlaengde=100):
        self.start_x, self.start_y = start_koordinat
        self.koordinat = start_koordinat
        self.tid = 0
        self.vinkel = vinkel
        self.hastighed = start_hastighed
        self.tyngdeacceleration = tyngdeacceleration
        self.spor = list()
        self.har_aktiveret = False
        self.fugl_affyret = False
        self.sporlaengde = sporlaengde

    def opdater(self, delta_tid):
        if self.fugl_affyret:
            self.tid += delta_tid
            x = self.hastighed * math.cos(self.vinkel) * self.tid + self.start_x
            y = -(1 / 2) * self.tyngdeacceleration * self.tid ** 2 + self.hastighed * math.sin(
                self.vinkel) * self.tid + self.start_y
            self.koordinat = (x, y)
            self.spor.append(self.koordinat)
            if len(self.spor) > self.sporlaengde:
                self.spor.pop(0)

    def ny_parabel(self, start_koordinat, vinkel, start_hastighed, tyngdeacceleration=70):
        if not self.har_aktiveret:
            self.start_x, self.start_y = start_koordinat
            self.tid = 0
            self.vinkel = vinkel
            self.hastighed = start_hastighed
            self.tyngdeacceleration = tyngdeacceleration
            if self.fugl_affyret:
                self.har_aktiveret = True

    def tegn(self):
        x, y = self.koordinat
        arcade.draw_circle_filled(x, y, 8, arcade.csscolor.RED)
        for punkt in self.spor:
            arcade.draw_circle_filled(*punkt, 3, arcade.csscolor.RED)

class Vindue(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.csscolor.LIGHT_SKY_BLUE)

    def setup(self):
        self.slangebosse = Slangebosse((100, 100))
        self.fugl = Fugl((100, 100), 0, 0, sporlaengde=200)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE and self.fugl.fugl_affyret:
            haeldning_x = math.cos(self.fugl.vinkel)*self.fugl.hastighed
            haeldning_y = -self.fugl.tyngdeacceleration*self.fugl.tid+self.fugl.hastighed*math.sin(self.fugl.vinkel)
            hastighed = math.sqrt(haeldning_x**2+haeldning_y**2)
            vinkel = math.atan(haeldning_y/haeldning_x)
            self.fugl.ny_parabel(self.fugl.koordinat, -math.fabs(vinkel)+(math.pi/2), hastighed+50)
    def on_mouse_drag(self, x: int, y: int, dx: int, dy: int, buttons: int, modifiers: int):
        if not self.fugl.fugl_affyret:
            self.slangebosse.update((x, y))
            self.fugl.koordinat = (x, y)
    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if not self.fugl.fugl_affyret:
            delta_x = x-self.fugl.start_x
            delta_y = y-self.fugl.start_y
            haeldning = delta_y/delta_x
            afstand = math.sqrt(delta_x**2+delta_y**2)
            vinkel = math.atan(haeldning)

            if afstand >= MAX_AFSTAND:
                afstand = MAX_AFSTAND

            if delta_x > 0:
                afstand = -afstand
                
            self.fugl.ny_parabel((x, y), vinkel, afstand*2)
            self.fugl.fugl_affyret = True

    def update(self, delta_time: float):
        self.fugl.opdater(delta_time)
    def on_draw(self):
        self.clear()
        self.fugl.tegn()
        self.slangebosse.tegn()

def main():
    vindue = Vindue(800, 600, "Angry birds fugle")
    vindue.setup()

    arcade.run()

if __name__ == "__main__":
    main()