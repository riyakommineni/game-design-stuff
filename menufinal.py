

import pygame, os,random,time

from pygame import color
os.system('clear')
pygame.init()

## LISTS FOR MENU MESSAGES

screenMessage=[ "800x800", "800x600", "600x600"]
settingMessages=["Screen Size", "Background colors", "Object Colors","Sounds On/Off"]
mainMenu=["Instructions", 'Settings', "Level 1", "Level 2", "ScoreBoard", "Exit"]
colors = {'black':(0,0,0), 'red':(255,0,0), 'green':(0,255,0), 'blue':(0,0,145), 'white':(255,255,255), 'purple':(150,0,150), 'orange':(214, 230, 73)}
#GLOBAL VARIABLES
WHITE=colors.get('white')
BLACK=colors.get('black')
ORANGE=colors.get('orange')
COLOR=WHITE
MAINMENU=True
SETTINGS=False
INSTRUCTIONS=False
BACKGROUND=False
SCREEN=False
LEVEL1=False
LEVEL2=False
SCOREBOARD=False
OBJECTCOLOR=False
SOUNDS=False
flag=False

# Screen and square definition
WIDTH=700
HEIGHT=700
wbox=30
hbox=30
x=70
y=150
xs=50
ys=200
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Setting Window")
square=pygame.Rect(x,y, wbox,hbox)
screenSize=pygame.Rect(xs,ys,wbox*4, hbox*4)
win.fill(COLOR)
squaresSize=[pygame.Rect(xs,ys,wbox*4, hbox*4), pygame.Rect(xs,ys,wbox*4, hbox*3), pygame.Rect(xs,ys,wbox*3, hbox*3)]
#Declare FONTS
TITLE_FONT=pygame.font.SysFont('freesansbold.ttf', 80)
MENU_FONT=pygame.font.SysFont('freesansbold.ttf', 40)
INSTRUCTIONS_FONT=pygame.font.SysFont('freesansbold.ttf', 30)
text= TITLE_FONT.render('message',1,BLACK)
#New window title
#images
bg1 = pygame.image.load('final images/peacesign.png')
im1 = pygame.image.load('final images/heart.png')
im2 = pygame.image.load('final images/flower.png')
im3 = pygame.image.load('final images/star.png')
im4 = pygame.image.load('final images/peacesign.png')
#game specific variables
FPS = 30
WINDOWWIDTH = 700
WINDOWHEIGHT = 700
FLASHSPEED = 500 # in milliseconds
FLASHDELAY = 200 # in milliseconds
BUTTONSIZE = 200
BUTTONGAPSIZE = 20
TIMEOUT = 4 # seconds before game over if no button is pushed.
#                R    G    B
WHITE        = (255, 255, 255)
BLACK        = (  0,   0,   0)
BRIGHTRED    = (255,   0,   0)
RED          = (230, 177, 225)
BRIGHTGREEN  = (  0, 255,   0)
GREEN        = ( 8, 140, 55)
BRIGHTBLUE   = (  0,   0, 255)
BLUE         = (  168, 235, 237)
BRIGHTYELLOW = (255, 255,   0)
YELLOW       = (247, 148, 10)
DARKGRAY     = ( 40,  40,  40)
bgColor = BLACK
XMARGIN = int((WINDOWWIDTH - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)
YMARGIN = int((WINDOWHEIGHT - (2 * BUTTONSIZE) - BUTTONGAPSIZE) / 2)
YELLOWRECT = pygame.Rect(XMARGIN, YMARGIN, BUTTONSIZE, BUTTONSIZE) 

BLUERECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN, BUTTONSIZE, BUTTONSIZE)

REDRECT = pygame.Rect(XMARGIN, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)
    

GREENRECT = pygame.Rect(XMARGIN + BUTTONSIZE + BUTTONGAPSIZE, YMARGIN + BUTTONSIZE + BUTTONGAPSIZE, BUTTONSIZE, BUTTONSIZE)

