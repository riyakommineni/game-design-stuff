#Riya Kommineni 
#06/17/22
#get username in pygame 

import pygame, os, sys

pygame.init()
os.system('clear')

clock = pygame.time.Clock
backgroundClr = (255,255,255)
WIDTH = 600 
HEIGHT = 600 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Get Name')
screen.fill(backgroundClr)
pygame.display.update()
run = True #run the while loop 
user_name = ''
nameClr = (0,105,105) #text of the name 
bxClr = (200,200,200)  #text box 

TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)
title = TITLE_FONT.render('Enter Name', 1, bxClr)
screen.blit(title,(WIDTH/2.5,HEIGHT//7))
pygame.time.delay(1000)
pygame.display.update()

namebox = pygame.Rect(WIDTH/2.5, HEIGHT//4,WIDTH//2, HEIGHT//5)
pygame.draw.rect(namebox)

while run: 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            #Menu(mainTitle,messageMenu)
            pygame.quit()
            sys.exit()
            print('You quit')
        if event.type == pygame.MOUSEBUTTONDOWN: 
            #draw box here 
         if event.type == pygame.KEYDOWN:
            if event == pygame.K_RETURN:
                print('name is in')
            
            if event == pygame.K_BACKSPACE: 
                print('user_name = username[:-1]')
            else: 
                print('user_name += event.unicode')
