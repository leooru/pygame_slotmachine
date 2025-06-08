#!/usr/bin/env python3

import pygame
import random
import time
import sys
from result import CreateResults
from settings import *
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

pygame.init()
pygame.mixer.init()
pygame.mouse.set_visible(False)

scene = "start"
rendered_text = None
exist_error = True
check_text = True # if there's already an error at Entry
min_max = []
button_start = None
button_gambling = None
button_overview = None
button_play = None
button_backmenu = None
var_money_scan = "0"
user_input= 0
neu_input = ""
scan_mode = 0
updated_value = 0
new_text = ""
plus_pressed_time = None
plus_hold_duration = 2000

def create_button_start(x, y, w, h, color, alignment):
    global button_start
    button_start = pygame.Rect(x, y, w, h)
    if alignment == "curved":
        pygame.draw.rect(fenster, color, button_start, border_radius=15)
    elif alignment == "straight":
        pygame.draw.rect(fenster, color, button_start)
    else:
        print("Alignment error!")

def create_button(x, y, w, h, color, alignment):
    button_input = pygame.Rect(x, y, w, h)
    if alignment == "curved":
        pygame.draw.rect(fenster, color, button_input, border_radius=15)
    elif alignment == "straight":
        pygame.draw.rect(fenster, color, button_input)
    else:
        print("Alignment error!")

def create_button_backmenu(x, y, w, h, color, alignment):
    global button_backmenu
    button_backmenu = pygame.Rect(x, y, w, h)
    if alignment == "curved":
        pygame.draw.rect(fenster, color, button_backmenu, border_radius=15)
    elif alignment == "straight":
        pygame.draw.rect(fenster, color, button_backmenu)
    else:
        print("Alignment error!")

def create_button_gambling(x, y, w, h, color, alignment):
    global button_gambling
    button_gambling = pygame.Rect(x, y, w, h)
    if alignment == "curved":
        pygame.draw.rect(fenster, color, button_gambling, border_radius=15)
    elif alignment == "straight":
        pygame.draw.rect(fenster, color, button_gambling)
    else:
        print("Alignment error!")

def create_button_overview(x, y, w, h, color, alignment):
    global button_overview
    button_overview = pygame.Rect(x, y, w, h)
    if alignment == "curved":
        pygame.draw.rect(fenster, color, button_overview, border_radius=15)
    elif alignment == "straight":
        pygame.draw.rect(fenster, color, button_overview)
    else:
        print("Alignment error!")
def create_button_play(x, y, w, h, color, alignment):
    global button_play
    button_play = pygame.Rect(x, y, w, h)
    if alignment == "curved":
        pygame.draw.rect(fenster, color, button_play, border_radius=15)
    elif alignment == "straight":
        pygame.draw.rect(fenster, color, button_play)
    else:
        print("Alignment error!")

fenster = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = pygame.display.get_surface().get_size()

pygame.mixer.music.load('Assets/original_spin_sound.mp3')#load spin sound

start_image = pygame.image.load("Assets/spin_bg.png")#load spin background
start_image = pygame.transform.scale(start_image, (screen_width, screen_height))# adapt to screen
fenster.blit(start_image, (0, 0))#draw

bg_image = pygame.image.load("Assets/menu_bg.png")#load menu background
bg_image = pygame.transform.scale(bg_image, (screen_width, screen_height))# adapt to screen

bg_overview = pygame.image.load("Assets/overview_bg.png")#load overview background
bg_overview = pygame.transform.scale(bg_overview, (screen_width, screen_height))

bg_green = pygame.image.load("Assets/green_bg.jpg")
bg_green = pygame.transform.scale(bg_green, (screen_width, screen_height))

