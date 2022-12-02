import arcade
import math


MAX_AFSTAND = 100

MENU_KNAP_CENTRUM_X = 770
MENU_KNAP_CENTRUM_Y = 570
MENU_KNAP_BREDDE = 60
MENU_KNAP_HOEJDE = 60

class Slangebosse:
    def __init__(self, start_position):
        self.position = start_position
        self.mus_position = start_position
    def update(self, mouse_position):
        self.mus_position = mouse_position  # Ville bruge mus-position til at tegne elastikken. Naar jeg ikke.
    def tegn(self):
        arcade.draw_rectangle_outline(*self.position, 40, 80, arcade.csscolor.BROWN, 5)
        # Her havde jeg så også taenkt mig at forbedre slangeboessens udseende. Det naar jeg ikke.

class Roed_Gul_Fugl():
    def __init__(self, start_koordinat, vinkel, start_hastighed, tyngdeacceleration=70, sporlaengde=100, type=0):
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
        if type == 0:  # Tjekker om det er den røde eller gule fugl.
            self.farve = arcade.csscolor.RED
        else:
            self.farve = arcade.csscolor.YELLOW

    def opdater(self, delta_tid):
        x_fugl, y_fugl = self.koordinat
        hastighed_y = -self.tyngdeacceleration * self.tid + self.hastighed * math.sin(self.vinkel)
        if self.fugl_affyret and (y_fugl > 60 or hastighed_y > 0):  # Tjekker at fuglen er affyret, og ikke er under jorden/bliver under jorden.
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
        arcade.draw_circle_filled(x, y, 8, self.farve)
        for punkt in self.spor:
            arcade.draw_circle_filled(*punkt, 3, self.farve)

class Hvid_Fugl():
    def __init__(self, start_koordinat, vinkel, start_hastighed, tyngdeacceleration=70, sporlaengde=100, type=1):
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
        self.ekstra_vektor_y = 0

    def opdater(self, delta_tid):
        x_fugl, y_fugl = self.koordinat
        hastighed_y = -self.tyngdeacceleration * self.tid + self.hastighed * math.sin(self.vinkel)
        if self.fugl_affyret and (y_fugl > 60 or hastighed_y > 0):  # Tjekker at fuglen er affyret, og ikke er under jorden/bliver under jorden.
            self.tid += delta_tid
            x = self.hastighed * math.cos(self.vinkel) * self.tid + self.start_x
            y = -(1 / 2) * self.tyngdeacceleration * self.tid ** 2 + self.hastighed * math.sin(
                self.vinkel) * self.tid + self.ekstra_vektor_y * self.tid + self.start_y
            self.koordinat = (x, y)
            self.spor.append(self.koordinat)
            if len(self.spor) > self.sporlaengde:
                self.spor.pop(0)

    def ny_parabel(self, start_koordinat, vinkel, start_hastighed, tyngdeacceleration=70, skub_vektor_y=0):
        if not self.har_aktiveret:
            self.start_x, self.start_y = start_koordinat
            self.tid = 0
            self.vinkel = vinkel
            self.hastighed = start_hastighed
            self.tyngdeacceleration = tyngdeacceleration
            self.ekstra_vektor_y = skub_vektor_y
            if self.fugl_affyret:
                self.har_aktiveret = True

    def tegn(self):
        x, y = self.koordinat
        arcade.draw_circle_filled(x, y, 8, arcade.csscolor.WHITE)
        for punkt in self.spor:
            arcade.draw_circle_filled(*punkt, 3, arcade.csscolor.WHITE)

class Blaa_Fugl():
    def __init__(self, start_koordinat, vinkel, start_hastighed, tyngdeacceleration=70, sporlaengde=100, lille=False, type=2):
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
        self.lille_stoerrelse = lille  # Hvis den er True, er det en lille fugl.
        self.under_fugle = list()  # De små fugle

    def opdater(self, delta_tid):
        x_fugl, y_fugl = self.koordinat
        hastighed_y = -self.tyngdeacceleration * self.tid + self.hastighed * math.sin(self.vinkel)
        if self.fugl_affyret and (y_fugl > 60 or hastighed_y > 0):  # Tjekker at fuglen er affyret, og ikke er under jorden/bliver under jorden.
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
        self.lille_stoerrelse = True

    def tegn(self):
        x, y = self.koordinat
        if self.lille_stoerrelse:  # Hvis fuglen er delt i tre, skal fuglene(cirklerne) også vaere mindre.
            arcade.draw_circle_filled(x, y, 5, arcade.csscolor.BLUE)
        else:
            arcade.draw_circle_filled(x, y, 8, arcade.csscolor.BLUE)

        for punkt in self.spor:
            arcade.draw_circle_filled(*punkt, 3, arcade.csscolor.BLUE)
        for under_fugl in self.under_fugle:  # Hvis fuglen har delt sig i tre, er laengden af self.under_fugle > 0.
            under_fugl.tegn()

