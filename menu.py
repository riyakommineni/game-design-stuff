#Riya Kommineni



import sys
import pygame, time,os,random, math, datetime 
pygame.init()#initialize the pygame package
date=datetime.datetime.now() 
pygame.init() 
# print(pygame.font.get_fonts())
# pygame.time.delay(10000)
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)

os.system('clear')
WIDTH=700 
HEIGHT=700
colors={"green":(189,227,114),"yellow":(225,208,0),"blue":(32, 206, 222),"orange":(242,112,23)}
clr=colors.get("orange")
message=['Instructions', 'Settings', 'Game 1', 'Game 2', 'Scoreboard', 'Exit']

screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("My First Game")  

#boxes for menu
Button_menu=pygame.Rect(274, 125, 125, 40)
Button_instruct=pygame.Rect(274, 150, 125, 40)
Button_settings=pygame.Rect(274, 200, 125, 40)
Button_Game1=pygame.Rect(274, 250, 125, 40)
Button_Game2=pygame.Rect(274, 300, 125, 40)
Button_score=pygame.Rect(274, 350, 125, 40)
Button_exit=pygame.Rect(274, 400, 125, 40)
#images
bg=pygame.image.load('background-firstgame.jpg')
char = pygame.image.load('character1.png')
char = pygame.transform.scale(char, (50, 50))
# screen.blit(bg, (0,0))
# pygame.display.update()
# pygame.time.delay(5000)


#square Var
hb=50
wb=50
xb=100
yb=300

charx = xb
chary = yb

cx=350
cy=350
rad=25
speed=2
ibox = rad*math.sqrt(2)
xig = cx-(ibox/2)
yig = cy-(ibox/2)

#mouse variables
mx = 0
my = 0

square=pygame.Rect(xb,yb,wb,hb)
insSquare=pygame.Rect(xig,yig,ibox,ibox)
squareClr=colors.get("green")
#keep running create a loop
mountainSquare=pygame.Rect(250,320,180,250)
circleClr=colors.get("blue")
backgrnd=colors.get("orange")
run = True
Game = False

def mainMenu():
    pygame.draw.rect(screen, colors.get('green'), Button_settings)
    Title = TITLE_FONT.render("Game Menu", 1, colors.get("blue"))
    screen.fill(colors.get('yellow'))
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    yMenu=150
    
    for item in message:
        button_menu=pygame.Rect(274, yMenu, 125, 40)
        text=MENU_FONT.render(item, 1, colors.get('blue'))
        pygame.draw.rect(screen, colors.get('green'), button_menu)
        screen.blit(text, (280, yMenu))
        pygame.display.update()
        pygame.time.delay(50)
        yMenu += 50
    MENU=True
    while MENU:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                print("You quit")
                pygame.display.quit()
                MENU=False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_instruct.collidepoint((mx, my)):
                    Instructions()
                if Button_settings.collidepoint((mx, my)):
                    settings()
                if Button_Game1.collidepoint((mx, my)):
                    Game1()
                if Button_score.collidepoint((mx, my)):
                    scoreboard()
                if Button_exit.collidepoint((mx, my)):
                    exit()
    
def Instructions():
 
    Title = TITLE_FONT.render("Instructions", 1, colors.get("blue"))
  
    screen.fill(colors.get("green"))

    Button_1 = pygame.Rect(36, 350, 220, 50)
    pygame.draw.rect(screen, colors.get("blue"), Button_1)
  
    myFile = open("instructions.txt", "r")
    content = myFile.readlines()

    yinstructions = 150
    for line in content:
        Instruc = MENU_FONT.render(line[0:-1], 1, colors.get("yellow"))
        screen.blit(Instruc, (40, yinstructions))
        pygame.display.update()
        pygame.time.delay(50)
        yinstructions += 40

    myFile.close()

    #renderig fonts to the screen
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))

    pygame.display.update()
    Instructions = True
    while Instructions:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Instructions=False
                pygame.display.quit()
                print("bye bye ")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_1.collidepoint((mx, my)):
                    mainMenu() 