class Slotmachine:

    def __init__(self): # constructor
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

    def get_random_icon(self): # get random icons
        return random.choices(self.icons, weights=self.__icon_proba, k=1)[0]

    def spinning(self): # spin the icons
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

            # draw icons on window
            fenster.blit(self.icon1, (235, 265))
            fenster.blit(self.icon2, (390, 265))
            fenster.blit(self.icon3, (545, 265))
            fenster.blit(self.icon4, (700, 265))
            a += 1
            time.sleep(0.1)
            overlay()
            pygame.display.flip()

        while b < self.__maxspin:
            fenster.blit(start_image, (0, 0))
            self.icon2 = icon_dict[slot.get_random_icon()]
            self.icon3 = icon_dict[slot.get_random_icon()]
            self.icon4 = icon_dict[slot.get_random_icon()]

            # draw icons on window
            fenster.blit(self.icon1, (235, 265))
            fenster.blit(self.icon2, (390, 265))
            fenster.blit(self.icon3, (545, 265))
            fenster.blit(self.icon4, (700, 265))
            b += 1
            time.sleep(0.1)
            overlay()
            pygame.display.flip()

        while c < self.__maxspin:
            fenster.blit(start_image, (0, 0))
            self.icon3 = icon_dict[slot.get_random_icon()]
            self.icon4 = icon_dict[slot.get_random_icon()]

            # draw icons on window
            fenster.blit(self.icon1, (235, 265))
            fenster.blit(self.icon2, (390, 265))
            fenster.blit(self.icon3, (545, 265))

            fenster.blit(self.icon4, (700, 265))
            c += 1
            time.sleep(0.1)
            overlay()
            pygame.display.flip()

        while d < self.__maxspin:
            fenster.blit(start_image, (0, 0))
            self.icon4 = icon_dict[slot.get_random_icon()]

            # draw icons on window
            fenster.blit(self.icon1, (235, 265))
            fenster.blit(self.icon2, (390, 265))
            fenster.blit(self.icon3, (545, 265))
            fenster.blit(self.icon4, (700, 265))
            d += 1
            time.sleep(0.1)
            overlay()
            pygame.display.flip()
    def last_icons(self):
        if self.icon1 is not None and self.icon2 is not None and self.icon3 is not None and self.icon4 is not None:
            fenster.blit(self.icon1, (235, 265))
            fenster.blit(self.icon2, (390, 265))
            fenster.blit(self.icon3, (545, 265))
            fenster.blit(self.icon4, (700, 265))
        else:
            pass

    def wallet_update(self):
        self.wallet -= self.entry

    def rend_min_max(self):
        global exist_error, check_text
        render_text(f"min: {self.min}", WHITE, 120, 170, 25, fenster, rendered_text)
        check_text = False
        exist_error = True
        pygame.display.flip()
    def game_update(self):
        fenster.blit(start_image, (0, 0))
        self.last_icons()




slot = Slotmachine()
cres = CreateResults(icon_dict)


def entry_check(min):
    global user_text, check_text, exist_error, user_input  # variables are global


    try:
        user_input = int(user_text)  # convert into integer

        if user_input > slot.wallet:  # check if entry is bigger than the wallet
            render_text("Du kannst nicht mehr setzen als du hast!", WHITE, 120, 300, 35, fenster, rendered_text)
            slot.rend_min_max()
            check_text = False
            exist_error = True
            pygame.display.flip()
            return False #returns for clean end of function

        elif user_input < min: # check if entry is less than minimum
            render_text("Du musst mindestens 20 EURO haben als Einsatz!", WHITE, 120, 300, 35, fenster, rendered_text)
            slot.rend_min_max()
            check_text = False
            exist_error = True
            pygame.display.flip()
            return False


        elif user_input > 0: # check if there is any entry
            slot.entry = user_input
            return True

        else:
            if exist_error:
                render_text("Du musst einen positiven Einsatz haben!", WHITE, 120, 300, 35, fenster, rendered_text)
                slot.rend_min_max()
                pygame.display.flip()
                check_text = False
                exist_error = True
                return False
    except ValueError:
        if exist_error:
            render_text("Du musst eine Zahl eingeben!", WHITE, 120, 300, 35, fenster, rendered_text)
            slot.rend_min_max()
            check_text = False
            exist_error = True
            pygame.display.flip()
            return False


def overlay(): #standard overlay
    create_button(185, 125, 663, 40, BLACK, "straight")
    render_text("Einsatz: " + str(slot.entry), GREEN, 185, 130, 35, fenster, rendered_text)
    render_text("Wallet: " + str(slot.wallet), GREEN, 355, 130, 35, fenster, rendered_text)
    render_text("Letzter Gewinn: " + str(slot.last_won), GREEN, 520, 130, 35, fenster, rendered_text)

def money_error():
    render_text("Du kannst nicht mehr abheben", RED, 340, 410, 40, fenster, rendered_text)

def new_wallet():
    slot.wallet = int(new_text)