#Function to print Titles to all screens
def display_Title(message,ym):
    pygame.time.delay(10)
    text= TITLE_FONT.render(message,1,BLACK)
    xm=WIDTH/2-text.get_width()/2
    win.blit(text, (xm,ym))
    pygame.display.update()
    pygame.time.delay(10)

#Function to print all the menus 
def Menu_function(line):
    pygame.time.delay(100)
    ym=y
    square.y=y
    xm=x+wbox+10
    for i in range(0,len(line)):
        word=line[i]
        pygame.draw.rect(win, ORANGE, square)
        text=MENU_FONT.render(word,1,BLACK)
        win.blit(text,(xm,ym))
        pygame.display.flip()
        pygame.time.delay(100)
        ym +=HEIGHT/10
        square.y=ym
    
def MainMenuWin(xm,ym):
    global MAINMENU
    global INSTRUCTIONS
    global SETTINGS
    global LEVEL1
    global LEVEL2
    global SCOREBOARD
    if xm>=70 and xm<=95 and ym>=150 and ym<=175:
        win.fill(COLOR)
        pygame.display.set_caption("Instructions")
        display_Title("Instructions", 70)
        display_Title("Back", HEIGHT-50)
        pygame.display.update()
        MAINMENU = False
        INSTRUCTIONS = True               
    if xm>=70 and xm<=95 and ym>=250 and ym<=275: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        pygame.display.set_caption("Settings")
        display_Title("SETTINGS",  70)
        Menu_function(settingMessages)
        display_Title("BACK", HEIGHT-50)
        pygame.display.update()
        MAINMENU = False
        SETTINGS = True  
    if xm>=70 and  xm<=95 and ym>=350 and ym<=375: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        pygame.display.set_caption("Level 1")
        display_Title("Level 1",  70)
        display_Title("Back", HEIGHT-50)
        pygame.display.update()
        MAINMENU = False
        LEVEL1 = True
    if xm>=70 and  xm<=95 and ym>=450 and ym<=475: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        pygame.display.set_caption("Level 2")
        display_Title("Level 2",  70)
        display_Title("Back", HEIGHT-50)
        pygame.display.update()
        MAINMENU = False
        LEVEL2 = True
    if xm>=70 and  xm<=95 and ym>=550 and ym<=575: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        pygame.display.set_caption("ScoreBoard")
        display_Title("Scoreboard",  70)
        display_Title("Back", HEIGHT-50)
        pygame.display.update()
        MAINMENU = False
        LEVEL2 = True
    if xm>=70 and  xm<=95 and ym>=650 and ym<=675: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        display_Title("Exit",  70)
        display_Title("Back", HEIGHT-50)
        pygame.display.update()
        MAINMENU = False
        global run
        run=False
def SettingMenuWin(xm,ym):
    global SETTINGS
    global SCREEN
    global BACKGROUND
    global OBJECTCOLOR
   
    if xm>=70 and xm<=95 and ym>=150 and ym<=175:
        win.fill(COLOR)
        display_Title("Screen Size", 70)
        display_Title("Back", 750)
        pygame.display.update()
        SETTINGS = False
        SCREEN = True  
                   
    if xm>=70 and xm<=95 and ym>=250 and ym<=275 and flag: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        display_Title("BACKGROUND COLORS",  70)
        display_Title("BACK", 750)
        pygame.display.update()
        BACKGROUND = True
        SETTINGS = False             
    if xm>=70 and  xm<=95 and ym>=350 and ym<=375: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        display_Title("OBJECT COLORS",  70)
        display_Title("Back", 750)
        pygame.display.update()
        SETTINGS = False
        OBJECTCOLOR = True
    if xm>=70 and  xm<=95 and ym>=450 and ym<=475: #71, 193. 93,193. 93, 212. 71, 211
        win.fill(COLOR)
        display_Title("SOUNDS",  70)
        display_Title("Back", 750)
        pygame.display.update()
        SETTINGS = False
        OBJECTCOLOR = True
def Menu_Back():
    win.fill(COLOR)
    display_Title("MAIN", 70)
    Menu_function(mainMenu)
    pygame.display.update()
