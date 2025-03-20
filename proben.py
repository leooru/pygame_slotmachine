import pygame
import random
import time
import sys
from result import CreateResults
from settings import *



"""
TODO

-einsatz erstellen->auf fenster zeichnen
-pause menu erstellen
"""

pygame.init()
pygame.mixer.init()


scene = "menu"
rendered_text = None
exist_error = True
check_text = True # falls es schon ein Fehlermeldung bei Einsatz setzen gibt
min_max = []


user_input= 0


def render_text(text, color, x, y, size):
    global rendered_text
    font_x = pygame.font.SysFont(None, size)
    rendered_text = font_x.render(text, True, color)
    fenster.blit(rendered_text, (x, y))

icon_dict = {
    "apple": pygame.transform.scale(pygame.image.load("Assets/icons/apple.png"), icon_size),
    "banana": pygame.transform.scale(pygame.image.load("Assets/icons/banana.png"), icon_size),
    "book": pygame.transform.scale(pygame.image.load("Assets/icons/book.png"), icon_size),
    "cherry": pygame.transform.scale(pygame.image.load("Assets/icons/cherry.png"), icon_size),
    "seven": pygame.transform.scale(pygame.image.load("Assets/icons/seven.png"), icon_size)
}


fenster = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = pygame.display.get_surface().get_size()

pygame.mixer.music.load('Assets/original_spin_sound.mp3')#spin sound laden

start_image = pygame.image.load("Assets/spin_bg.png")#spin background laden
start_image = pygame.transform.scale(start_image, (screen_width, screen_height))# anpassen an bildschirm
fenster.blit(start_image, (0, 0))#zeichnen

bg_image = pygame.image.load("Assets/menu_bg.png")#menu background laden
bg_image = pygame.transform.scale(bg_image, (screen_width, screen_height))# anpassen an bildschirm

class Slotmachine:

    def __init__(self): # Konstruktor
        self.entry = 0
        self.wallet = 500
        self.__maxspin = 7
        self.icons = ["apple", "banana", "book", "cherry", "seven"]
        self.__icon_proba = [0.30, 0.15, 0.20, 0.25, 0.10]
        self.icon1 = None
        self.icon2 = None
        self.icon3 = None
        self.icon4 = None
        self.min = 20
        self.janein = []
        self.icon_names = []
        self.eval_return = []
        self.last_won= 0

    def get_random_icon(self): # sucht random icons raus
        return random.choices(self.icons, weights=self.__icon_proba, k=1)[0]

    def spinning(self): # drehen der icons
        pygame.mixer.music.play()
        a = 1
        b = 1
        c = 1
        d = 1
        self.wallet_update()
        while a < self.__maxspin:
            fenster.blit(start_image, (0, 0))
            self.icon1 = icon_dict[slot.get_random_icon()]
            self.icon2 = icon_dict[slot.get_random_icon()]
            self.icon3 = icon_dict[slot.get_random_icon()]
            self.icon4 = icon_dict[slot.get_random_icon()]

            # icons auf fenster zeichnen
            fenster.blit(self.icon1, (430, 500))
            fenster.blit(self.icon2, (730, 500))
            fenster.blit(self.icon3, (1030, 500))
            fenster.blit(self.icon4, (1330, 500))
            a += 1
            time.sleep(0.1)
            overlay()
            pygame.display.flip()

        while b < self.__maxspin:
            fenster.blit(start_image, (0, 0))
            self.icon2 = icon_dict[slot.get_random_icon()]
            self.icon3 = icon_dict[slot.get_random_icon()]
            self.icon4 = icon_dict[slot.get_random_icon()]

            # icons auf fenster zeichnen
            fenster.blit(self.icon1, (430, 500))
            fenster.blit(self.icon2, (730, 500))
            fenster.blit(self.icon3, (1030, 500))
            fenster.blit(self.icon4, (1330, 500))
            b += 1
            time.sleep(0.1)
            overlay()
            pygame.display.flip()

        while c < self.__maxspin:
            fenster.blit(start_image, (0, 0))
            self.icon3 = icon_dict[slot.get_random_icon()]
            self.icon4 = icon_dict[slot.get_random_icon()]

            # icons auf fenster zeichnen
            fenster.blit(self.icon1, (430, 500))
            fenster.blit(self.icon2, (730, 500))
            fenster.blit(self.icon3, (1030, 500))
            fenster.blit(self.icon4, (1330, 500))
            c += 1
            time.sleep(0.1)
            overlay()
            pygame.display.flip()

        while d < self.__maxspin:
            fenster.blit(start_image, (0, 0))
            self.icon4 = icon_dict[slot.get_random_icon()]

            # icons auf fenster zeichnen
            fenster.blit(self.icon1, (430, 500))
            fenster.blit(self.icon2, (730, 500))
            fenster.blit(self.icon3, (1030, 500))
            fenster.blit(self.icon4, (1330, 500))
            d += 1
            time.sleep(0.1)
            overlay()
            pygame.display.flip()
    def last_icons(self):
        if self.icon1 is not None and self.icon2 is not None and self.icon3 is not None and self.icon4 is not None:
            fenster.blit(self.icon1, (430, 500))
            fenster.blit(self.icon2, (730, 500))
            fenster.blit(self.icon3, (1030, 500))
            fenster.blit(self.icon4, (1330, 500))
        else:
            pass

    def wallet_update(self):
        self.wallet -= self.entry

    def rend_min_max(self):
        global exist_error, check_text
        render_text(f"min: {self.min}", WHITE, 320, 470, 35)
        check_text = False
        exist_error = True
        pygame.display.flip()
    def game_update(self):
        fenster.blit(start_image, (0, 0))
        self.last_icons()