def scoreboard():
    title=TITLE_FONT.render('Scoreboard', 1, colors.get('blue'))
    text3 = MENU_FONT.render("Return to Menu", 1, colors.get("yellow"))


    screen.fill(colors.get('green'))
    Button_3 = pygame.Rect(25, 350, 200, 50)
    pygame.draw.rect(screen, colors.get("blue"), Button_3)
    

    screen.blit(title, (265,50))
    screen.blit(text3, (30,355))
    pygame.display.update()

    scoreboard=True
    while scoreboard:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.display.quit()
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                if Button_3.collidepoint((mx, my)):
                    mainMenu()


def settings():
    global content 

    title=TITLE_FONT.render('Settings', 1, colors.get('blue'))
    text=MENU_FONT.render('Return to Menu', 1, colors.get('yellow'))

    screen.fill(colors.get('green'))

    myFile = open("settings.txt", "r")
    content = myFile.readlines()

    Button_2 = pygame.Rect(25, 350, 200, 50)
    pygame.draw.rect(screen, colors.get("blue"), Button_2)

    screen.blit(title, (275,50))
    screen.blit(text, (30,355))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.display.quit()
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                if Button_2.collidepoint((mx, my)):
                    mainMenu()


mainMenu()
Instructions()
score=0 
high=0

def Game1():
    global score 
    global high
    score=0
    global charx
    global chary
    global mx
    global my
    global rad
    run=True 
    while run:
        # screen.fill(background)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                print("Y quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
        screen.blit(bg, (0,0))
        keys= pygame.key.get_pressed() 
        if keys[pygame.K_RIGHT] and square.x < WIDTH -(wb):
            square.x += speed
            charx += speed
        if keys[pygame.K_LEFT] and  square.x > speed:
            square.x -= speed
            charx -= speed
        if keys[pygame.K_UP] and square.y >speed:   
            square.y -= speed
            chary -= speed
        if keys[pygame.K_DOWN] and square.y <HEIGHT -hb:  
            square.y += speed
            chary += speed
            
        if keys[pygame.K_d] and cx < WIDTH -(rad):
            cx += speed
            insSquare.x += speed
        if keys[pygame.K_a] and  cx > (speed+rad):
            cx -= speed
            insSquare.x -= speed
        if keys[pygame.K_w] and cy >(speed+rad):   
            cy -= speed
            insSquare.y -= speed
        if keys[pygame.K_s] and cy <HEIGHT -(rad):  
            cy += speed
            insSquare.y += speed

        if square.colliderect(insSquare):
            score +1 
            print("BOOM")
            rad+=1
            cx=random.randint(rad, WIDTH-rad)
            cy=random.randint(rad, HEIGHT-rad)
            ibox = rad*math.sqrt(2)
            xig = cx-(ibox/2)
            yig = cy-(ibox/2)
            insSquare=pygame.Rect(xig,yig,ibox,ibox)
            
        #if square.colliderect(mountainSquare):
            #square.x=10
            #square.y=10
            #charx=10
            #chary=10
        #rect(surface, color, rect) -> Rect
        pygame.draw.rect(screen, squareClr,square)
        #circle(surface, color, center, radius)
        pygame.draw.circle(screen, circleClr, (cx,cy), rad)
        pygame.draw.rect(screen, squareClr, insSquare)

        #pygame.draw.rect(screen, colors.get('white'), mountainSquare,)
        pygame.display.update()





def exit():
    global title
    global Game
    title=TITLE_FONT.render('goodbye', 1, colors.get('blue'))
    Game= False         






def scoreboard():
    print(score)
    File=open("cesscore.txt",'a') 
    File.write (str(score)) 
    File.close()
    with open("cescore.txt") as f:
        if score > high:
                high=score  
    File.write(str(score)+"\t"+"\t"+ date.strftime("%m/%d/%Y"))
    File.close() 


Game1() 