def space_taste():
    """
    in this function, everything is happening when the spacebar is pressed
    """
    if slot.wallet > 0:
        slot.icon_names.clear()
        slot.janein.clear()
        slot.eval_return.clear()
        fenster.blit(start_image, (0, 0))
        slot.spinning()
        slot.janein.extend(cres.amount_combination(slot.icon1, slot.icon2, slot.icon3,slot.icon4)) #  amount_icon_number will be used by result.py for the evalutation
        for y in slot.janein:
            print(f" {y}")
        slot.icon_names.extend(cres.get_icon_name(slot.icon1, slot.icon2, slot.icon3, slot.icon4))
        for i in slot.icon_names:
            print(i)
        slot.eval_return.extend(cres.evalutation(slot.janein[0],slot.janein[1],slot.janein[2],slot.janein[3],
                                                 slot.icon_names[0], slot.icon_names[1], slot.icon_names[2],
                                                 slot.icon_names[3],slot.wallet, slot.entry))
        slot.wallet = slot.eval_return[0]
        slot.last_won = slot.eval_return[1]
        print(f"{slot.eval_return[1]}")
        slot.game_update()
        pygame.display.flip()

    else:
        #hier kann dann dass wenn man kein geld mehr halt also wallet leer
        render_text("Du Hast kein Geld mehr!", BLUE, 150, 450, 35, fenster, rendered_text)
        print("Du musst einen Einsatz haben!")