class Menu:
    def __init__(self):
        self.knap_antal = 4
        self.knap_bredde = 120
        self.knap_hoejde = 80

    def tegn_roed_fugl_knap(self):
        arcade.draw_rectangle_outline(400, 520, self.knap_bredde, self.knap_hoejde, arcade.csscolor.BLACK, 2)
        arcade.draw_circle_filled(400, 520, 24, arcade.csscolor.RED)

    def tegn_hvid_fugl_knap(self):
        arcade.draw_rectangle_outline(400, 420, self.knap_bredde, self.knap_hoejde, arcade.csscolor.BLACK, 2)
        arcade.draw_circle_filled(400, 420, 24, arcade.csscolor.WHITE)

    def tegn_blaa_fugl_knap(self):
        arcade.draw_rectangle_outline(400, 320, self.knap_bredde, self.knap_hoejde, arcade.csscolor.BLACK, 2)
        arcade.draw_circle_filled(400, 320, 24, arcade.csscolor.BLUE)

    def tegn_gul_fugl_knap(self):
        arcade.draw_rectangle_outline(400, 220, self.knap_bredde, self.knap_hoejde, arcade.csscolor.BLACK, 2)
        arcade.draw_circle_filled(400, 220, 24, arcade.csscolor.YELLOW)

    def tegn_tekst(self):
        arcade.draw_text("Tryk på en fugl(cirkel) for at vælge den\n\nHold venstre musseknap nede, træk i modsatte retning af hvor du vil skyde hen og slip for at affyre fuglen\n\nTryk på space for at aktivere fuglen", 25, 400, width=300, multiline=True, bold=True)

    def tjek_knap_klik(self, koordinat):
        klik_x, klik_y = koordinat
        if klik_x >= 320 and klik_x <= 480:  # har man trykket indenfor det korrekte x-interval.
            for i in range(self.knap_antal):
                knap_y_min = 470-100*i
                knap_y_max = 570-100*i
                if klik_y >= knap_y_min and klik_y <= knap_y_max:  # Har man trykket indenfor det korrekte y-interval for den specifikke knap.
                    return i
        return None

    def tegn(self):
        self.tegn_roed_fugl_knap()
        self.tegn_hvid_fugl_knap()
        self.tegn_blaa_fugl_knap()
        self.tegn_gul_fugl_knap()
        self.tegn_tekst()

