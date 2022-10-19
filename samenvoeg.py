from pickle import TRUE
import sys
import pygame
import time
import button
import os

pygame.init()
#scherm voor de game
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# x en y in een list locaties voor de draw lines
points = [(0, 400), (35, 363), (45, 359), (45, 351), (50, 347), (60, 339), (60, 335), (66, 333), (72, 327), 
(78, 325), (84, 322), (89, 320), (93, 322), (104, 324), (106, 329), (109, 337), (118, 344), (120, 348), 
(126, 359), (130, 363), (135, 370), (137, 375), (137, 382), (141, 390), (146, 396), (155, 408), (158, 419), 
(158, 426), (167, 439), (173, 440), (181, 442), (186, 437), (193, 433), (199, 430), (204, 422), (203, 413), 
(208, 400), (216, 400), (235, 400), (244, 392), (249, 384), (255, 379), (262, 369), (269, 358), (279, 346), 
(285, 347), (292, 338), (301, 330), (316, 323), (319, 322), (328, 323), (335, 329), (342, 334), (349, 336), 
(352, 341), (361, 345), (375, 345), (384, 339), (395, 347), (421, 355), (428, 365), (429, 376), (430, 387), 
(449, 407), (456, 420), (460, 428), (465, 435), (466, 445), (462, 455), (471, 474), (481, 485), (487, 493), 
(487, 503), (498, 509), (513, 520), (524, 520), (531, 520), (555, 520), (556, 520), (564, 505), (569, 503), 
(580, 494), (582, 485), (586, 480), (597, 473), (607, 464), (615, 460), (624, 462), (646, 456), (656, 463), 
(667, 473), (681, 478), (699, 484), (716, 484), (728, 487), (758, 494), (756, 503), (767, 511), (780, 514), 
(822, 527), (824, 534), (838, 538), (847, 534), (852, 532), (866, 526), (875, 522), (888, 517), (890, 524), 
(902, 523), (911, 519), (929, 505), (936, 497), (938, 477), (946, 460), (952, 460), (966, 460), (974, 460), 
(981, 460), (992, 460), (1000, 460), (1020, 460), (1025, 456), (1036, 448), (1043, 438), (1054, 435), (1061, 436), 
(1080, 429), (1083, 428), (1099, 447), (1112, 462), (1110, 469), (1108, 480), (1114, 485), (1119, 491),(1126, 498),
(1137, 494), (1142, 489), (1149, 473), (1155, 467), (1165, 466), (1177, 463), (1179, 450), (1185, 443), 
(1194, 439), (1203, 434), (1209, 423), (1211, 420), (1225, 417), (1233, 424), (1242, 427), (1247, 434), 
(1253, 443), (1262, 442), (1267, 446), (1273, 443), (1278, 443)]

points2 = [(0, 480), (61, 560), (88, 560), (115, 598), (190, 580), (219, 619), (247, 551), (286, 596), (320, 605),
(329, 585), (365, 550), (390, 560), (430, 590), (444, 552), (464, 624), (512, 625), (559, 612), (582, 589),
(600, 566), (620, 620), (680, 520), (694, 570), (704, 530), (757, 500), (808, 500), (869, 524), (925, 495),
(950, 506), (966, 544), (988, 582), (1030, 598), (1051, 571), (1093, 520), (1141, 581), (1173, 603), (1208, 602),
(1227, 590), (1240, 595), (1263, 590), (1280, 588)] 

points3 = [(0, 200), (22, 221), (29, 224), (35, 232), (40, 246), (52, 260), (64, 271), (76, 291), (89, 306), 
(97, 311), (114, 320), (120, 331), (131, 340), (151, 344), (157, 343), (172, 344), (177, 351), (181, 360), 
(185, 366), (196, 371), (203, 373), (208, 376), (216, 383), (230, 395), (253, 399), (267, 396), (279, 405), 
(290, 416), (305, 419), (325, 433), (327, 440), (349, 440), (367, 440), (379, 431), (392, 416), (405, 407), 
(420, 409), (429, 404), (432, 390), (439, 382), (443, 381), (462, 383), (488, 382), (495, 370), (506, 358), 
(522, 355), (541, 359), (566, 365), (585, 362), (590, 370), (594, 379), (602, 398), (610, 414), (613, 438), 
(624, 454), (639, 479), (638, 497), (645, 517), (656, 526), (661, 556), (661, 575), (669, 584), (694, 592), 
(723, 599), (736, 596), (751, 587), (762, 584), (779, 576), (809, 576), (833, 559), (844, 546), (855, 550), 
(878, 554), (894, 536), (905, 513), (906, 493), (915, 480), (930, 480), (945, 480), (964, 464), (969, 451), 
(982, 429), (999, 420), (1016, 417), (1036, 408), (1057, 411), (1086, 394), (1114, 403), (1129, 421), (1155, 433), 
(1179, 411), (1200, 392), (1205, 372), (1207, 355), (1223, 344), (1245, 333), (1249, 311), (1257, 303), 
(1274, 302), (1280, 301)]