def Setting_Back():
    win.fill(COLOR)
    display_Title("SETTINGS", 70)
    Menu_function(settingMessages)
    display_Title("Back", HEIGHT-50)
    pygame.display.update()
def Screen_size():
    pygame.time.delay(100)
    ym=ys
    screenSize.x=xs
    xm=xs
    for i in range(0,len(squaresSize)):
        squary=squaresSize[i]
        squary.x=xm
        pygame.draw.rect(win, ORANGE, squary)
        word= screenMessage[i]
        text=MENU_FONT.render(word,1,BLACK)
        win.blit(text,(xm-10,ym-40))
        pygame.display.flip()
        pygame.time.delay(100)
        xm +=200
def game_Level1():
    win.blit(bg1, (0,0))
    pygame.display.set_caption("My game 1")
    pygame.display.flip()
    #add your game logic here

# def Color_screen():
#     for key in colors:
#Start Program
display_Title("MENU", 40)
Menu_function(mainMenu)
run=True
xm=0
ym=0
# C:\Users\suarezm\OneDrive - Greenhill School\Game Design\GameDesign2021_Fall_Ablock\cade.py  
while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run=False
    mouse_pos=(0,0)
    if eve.type==pygame.MOUSEBUTTONDOWN:
        mouse_pressed=pygame.mouse.get_pressed()
        if mouse_pressed:
            mouse_pos=pygame.mouse.get_pos()
            print(pygame.mouse.get_pos())
            xm=mouse_pos[0]
            ym=mouse_pos[1]
    if MAINMENU:
        MainMenuWin(xm,ym)
    if INSTRUCTIONS:
       
        myFile=open('instructions.txt', 'r')
        yi=150
        for line in myFile.readlines():
            text=INSTRUCTIONS_FONT.render(line, 1, BLACK)
            win.blit(text, (40,yi))
            pygame.display.update()
            pygame.time.delay(50)
            yi+=50
        myFile.close()
        display_Title("Back", HEIGHT-100)
        print(xm,ym)
        if xm >320 and xm<490 and ym>HEIGHT-200 and ym<HEIGHT:
            MAINMENU = True
            INSTRUCTIONS = False
            #Menu_Back()
    if SETTINGS:
        SettingMenuWin(xm,ym)
        flag=True
        if xm >335 and xm<460 and ym>HEIGHT-50 and ym<HEIGHT:
            Menu_Back()
            MAINMENU = True
            SETTINGS = False
            flag=False
    if SCREEN:
        Screen_size()
        display_Title("Back", HEIGHT-50)
        pygame.display.update()
        if xm>450 and xm <540 and ym>200 and ym<290: 
            WIDTH=600
            HEIGHT=600
            win=pygame.display.set_mode((WIDTH,HEIGHT))
            win.fill(COLOR)
            Screen_size()
            display_Title("Back", HEIGHT-100)
            pygame.display.update()
        if xm >335 and xm<460 and ym>HEIGHT-100 and ym<HEIGHT:
            Setting_Back()
            SETTINGS = True
            SCREEN = False
        if xm >335 and xm<460 and ym>745 and ym<795:
            Setting_Back()
            SETTINGS = True
            SCREEN = False
    if BACKGROUND:
        if xm >335 and xm<460 and ym>HEIGHT-50 and ym<HEIGHT:
            Setting_Back()
            SETTINGS = True
            BACKGROUND = False
    if OBJECTCOLOR:
        if xm >335 and xm<460 and ym>745 and ym<795:
            Setting_Back()
            SETTINGS = True
            OBJECTCOLOR = False
    if LEVEL1:
        #play game here
        game_Level1()
        if xm >335 and xm<460 and ym>745 and ym<795:
            Menu_Back()
            MAINMENU = True
            LEVEL1 = False
        pygame.display.flip()
    if LEVEL2:
        #Play game
        if xm >335 and xm<460 and ym>745 and ym<795:
            Menu_Back()
            MAINMENU = True
            LEVEL2 = False