class Vindue(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.csscolor.LIGHT_SKY_BLUE)
        self.fugl_valgt = False
        self.fugl = None
        self.fugl_type = None
        self.fugle = {"0": Roed_Gul_Fugl, "1": Hvid_Fugl, "2": Blaa_Fugl, "3": Roed_Gul_Fugl} # dict, der faar menu-knapper til at fungere
        self.menu = Menu()

    def setup(self):
        self.slangebosse = Slangebosse((100, 100))

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE and self.fugl_valgt and self.fugl.fugl_affyret: # Hvis man trykker på mellemrum for at aktivere fuglens specielle evne, og fuglen er blevet affyret.
            if self.fugl_type == 1:
                # Hvid hoppe fugl
                hastighed_x = math.cos(self.fugl.vinkel)*self.fugl.hastighed
                hastighed_y = -self.fugl.tyngdeacceleration*self.fugl.tid+self.fugl.hastighed*math.sin(self.fugl.vinkel)
                hastighed = math.sqrt(hastighed_x**2+hastighed_y**2)
                vinkel = math.atan(hastighed_y/hastighed_x)

                if hastighed_x <= 0:
                    vinkel += math.pi

                if hastighed_y < 0:
                    ekstra_vektor_y = math.fabs(hastighed_y) + 100
                else:
                    ekstra_vektor_y = 100

                self.fugl.ny_parabel(self.fugl.koordinat, vinkel, hastighed, skub_vektor_y=ekstra_vektor_y)
            elif self.fugl_type == 2:
                # Blå flerdelende fugl
                if len(self.fugl.under_fugle) < 3:  # Hvis den ikke allerede har aktiveret.
                    hastighed_x = math.cos(self.fugl.vinkel) * self.fugl.hastighed
                    hastighed_y = -self.fugl.tyngdeacceleration * self.fugl.tid + self.fugl.hastighed * math.sin(self.fugl.vinkel)
                    hastighed = math.sqrt(hastighed_x ** 2 + hastighed_y ** 2)
                    for i in range(3):
                        vinkel = math.atan(hastighed_y/hastighed_x)+(i-1)*(math.pi/6)
                        if hastighed_x <= 0:  # Sikrer at man bevæger sig i de korrekte retning ift. x-aksen.
                            vinkel += math.pi
                        self.fugl.skab_under_fugl(vinkel, hastighed)
            elif self.fugl_type == 3:
                # Gul hurtig fugl
                hastighed_x = math.cos(self.fugl.vinkel) * self.fugl.hastighed
                hastighed_y = -self.fugl.tyngdeacceleration * self.fugl.tid + self.fugl.hastighed * math.sin(self.fugl.vinkel)
                hastighed = math.sqrt(hastighed_x ** 2 + hastighed_y ** 2)
                vinkel = math.atan(hastighed_y / hastighed_x)

                if hastighed_x <= 0:
                    vinkel += math.pi

                self.fugl.ny_parabel(self.fugl.koordinat, vinkel, hastighed + 100, tyngdeacceleration=35)

    def on_mouse_drag(self, x: int, y: int, dx: int, dy: int, buttons: int, modifiers: int):
        if self.fugl_valgt and not self.fugl.fugl_affyret:
            self.slangebosse.update((x, y)) # Dette var ment til at skabe elastikken. Det naaede jeg ikke.
            delta_x = x - self.fugl.start_x
            delta_y = y - self.fugl.start_y
            afstand = math.sqrt(delta_x**2+delta_y**2)
            if afstand <= MAX_AFSTAND:
                self.fugl.koordinat = (x, y)
            else:
                x_cirkel = delta_x/afstand*100+self.fugl.start_x
                y_cirkel = delta_y/afstand*100+self.fugl.start_y

                self.fugl.koordinat = (x_cirkel, y_cirkel)

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int):
        if x <= MENU_KNAP_CENTRUM_X+MENU_KNAP_BREDDE/2 and x >= MENU_KNAP_CENTRUM_X-MENU_KNAP_BREDDE/2 and y <= MENU_KNAP_CENTRUM_Y+MENU_KNAP_HOEJDE/2 and y >= MENU_KNAP_CENTRUM_Y-MENU_KNAP_HOEJDE/2:
        # ^ tjekker om man har trykket oppe på menu-knappen øverst i højre hjørne.
            self.fugl = None
            self.fugl_type = None
            self.fugl_valgt = False
        else:
            if self.fugl_valgt and not self.fugl.fugl_affyret:
                fugl_x, fugl_y = self.fugl.koordinat  # Fuglens koordinat svarer til der, hvor fuglen er trukket tilbage til, indenfor slangeboessens raekkevidde.

                delta_x = fugl_x-self.fugl.start_x
                delta_y = fugl_y-self.fugl.start_y
                hastighed = delta_y/delta_x
                afstand = math.sqrt(delta_x**2+delta_y**2)
                vinkel = math.atan(hastighed)

                if math.ceil(afstand) >= MAX_AFSTAND:
                    #x = delta_x / afstand + fugl_x
                    #y = delta_y / afstand + fugl_y
                    x = fugl_x
                    y = fugl_y

                if delta_x > 0:
                    vinkel += math.pi

                self.fugl.ny_parabel((x, y), vinkel, afstand*2)
                self.fugl.fugl_affyret = True

            elif not self.fugl_valgt:
                knap = self.menu.tjek_knap_klik((x, y))
                if knap != None: # knappen kan returnere 0, som behandles som false. Derfor tjekker den om knappen ikke er None, men hvis den returnerer 0, bliver conditionen true.
                    self.fugl_type = knap
                    self.fugl_valgt = True
                    self.fugl = self.fugle.get(str(knap))((100, 100), 0, 0, sporlaengde=200, type=knap)

    def update(self, delta_time: float):
        if self.fugl_valgt:
            self.fugl.opdater(delta_time)

    def on_draw(self):
        self.clear()
        if self.fugl_valgt:
            # tegn jorden
            arcade.draw_rectangle_filled(400, 25, 800, 55, arcade.color.BROWN)
            arcade.draw_rectangle_filled(400, 55, 800, 10, arcade.color.GREEN)

            # tegn fugl og slangebosse
            self.fugl.tegn()
            self.slangebosse.tegn()

            # gaa til menu knappen oeverst i hoejre hjoerne
            arcade.draw_rectangle_outline(MENU_KNAP_CENTRUM_X, MENU_KNAP_CENTRUM_Y, MENU_KNAP_BREDDE, MENU_KNAP_HOEJDE, arcade.csscolor.BROWN, 2)
            for i in range(3):
                arcade.draw_rectangle_filled(MENU_KNAP_CENTRUM_X, MENU_KNAP_CENTRUM_Y+(12+5)-i*17, 40, 12, arcade.csscolor.BROWN)
        else:
            self.menu.tegn()

def main():
    vindue = Vindue(800, 600, "Angry birds fugle")
    vindue.setup()

    arcade.run()

if __name__ == "__main__":
    main()