landing_cords = [(757, 600), (808, 600)]

game_info = pygame.image.load('info.jpeg')
game_info_false = pygame.image.load('black.jpeg')

info = False

#variables for welcome text
font = pygame.font.SysFont("Arial", 20)
smallfont = pygame.font.SysFont('Corbel',35)
white = (255, 255, 255)
black = (0, 0, 0)
welcome_text = font.render('Welcome to project moonlanding', True, white, black)
textRect = welcome_text.get_rect()
textRect.center = (650, 200)

#score

def min_num_in_file(filename):    
    """Returns the largest integer found in the file"""    
    with open(filename, "r") as f:        
        data = [int(x) for x in f.readlines()]        
    return min(data)

highscore = min_num_in_file('high_score.txt')

# white color
color = (255,255,255)

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 191, 0)


# light shade of the button
color_light = (170,170,170)
  
# dark shade of the button
color_dark = (100,100,100)

# defining a font
font = pygame.font.SysFont('Corbel',50)
font2 = pygame.font.SysFont('Corbel',45)
smallfont = pygame.font.SysFont('Corbel',35)
#defining sounds
failed = pygame.mixer.Sound('gameover.mp3')


# eind/begin scherm tijdelijk
def ending():
    text = font2.render("Game over!", True, (255,255,255))
    screen.blit(text, (550,350))
#tekst beneden
def knop():
    text2 = font.render("Naar beginscherm", True, (255,255,255))
    screen.blit(text2, (10,680))
#terug naar beginscherm
def beginning():
    screen.fill((0,0,0))

exit_button = pygame.image.load('main_menu.png').convert_alpha()
exit_button = pygame.transform.scale(exit_button, (200, 100))
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self):
        action = False
        #positie muis
        pos = pygame.mouse.get_pos()
        #check of muis op button is
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                action = True
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action
        
end_button = Button(50,600, exit_button)

####################################################################
# rendering a text written in
# this font
text_quit = smallfont.render('quit' , True , color)
text_level_1 = smallfont.render('level 1' , True , color)
text_level_2 = smallfont.render('level 2' , True , color)
text_level_3 = smallfont.render('level 3' , True , color)
text_info = smallfont.render('How to play' , True , color)

