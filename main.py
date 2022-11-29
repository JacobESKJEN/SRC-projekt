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

class Roed_Fugl():
    def __init__(self, start_koordinat, vinkel, start_hastighed, tyngdeacceleration=70, sporlaengde=100):
        self.start_x, self.start_y = start_koordinat
        self.koordinat = start_koordinat
        self.tid = 0
        self.vinkel = vinkel
        self.hastighed = start_hastighed
        self.tyngdeacceleration = tyngdeacceleration
        self.spor = list()
        self.har_aktiveret = True
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
        if not self.fugl_affyret:
            self.start_x, self.start_y = start_koordinat
            self.tid = 0
            self.vinkel = vinkel
            self.hastighed = start_hastighed
            self.tyngdeacceleration = tyngdeacceleration


    def tegn(self):
        x, y = self.koordinat
        arcade.draw_circle_filled(x, y, 8, arcade.csscolor.RED)
        for punkt in self.spor:
            arcade.draw_circle_filled(*punkt, 3, arcade.csscolor.RED)

class Hvid_Fugl():
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
        arcade.draw_circle_filled(x, y, 8, arcade.csscolor.WHITE)
        for punkt in self.spor:
            arcade.draw_circle_filled(*punkt, 3, arcade.csscolor.WHITE)

class Blaa_Fugl():
    def __init__(self, start_koordinat, vinkel, start_hastighed, tyngdeacceleration=70, sporlaengde=100, lille=False):
        self.start_x, self.start_y = start_koordinat
        self.koordinat = start_koordinat
        self.tid = 0
        self.vinkel = vinkel
        self.hastighed = start_hastighed
        self.tyngdeacceleration = tyngdeacceleration
        self.spor = list()
        self.har_aktiveret = False
        self.fugl_affyret = lille
        self.sporlaengde = sporlaengde
        self.lille_stoerrelse = lille
        self.under_fugle = list()

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

            for under_fugl in self.under_fugle:  # Hvis fuglen har delt sig i tre, er længden af self.under_fugle > 0.
                under_fugl.opdater(delta_tid)

    def ny_parabel(self, start_koordinat, vinkel, start_hastighed, tyngdeacceleration=70):
        if not self.har_aktiveret:
            self.start_x, self.start_y = start_koordinat
            self.tid = 0
            self.vinkel = vinkel
            self.hastighed = start_hastighed
            self.tyngdeacceleration = tyngdeacceleration
            if self.fugl_affyret:
                self.har_aktiveret = True

    def skab_under_fugl(self, vinkel, hastighed):
        under_fugl = Blaa_Fugl(self.koordinat, vinkel, hastighed, self.tyngdeacceleration, self.sporlaengde, True)
        self.under_fugle.append(under_fugl)

    def tegn(self):
        x, y = self.koordinat
        arcade.draw_circle_filled(x, y, 8, arcade.csscolor.BLUE)
        for punkt in self.spor:
            arcade.draw_circle_filled(*punkt, 3, arcade.csscolor.BLUE)
        for under_fugl in self.under_fugle:  # Hvis fuglen har delt sig i tre, er længden af self.under_fugle > 0.
            under_fugl.tegn()


class Menu:
    def __init__(self):
        self.knap_antal = 3
        self.knap_bredde = 120
        self.knap_hoejde = 80
        self.knap_afstand = 20

    def tegn_rød_fugl_knap(self):
        arcade.draw_rectangle_outline(400, 520, self.knap_bredde, self.knap_hoejde, arcade.csscolor.BLACK, 2)
        arcade.draw_circle_filled(400, 520, 24, arcade.csscolor.RED)

    def tegn_hvid_fugl_knap(self):
        arcade.draw_rectangle_outline(400, 420, self.knap_bredde, self.knap_hoejde, arcade.csscolor.BLACK, 2)
        arcade.draw_circle_filled(400, 420, 24, arcade.csscolor.WHITE)

    def tegn_blaa_fugl_knap(self):
        arcade.draw_rectangle_outline(400, 320, self.knap_bredde, self.knap_hoejde, arcade.csscolor.BLACK, 2)
        arcade.draw_circle_filled(400, 320, 24, arcade.csscolor.BLUE)

    def tjek_knap_klik(self, koordinat):
        klik_x, klik_y = koordinat
        if klik_x >= 320 and klik_x <= 480:
            for i in range(self.knap_antal):
                knap_y_min = 470-100*i
                knap_y_max = 570-100*i
                if klik_y >= knap_y_min and klik_y <= knap_y_max:
                    return i
        return None

    def tegn(self):
        self.tegn_rød_fugl_knap()
        self.tegn_hvid_fugl_knap()
        self.tegn_blaa_fugl_knap()