while True:
    global user_text
    #event loop



    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if scene == "menu":
                if event.unicode.isdigit():  # check if entry is only digits, bc only digits are allowed
                    user_text += event.unicode
                    user_text = user_text[:5]
                elif event.key == pygame.K_BACKSPACE:  # backspace to delete
                    user_text = user_text[:-1]
            if scene == "scan_menu":
                if event.unicode.isdigit():  # check if entry is only digits, bc only digits are allowed
                    input_text += event.unicode
                    input_text = input_text[:4]
                    if int(input_text) > 5000:
                        input_text = "5000"

                elif event.key == pygame.K_BACKSPACE:  # backspace to delete
                    input_text = input_text[:-1]
            if scene == "afterscan_menu":
                if event.unicode.isdigit():
                    neu_input += event.unicode
                    neu_input = neu_input[:4]
                    if int(neu_input) > int(erneuerte_max):
                        neu_input = int(erneuerte_max)

            if event.key == pygame.K_KP_MINUS: # - key for switching between menu and game
                if scene != "start":
                    if scene != "menu":
                        scene = "menu"
                        check_text = True
            if event.key == pygame.K_KP_ENTER:
                if scene == "start":
                    scene = "scanbefore_menu"
                    scan_mode = 1
                elif scene == "scan_menu":
                    if int(input_text) > 5000:
                        money_error()

                    else:
                        id, moment_text = reader.read()
                        erneuerte_max = str(int(input_text)+int(moment_text))
                        reader.write(str(int(input_text)+int(moment_text)))
                        scene = "afterscan_menu"
                elif scene == "afterscan_menu":
                    """id, new_text = reader.read()
                    reader.write(str(int(new_text)-int(neu_input)))
                    scene = "menu"
                    """
                    if int(neu_input) <= int(erneuerte_max):
                        updated_value += int(erneuerte_max) - int(neu_input)
                        reader.write(str(updated_value))
                        slot.wallet = int(neu_input)
                        scene = "menu"
                    else:
                        money_error()
                        pygame.display.flip()
            if event.key == pygame.K_KP_DIVIDE:
                if scene == "menu":
                    id, value_text = reader.read()
                    neue_write = int(value_text) + slot.wallet
                    reader.write(str(neue_write))
                    scene = "start"


            elif event.key == pygame.K_KP_PLUS:
                plus_pressed_time = pygame.time.get_ticks()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_start is not None and button_start.collidepoint(event.pos):
                scene = "scanbefore_menu"
                scan_mode = 1
            elif button_gambling is not None and button_gambling.collidepoint(event.pos):
                scene = "gambling"
            elif button_overview is not None and button_overview.collidepoint(event.pos):
                scene = "overview"
            elif button_backmenu is not None and button_backmenu.collidepoint(event.pos):
                scene = "menu"
                check_text = True
            elif button_play is not None and button_play.collidepoint(event.pos):
                if scene != "start":
                    if scene == "menu":
                        if exist_error:
                            fenster.blit(bg_image, (0, 0))
                        if entry_check(slot.min): # if function returns True, it changes to the game
                            scene = "game"
                            fenster.blit(start_image, (0, 0))
                            slot.last_icons()
                            overlay()
                            pygame.display.flip()
    if GPIO.input(26) == GPIO.HIGH:
        if scene == "game":
            space_taste()
            overlay()



    if scene == "menu":
        if check_text:
            #background image menu
            fenster.blit(bg_image, (0, 0))
            slot.rend_min_max()

        render_text("Menü", WHITE, 420, 90, 90, fenster, rendered_text)

        create_button(120, 250, 300, 40, WHITE, "straight") # area for entry
        render_text("Einsatz:", BLACK, 120, 255, 45, fenster, rendered_text)
        create_button_gambling(570, 250, 300, 40, GREEN, "curved")#button glückspiel infos
        render_text("Glückspiel Infos", BLACK, 570, 255, 45, fenster, rendered_text)
        render_text("Bitte Einsatz eingeben:", CYAN, 120, 200, 30, fenster, rendered_text)
        render_text(user_text, BLACK, 240, 255, 45, fenster, rendered_text)
        create_button_overview(570, 360, 300, 40, GREEN, "curved")#button overview results
        render_text("Übersicht", BLACK, 640, 365, 45, fenster, rendered_text)
        create_button_play(350, 450, 300, 40, BLUE, "curved")
        render_text("SPIELEN", WHITE, 430, 455, 45, fenster, rendered_text)

        create_button(120, 360, 300, 40, WHITE, "straight")#area wallet570, 255, 45
        render_text(f"Wallet: {slot.wallet}", BLACK, 120, 365, 45, fenster, rendered_text)

    if scene == "start":
        # background image menu
        fenster.blit(bg_image, (0, 0))
        create_button_start(350,300, 330, 50, WHITE, "curved") # area for entry
        render_text("Drücke zum Spielen", BLACK, 350, 310, 50, fenster, rendered_text)

    if scene == "gambling":
        fenster.blit(bg_image, (0, 0))
        render_text("GLÜCKSPIEL", WHITE, 150, 150, 50, fenster, rendered_text)
        render_text("Glückspiel kann zu einer ernsthaften Sucht führen, deshalb sollte man nicht Automaten, ", WHITE, 150, 200, 26, fenster, rendered_text)
        render_text("Kartenspiele oder Wetten spielen. Dies kann ernsthafte Folgen haben, wie Verschuldungen, ", WHITE,150, 230, 26, fenster, rendered_text)
        render_text("Depressionen etc. Glücksspiele sind inzwischen jederzeit verfügbar. Und genau das wird ", WHITE,150, 260, 26, fenster, rendered_text)
        render_text("für viele Menschen ein großes Problem – egal, ob jung oder alt.Was lernen wir daraus? ", WHITE,150, 290, 26, fenster, rendered_text)
        render_text("LET'S GO GAMBLING", BLUE,150, 350, 40, fenster, rendered_text)
        create_button_backmenu(620, 400, 210, 40, GREEN, "curved")
        render_text("BACK TO MENU", WHITE, 630, 410, 35, fenster, rendered_text)

    if scene == "overview":
        fenster.blit(bg_overview, (0, 0))
        render_text("Übersicht", WHITE, 350, 90, 80, fenster, rendered_text)
        create_button_backmenu(620, 400, 210, 40, GREEN, "curved")
        render_text("BACK TO MENU", WHITE, 630, 410, 35, fenster, rendered_text)

    if scene == "afterscan_menu":
        fenster.blit(bg_green, (0, 0))
        render_text("Wie viel möchtest du in das Wallet einzahlen?", WHITE, 210, 240, 40, fenster, rendered_text)
        create_button(340, 300, 300, 50, WHITE, "straight")
        render_text(f"max: {erneuerte_max}€", RED, 340, 270, 40, fenster, rendered_text)
        render_text(neu_input, BLACK, 340, 305, 60, fenster, rendered_text)


    if scene == "scan_menu":
        fenster.blit(bg_green, (0, 0))
        create_button(340,300, 330, 50, WHITE, "straight")
        render_text("BANK", WHITE, 400, 50, 100, fenster, rendered_text)
        render_text(input_text, BLACK, 340, 305, 70, fenster, rendered_text)
        render_text("Wie viel möchtest du aufladen?", WHITE, 300, 250, 40, fenster, rendered_text)
        render_text("max: 5000€", RED, 340, 350, 40, fenster, rendered_text)
        render_text(f"Kontostand: {var_money_scan}", WHITE, 340, 380, 40, fenster, rendered_text)

    if scene == "scanbefore_menu":
        reader = SimpleMFRC522()
        fenster.blit(bg_green, (0, 0))
        render_text("Scanne erst deine Karte!", WHITE, 350, 250, 40, fenster, rendered_text)
        pygame.display.flip()
        if scan_mode == 1:
            try:
                print("Warte auf eine RFID-Karte..")
                id, var_money_scan = reader.read()
                if (id == 566858559280):
                    scene = "scan_menu"
                    scan_mode = 2
            finally:
                GPIO.cleanup()
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(26, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_KP_PLUS]:
        if plus_pressed_time is not None:
            if pygame.time.get_ticks() - plus_pressed_time > plus_hold_duration:
                pygame.quit()
                sys.exit()
    else:
        plus_pressed_time = None
    pygame.display.flip()