# een sprite class aangemaakt voor de terrain.
class Terrain(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((1280, 720))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.lines(self.image, (255,255,255),False, points,2)
        self.rect = self.image.get_rect(topleft = (0, 0))

#een class aangemaakt voor de player, wat voor nu alleen maar een blokje is
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('shuttle1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = (600, 10))

#sprite class voor de landing spot
class Landing(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((1280, 720))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.line(self.image, (255,255,255), (513, 520), (556, 520),6)
        pygame.draw.line(self.image, (255,255,255), (946, 460), (1020, 460),6)
        pygame.draw.line(self.image, (255,255,255), (208, 400), (235, 400),6)
        self.rect = self.image.get_rect(topleft = (0, 0))
#################################################################################
# een sprite class aangemaakt voor de terrain2.
class Terrain2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((1280, 720))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.lines(self.image, (255,255,255),False, points2,2)
        self.rect = self.image.get_rect(topleft = (0, 0))

#een class aangemaakt voor de player, wat voor nu alleen maar een blokje is
class Player2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('shuttle1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = (600, 10))

#sprite class voor de landing spot
class Landing2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((1280, 720))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.line(self.image, (255,255,255), (760, 500), (780, 500),6)
        pygame.draw.line(self.image, (255,255,255), (490, 625), (510, 625),6)
        self.rect = self.image.get_rect(topleft = (0, 0))
##################################################################################
# een sprite class aangemaakt voor de terrain3.
class Terrain3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((1280, 720))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.lines(self.image, (255,255,255),False, points3,2)
        self.rect = self.image.get_rect(topleft = (0, 0))

#een class aangemaakt voor de player, wat voor nu alleen maar een blokje is
class Player3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('shuttle1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = (600, 10))

#sprite class voor de landing spot
class Landing3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((1280, 720))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.line(self.image, (255,255,255), (325, 440), (367, 440),6)
        pygame.draw.line(self.image, (255,255,255), (915, 480), (945, 480),6)
        self.rect = self.image.get_rect(topleft = (0, 0))
##################################################################################
FONT = pygame.font.SysFont('arialblack', 20)
CON_FONT = pygame.font.SysFont('arialblack', 100)
SMALL_FONT = pygame.font.SysFont('comicsans', 16)

QUIT_IMG = pygame.image.load('QUIT.png')
QUIT_IMG = pygame.transform.scale(QUIT_IMG, (200, 100))
MAIN_MENU_IMG = pygame.image.load('main_menu.png')
MAIN_MENU_IMG = pygame.transform.scale(MAIN_MENU_IMG, (200, 100))

quit_button = button.Button(900, 550, QUIT_IMG, 1)
main_menu_button = button.Button(200, 550, MAIN_MENU_IMG, 1)

#timer
clock = pygame.time.Clock()
counter, text = 0, 'TIME:'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 15)

running = True
right = False
speed = 2
gravity = True
fuel = 200

#variable aangemaakt die de classes oproepen
terrain = Terrain()
player = Player()
landing = Landing()

#variable lvl2 aangemaakt die de classes oproepen
terrain2 = Terrain2()
player2 = Player2()
landing2 = Landing2()

#variable lvl3 aangemaakt die de classes oproepen
terrain3 = Terrain3()
player3 = Player3()
landing3 = Landing3()

#groups maken van de 2 sprite classes die met elkaar moeten kunnen colliden
game_over_group = pygame.sprite.Group([terrain, player])
landing_group = pygame.sprite.Group([landing, player])

game_over_group2 = pygame.sprite.Group([terrain2, player2])
landing_group2 = pygame.sprite.Group([landing2, player2])

game_over_group3 = pygame.sprite.Group([terrain3, player3])
landing_group3 = pygame.sprite.Group([landing3, player3])

def change_values():
    global gravity
    global fuel
    global speed
    player.rect.x = 600
    player.rect.y = 10
    player2.rect.x = 600
    player2.rect.y = 10
    player3.rect.x = 600
    player3.rect.y = 10

    speed = 2
    gravity = True
    fuel = 200

def victory_screen():
    screen.fill(BLACK)
    victory_txt = CON_FONT.render("VICTORY", 1, WHITE)
    screen.blit(victory_txt, (WIDTH/2 - victory_txt.get_width()/2 , HEIGHT/6))
    victory_screen_txt = SMALL_FONT.render("Congratulations you completed the level!", 1, WHITE)
    screen.blit(victory_screen_txt, (WIDTH/2 - victory_screen_txt.get_width()/2 , HEIGHT/6 + victory_txt.get_height() + 5))

    quit_button.draw(screen)
    main_menu_button.draw(screen)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)

        if quit_button.draw(screen):
            run = False
            pygame.quit()
            sys.exit()
        if main_menu_button.draw(screen):
            change_values()
            screen.fill(BLACK)
            main()
            run = False
            exit()
            
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def level1():
    screen.fill((0,0,0))
    rocket = pygame.mixer.Sound('earrape.mp3')
    global speed
    global gravity
    global fuel
    pygame.draw.rect(screen, WHITE if fuel > 65 else ORANGE if fuel > 0 else RED, (10, 30, 3+fuel, 15))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and fuel > 0: #left
        player.rect.x -= speed
        fuel -= 1
        rocket.play()
    if keys[pygame.K_RIGHT] and fuel > 0: #right
        player.rect.x += speed
        fuel -= 1
        rocket.play()
    if keys[pygame.K_UP] and fuel > 0: #up
        player.rect.y -= speed
        fuel -= 1
        rocket.play()
    player.rect.clamp_ip(screen.get_rect())

    if gravity:
        player.rect.y += 1



        
    #checkt of er een collision is tussen player en terrain
    destroyed = pygame.sprite.collide_mask(player, terrain)
    #checkt of er een collision is tussen player en landing plekken
    landed = pygame.sprite.collide_mask(player, landing)

        
        
    screen.blit(font.render(text, True, (255, 255, 255)), (10, 10))

    #teken de groups op screen (de game)
    game_over_group.draw(screen)
    landing_group.draw(screen)

    #zodra er collision is tussen terrain en player, is de player dood
    endscr = 0
    if destroyed and not landed:
        endscr += 1
        if endscr > 0:
            screen.fill((0,0,0))
            ending()
            knop()
            failed.play()
            gravity = False
            speed = 0
            if end_button.draw():
                change_values()
                main()
                exit()

    #zodra er collision is tussen landingspot en player, is de player succesvol geland
    elif landed and destroyed:
        # pygame.draw.rect(screen, (255, 255, 255), (0, 0, 50, 50))
        # Open a file with access mode 'a'
        file_object = open('high_score.txt', 'a')
        # Append score at the end of file
        file_object.write(f"{counter}\n")
        # Close the file
        file_object.close() 
        victory_screen()
        speed = 0
        gravity = False
        fuel = 200
####################################################################################
def level2():
    screen.fill((0,0,0))
    rocket = pygame.mixer.Sound('earrape.mp3')
    global speed
    global gravity
    global fuel
    pygame.draw.rect(screen, WHITE if fuel > 65 else ORANGE if fuel > 0 else RED, (10, 30, 3+fuel, 15))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and fuel > 0: #left
        player2.rect.x -= speed
        fuel -= 1
        rocket.play()
    if keys[pygame.K_RIGHT] and fuel > 0: #right
        player2.rect.x += speed
        fuel -= 1
        rocket.play()
    if keys[pygame.K_UP] and fuel > 0: #up
        player2.rect.y -= speed
        fuel -= 1
        rocket.play() 
    player2.rect.clamp_ip(screen.get_rect())

    if gravity:
        player2.rect.y += 1



        
    #checkt of er een collision is tussen player en terrain
    destroyed = pygame.sprite.collide_mask(player2, terrain2)
    #checkt of er een collision is tussen player en landing plekken
    landed = pygame.sprite.collide_mask(player2, landing2)

        
        
    screen.blit(font.render(text, True, (255, 255, 255)), (10, 10))

    #teken de groups op screen (de game)
    game_over_group2.draw(screen)
    landing_group2.draw(screen)

    #zodra er collision is tussen terrain en player, is de player dood
    endscr = 0
    if destroyed and not landed:
        endscr += 1
        if endscr > 0:
            screen.fill((0,0,0))
            ending()
            knop()
            failed.play()
            gravity = False
            speed = 0
            if end_button.draw():
                change_values()
                main()
                exit()

    #zodraa er collision is tussen landingspot en player, is de player succesvol geland
    elif landed and destroyed:
        # pygame.draw.rect(screen, (255, 255, 255), (0, 0, 50, 50))
        # Open a file with access mode 'a'
        file_object = open('high_score.txt', 'a')
        # Append score at the end of file
        file_object.write(f"{counter}\n")
        # Close the file
        file_object.close() 
        victory_screen()
        speed = 0
        gravity2 = False
        fuel = 200
####################################################################################
def level3():
    screen.fill((0,0,0))
    rocket = pygame.mixer.Sound('earrape.mp3')
    global speed
    global gravity
    global fuel
    pygame.draw.rect(screen, WHITE if fuel > 65 else ORANGE if fuel > 0 else RED, (10, 30, 3+fuel, 15))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and fuel > 0: #left
        player3.rect.x -= speed
        fuel -= 1
        rocket.play()
    if keys[pygame.K_RIGHT] and fuel > 0: #right
        player3.rect.x += speed
        fuel -= 1
        rocket.play()
    if keys[pygame.K_UP] and fuel > 0: #up
        player3.rect.y -= speed
        fuel -= 1
        rocket.play() 
    player3.rect.clamp_ip(screen.get_rect())

    if gravity:
        player3.rect.y += 1



        
    #checkt of er een collision is tussen player en terrain
    destroyed = pygame.sprite.collide_mask(player3, terrain3)
    #checkt of er een collision is tussen player en landing plekken
    landed = pygame.sprite.collide_mask(player3, landing3)

        
        
    screen.blit(font.render(text, True, (255, 255, 255)), (10, 10))

    #teken de groups op screen (de game)
    game_over_group3.draw(screen)
    landing_group3.draw(screen)

    #zodra er collision is tussen terrain en player, is de player dood
    endscr = 0
    if destroyed and not landed:
        endscr += 1
        if endscr > 0:
            screen.fill((0,0,0))
            ending()
            knop()
            failed.play()
            gravity = False
            speed = 0
            if end_button.draw():
                change_values()
                main()
                exit()

    #zodra er collision is tussen landingspot en player, is de player succesvol geland
    elif landed and destroyed:
        # pygame.draw.rect(screen, (255, 255, 255), (0, 0, 50, 50))
        # Open a file with access mode 'a'
        file_object = open('high_score.txt', 'a')
        # Append score at the end of file
        file_object.write(f"{counter}\n")
        # Close the file
        file_object.close() 
        victory_screen()
        speed = 0
        gravity3 = False
        fuel = 200

####################################################################################
def main():
    song = pygame.mixer.Sound('squidgame.mp3')
    song.play()
    screen.fill(BLACK)
    global info, counter, clock, font, text, highscore, highscore_inscreen
    tel_lvl1 = 0
    tel_lvl2 = 0
    tel_lvl3 = 0
    quit1 = 0
    startscherm = True
    while running:
        highscore_inscreen = smallfont.render(f'highscore:{highscore}' , True , white)
        #checkt of de game wordt afgesloten
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #timer
            if event.type == pygame.USEREVENT and startscherm == False: 
                counter += 1
                text = 'TIME:' + str(counter).rjust(3) if counter > 0 else 'boom!'

        #knop
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        
        if click[0] == True and 440 <= mouse[0] <= 580+140 and 240 <= mouse[1] <= 240+40:
            counter = 0
            tel_lvl1 += 1
        #button_level_1
        if tel_lvl1 > 0:
            screen.fill((0,0,0))
            level1()
            startscherm = False

        if click[0] == True and 440 <= mouse[0] <= 580+140 and 300 <= mouse[1] <= 300+40:
            counter = 0
            tel_lvl2 += 1
        #button_level_2
        if tel_lvl2 > 0:
            screen.fill((0,0,0))
            level2()
            startscherm = False
        #button_level_3
        if click[0] == True and 440 <= mouse[0] <= 580+140 and 360 <= mouse[1] <= 360+40:
            counter = 0
            tel_lvl3 += 1
        if tel_lvl3 > 0:
            screen.fill((0,0,0))
            level3()
            startscherm = False
        #button quit
        if click[0] == True and 800 <= mouse[0] <= 800+140 and 625 <= mouse[1] <= 625+40:
            quit1 += 1
        if quit1 > 1:
            exit()


        if startscherm == True:
            screen.fill(BLACK)
            highscore = min_num_in_file('high_score.txt')
            #button info
            if click[0] == True and 100 <= mouse[0] <= 100+180 and 75 <= mouse[1] <= 75+40 and info == False:
                info = True
                time.sleep(0.2)
            elif click[0] == True and 100 <= mouse[0] <= 100+180 and 75 <= mouse[1] <= 75+40 and info == True:
                info = False
                time.sleep(0.2)
            if info == True:
                screen.blit(game_info,(100,450))
            pygame.draw.rect(screen,color_dark,[800, 625,140,40])
            pygame.draw.rect(screen,color_dark,[580, 240,140,40])
            pygame.draw.rect(screen,color_dark,[580, 300,140,40])
            pygame.draw.rect(screen,color_dark,[580, 360,140,40])
            pygame.draw.rect(screen,color_dark,[100, 75,180,40])
            #button quit
            if 800 <= mouse[0] <= 800+140 and 625 <= mouse[1] <= 625+40:
                pygame.draw.rect(screen,color_light,[800, 625,140,40])
            #button level 1
            elif 580 <= mouse[0] <= 580+140 and 240 <= mouse[1] <= 240+40:
                pygame.draw.rect(screen,color_light,[580, 240,140,40])
            #button level 2
            elif 580 <= mouse[0] <= 580+140 and 300 <= mouse[1] <= 300+40:
                pygame.draw.rect(screen,color_light,[580, 300,140,40])
            #button level 3
            elif 580 <= mouse[0] <= 580+140 and 360 <= mouse[1] <= 360+40:
                pygame.draw.rect(screen,color_light,[580, 360,140,40])
            #button info
            elif 100 <= mouse[0] <= 100+180 and 75 <= mouse[1] <= 75+40:
                pygame.draw.rect(screen,color_light,[100, 75,180,40])

            # superimposing the text onto our buttons
            screen.blit(text_quit , (800+40,625))
            screen.blit(text_level_1 , (550+40,245))
            screen.blit(text_level_2 , (550+40,305))
            screen.blit(text_level_3 , (550+40,365))
            screen.blit(highscore_inscreen , (900+40,80))
            screen.blit(text_info , (70+40,80))
            #show text
            screen.blit(welcome_text, textRect)
        
        
        
        ####################################
        clock.tick(60)

        pygame.display.flip()

main()