class Vindue(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.csscolor.LIGHT_SKY_BLUE)
        self.fugl_valgt = False
        self.fugl = None
        self.fugl_type = None
        self.fugle = {"0": Roed_Fugl, "1": Hvid_Fugl, "2": Blaa_Fugl}
        self.menu = Menu()

    def setup(self):
        self.slangebosse = Slangebosse((100, 100))

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE and self.fugl_valgt and self.fugl.fugl_affyret:
            if self.fugl_type == 1:
                # Hvid hoppe fugl
                haeldning_x = math.cos(self.fugl.vinkel)*self.fugl.hastighed
                haeldning_y = -self.fugl.tyngdeacceleration*self.fugl.tid+self.fugl.hastighed*math.sin(self.fugl.vinkel)
                hastighed = math.sqrt(haeldning_x**2+haeldning_y**2)
                vinkel = math.atan(haeldning_y/haeldning_x)

                self.fugl.ny_parabel(self.fugl.koordinat, ((math.pi/2)-math.fabs(vinkel)), hastighed+100)
            elif self.fugl_type == 2:
                # Blå flerdelende fugl
                if len(self.fugl.under_fugle) < 3:
                    haeldning_x = math.cos(self.fugl.vinkel) * self.fugl.hastighed
                    haeldning_y = -self.fugl.tyngdeacceleration * self.fugl.tid + self.fugl.hastighed * math.sin(self.fugl.vinkel)
                    hastighed = math.sqrt(haeldning_x ** 2 + haeldning_y ** 2)
                    for i in range(3):
                        vinkel = math.atan(haeldning_y/haeldning_x)+i*(math.pi/6)-math.pi/6
                        self.fugl.skab_under_fugl(vinkel, hastighed)
    def on_mouse_drag(self, x: int, y: int, dx: int, dy: int, buttons: int, modifiers: int):
        if self.fugl_valgt and not self.fugl.fugl_affyret:
            self.slangebosse.update((x, y))
            self.fugl.koordinat = (x, y)
    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if self.fugl_valgt and not self.fugl.fugl_affyret:
            delta_x = x-self.fugl.start_x
            delta_y = y-self.fugl.start_y
            haeldning = delta_y/delta_x
            afstand = math.sqrt(delta_x**2+delta_y**2)
            vinkel = math.atan(haeldning)
            if vinkel <= math.pi/2.5:  # pi/2.5 radianer svarer til 72 grader

                if afstand >= MAX_AFSTAND:
                    afstand = MAX_AFSTAND

                if delta_x > 0:
                    afstand = -afstand

                self.fugl.ny_parabel((x, y), vinkel, afstand*2)
                self.fugl.fugl_affyret = True
            else:
                self.fugl.koordinat = (self.fugl.start_x, self.fugl.start_y)
        elif not self.fugl_valgt:
            knap = self.menu.tjek_knap_klik((x, y))
            if knap != None:
                self.fugl_type = knap
                self.fugl_valgt = True

                self.fugl = self.fugle.get(str(knap))((100, 100), 0, 0, sporlaengde=200)

    def update(self, delta_time: float):
        if self.fugl_valgt:
            self.fugl.opdater(delta_time)

    def on_draw(self):
        self.clear()
        if self.fugl_valgt:
            self.fugl.tegn()
            self.slangebosse.tegn()
        else:
            self.menu.tegn()

def main():
    vindue = Vindue(800, 600, "Angry birds fugle")
    vindue.setup()

    arcade.run()

if __name__ == "__main__":
    main()