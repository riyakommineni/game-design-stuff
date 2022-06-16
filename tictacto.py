#Riya Kommineni
#Tic Tac To game 

#functions:  
#draw_grid() 
#zero_grid()
#draw_markers()
#check_winner()
#game_end()

import os 
os.system('clear')
import sys
import pygame, time,os,random, math, datetime  
pygame.init()
date=datetime.datetime.now 
WIDTH=600
HEIGHT=600
colors={"green":(189,227,114),"yellow":(225,208,0),"blue":(32, 206, 222),"orange":(242,112,23)}
clr=colors.get("orange")
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("My First Game") 
scoreo = 0 
scorex = 0

SIZE = 3
markers = [] #control cells
MxMy = (0,0) #clicks
lineWidth = 10 
cellx = 0 
celly = 0
player = 1  #change players 1 and -1 
Game=True #control game
gameOver = False #check is game is over 
winner = 0 #save winner either 1 or -1 ZERO means tie 
cirClr = colors.get('blue') #circle color
xClr = colors.get('green') #x color 
clr=colors.get("limeGreen")
messageMenu=['Instructions', 'Settings', 'Game 1', 'Game 2', 'Scoreboard', 'Exit']
messageSettings=["Background Colors", "Screen Size", "Sound On/Off"]
mainTitle="Circle eats Square Menu"
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("Tic Tac Te")  #change the title of my window
backgrnd=colors.get("green")

#game Variable





print(markers)  
cirClr=colors.get("blue")
xClr=colors.get("yellow")
#function to zero array 
def zero_Array(): 
    for x in range(3):
        row= [0] *3
        markers.append(row)


def draw_grid():
    lineClr=colors.get("orange")
    for x in range(1,3):
        pygame.draw.line(screen,lineClr,(0,HEIGHT//3*x),(WIDTH,HEIGHT//3*x),lineWidth)  #Hztal line
        pygame.draw.line(screen,lineClr,(WIDTH//3*x, 0),(WIDTH//3*x,HEIGHT),lineWidth)  #Vert line
    pygame.time.delay(100)

def draw_Markers():
    xValue=0
    for x in markers:   # getting a rw
        yValue=0
        for y in x:  #each elem fthe rw
            if y ==1:
                print ("x")
                pygame.draw.line(screen,xClr,(xValue * WIDTH//3 + 15, yValue * HEIGHT//3 + 15), (xValue * WIDTH//3 + WIDTH//3-15, yValue * WIDTH//3 + WIDTH//3-15),lineWidth)
                pygame.draw.line(screen, xClr,(xValue*WIDTH//3 +WIDTH//3-15, yValue*HEIGHT//3+15),(xValue *WIDTH//3+15,yValue*HEIGHT//3+HEIGHT//3-15),lineWidth)
            if y==-1:
                print("O")
                pygame.draw.circle(screen,cirClr,(xValue*WIDTH//3+WIDTH//6,yValue*HEIGHT//3 +HEIGHT//6),WIDTH//6-15, lineWidth)
            yValue +=1
        xValue +=1
    pygame.display.update() 
def checkWinner():
    global gameOver, winner
    x_position = 0 
    for x in markers: 
        #check column 
        if sum (x) == 3: 
            print ('sum')
            winner = 1 
            gameOver = True 
        if sum (x) == -3: 
            winner == -1 
            gameOver = True 
        #Check Rows
        if markers[0][x_position] + markers[1][x_position] + markers[2][x_position] == 3:
            winner = 1 
            gameOver = True 
        if markers[0][x_position] + markers[1][x_position] + markers[2][x_position] == -3:
            winner = -1 
            gameOver = True
        x_position += 1
    #Check diaganols 
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or  markers[2][0] + markers[1][1] + markers[0][2] == 3: 
        winner = 1 
        gameOver = True 
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or  markers[2][0] + markers[1][1] + markers[0][2] == -3: 
        winner = -1 
        gameOver = True
    #Check for a tie 
    if gameOver == False: 
        tie = True 
        for ROW in markers:
            for COL in ROW:
               if COL == 0: 
                tie = False 
        #return winner 
        if tie: #in a bOOlean variable dont need == 
            gameOver = True 
            winner = 0 
              
    
    
def gameEnd():
    global Game, scoreo, scorex, markers 
    if winner == 1: 
        scorex += 1 
    if winner == -1: 
        scoreo += 1
    scro = str(scoreo)
    scrx = str(scorex)
    txtcolor = colors.get('blue')
    textxscore = MENU_FONT.render('x score is '+scrx, 1, (txtcolor))
    textoscore = MENU_FONT.render('o score is '+scrx, 1, (txtcolor))
    textagn = MENU_FONT.render('Want to play again?', 1, (txtcolor))
    textyes = MENU_FONT.render('Yes', 1, (txtcolor))
    textno = MENU_FONT.render('No', 1, (txtcolor))
    screen.fill(backgrnd)
    screen.blit(textxscore, (100,100))
    pygame.display.update()
    pygame.time.delay(500)
    print('do you want to play again and keep score?')
    markers = []
    zero_Array()

zero_Array()
while Game:
    screen.fill(backgrnd)
    draw_grid()
    draw_Markers()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            #Menu(mainTitle,messageMenu)
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            MxMy = pygame.mouse.get_pos()
            cellx=MxMy[0]//(WIDTH//3)
            celly=MxMy[1]//(HEIGHT//3)
            #print(cellx, celly)
            if markers[cellx][celly]==0:
                markers[cellx][celly]=player
                player *=-1
                checkWinner()
                print(winner)
                if gameOver: 
                    gameEnd()
            
            
            
    pygame.display.update() 
    pygame.time.delay(500)