slot = Slotmachine()
cres = CreateResults(icon_dict)
def create_button(x, y, w, h, color, alignment):
    button_input = pygame.Rect(x, y, w, h)
    if alignment == "curved":
        pygame.draw.rect(fenster, color, button_input, border_radius=10)
    elif alignment == "straight":
        pygame.draw.rect(fenster, color, button_input)
    else:
        print("Alignment error!")

def entry_check(min):
    global user_text, check_text, exist_error, user_input  # Variablen sind global


    try:
        user_input = int(user_text)  # In Integer umwandeln

        if user_input > slot.wallet:  # Prüfen, ob der Einsatz größer als das Wallet ist
            render_text("Du kannst nicht mehr setzen als du hast!", WHITE, 320, 370, 35)
            slot.rend_min_max()
            check_text = False
            exist_error = True
            pygame.display.flip()
            return False

        elif user_input < min: # prüfen ob Einsatz kleiner ist als minimum
            render_text("Du musst mindestens 20 ayris haben als Einsatz!", WHITE, 320, 370, 35)
            slot.rend_min_max()
            check_text = False
            exist_error = True
            pygame.display.flip()
            return False


        elif user_input > 0:
            slot.entry = user_input
            return True

        else:
            if exist_error:
                render_text("Du musst einen positiven Einsatz haben!", WHITE, 320, 370, 35)
                slot.rend_min_max()
                pygame.display.flip()
                check_text = False
                exist_error = True
                return False
    except ValueError:
        if exist_error:
            render_text("Du musst eine Zahl eingeben!", WHITE, 320, 370, 35)
            slot.rend_min_max()
            check_text = False
            exist_error = True
            pygame.display.flip()
            return False


def overlay():
    create_button(346, 260, 1243, 60, BLACK, "straight")
    render_text("Einsatz: " + str(slot.entry), WHITE, 350, 275, 50)
    render_text("Wallet: " + str(slot.wallet), WHITE, 680, 275, 50)
    render_text("Letzter Gewinn: " + str(slot.last_won), WHITE, 1010, 275, 50)

def space_taste():
    """
    aktionscode
    hier wird gesagt was passiert beim Drücken der Leertaste
    """
    if slot.wallet > 0:
        slot.icon_names.clear()
        slot.janein.clear()
        slot.eval_return.clear()
        fenster.blit(start_image, (0, 0))
        slot.spinning()
        slot.janein.extend(cres.amount_combination(slot.icon1, slot.icon2, slot.icon3,slot.icon4)) # amount_icon_number von result.py wird benutzt für die Auswertung
        for y in slot.janein:
            print(f" {y}")
        slot.icon_names.extend(cres.get_icon_name(slot.icon1, slot.icon2, slot.icon3, slot.icon4))
        for i in slot.icon_names:
            print(i)
        slot.eval_return.extend(cres.evalutation(slot.janein[0],slot.janein[1],slot.janein[2],slot.janein[3], slot.icon_names[0], slot.icon_names[1], slot.icon_names[2], slot.icon_names[3],slot.wallet, slot.entry))
        slot.wallet = slot.eval_return[0]
        slot.last_won = slot.eval_return[1]
        print(f"{slot.eval_return[1]}")
        slot.game_update()
        pygame.display.flip()

    else:
        #hier kann dann dass wenn man kein geld mehr halt also wallet leer
        print("Du musst einen Einsatz haben!")
    
while True:
    global user_text
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if scene == "menu":
                if event.unicode.isdigit():  # Überprüfen, ob es eine Ziffer ist, denn bei Einsatz dürfen nur Zahlen drin sein
                    user_text += event.unicode
                    user_text = user_text[:5]
                elif event.key == pygame.K_BACKSPACE:  # Backspace-Taste zum Löschen
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:  # Enter-Taste zum Bestätigen
                    print("Eingegebene Zahl:", user_text)
            if event.key == pygame.K_ESCAPE: # escape-Taste zum Wechseln zwischen Menü und Game
                if scene == "menu":
                    if exist_error:
                        fenster.blit(bg_image, (0, 0))
                    if entry_check(slot.min): # falls funktion True zurück gibt, wechselt es zum game
                        scene = "game"
                        fenster.blit(start_image, (0, 0))
                        slot.last_icons()
                        overlay()
                        pygame.display.flip()
                else:
                    scene = "menu"
                    check_text = True
            elif event.key == pygame.K_F8:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_SPACE: # Spinnen der Icons
                if scene == "game":
                    space_taste()
                    overlay()

    if scene == "menu":
        if check_text:
            #Hintergrundbild menu
            fenster.blit(bg_image, (0, 0))
            slot.rend_min_max()

        render_text("Menü", WHITE, 790, 200, 160)

        create_button(320, 600, 400, 50, WHITE, "curved") # flächen für einsatz
        render_text("Einsatz:", BLACK, 320, 600, 80)
        create_button(1170, 600, 400,  50, WHITE, "curved")
        render_text(f"Wallet: {slot.wallet}", BLACK, 1170, 600, 80)
        create_button(320, 760, 400, 50, WHITE, "curved")
        render_text("Bitte Einsatz eingeben:", CYAN, 320, 560, 40)
        render_text(user_text, BLACK, 570, 605, 70)



    pygame.display.flip()
