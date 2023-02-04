#import
import pygame, os,random
from tkinter import Tk,messagebox
from CPTclass import Magikoopa, BulletBill
from pygame.locals import *
'''
Name: Muhammad Ali
Date: Friday, April 9th, 2021 
Course Code: ICS3U1-02
Program: Magikoopa vs. Bullet Bill
'''
#create a tinker window and make it disappear
root = Tk()
root.withdraw()
#timer to see if koopa stays in bounds and to see if he touches the ground then he dies
def koopa_timer():
    #globalize variables
    global startgame
    global surface
    global show
    global numlives
    global play
    global redo_game
    global gameover_output
    global show_message
    #check if koopa goes to the left too much if he does set him to 0
    if koopa.getX() < 0:
        koopa.setX(0)
    #Check if koopa goes to the right to much if so than set him to surface width - koopas width
    if koopa.getX() + koopa.get_width() > surface.get_width():
        koopa.setX(surface.get_width() - koopa.get_width())
    #check if goes up to much too much if so set him to 50
    if koopa.getY() < 50:
        koopa.setY(50)
    #check if koopa hits near the ground if so make him die
    if koopa.getY() + koopa.get_height() > surface.get_height()-30:
        koopa.setY(surface.get_height() - koopa.get_height()-30)
        #koopa dies
        koopa.is_dead()
        #This will make sure that his old body is not shown only the grayscale
        show=False
        #this outputs the starting position 
        startgame=False
        #decrease the life number
        numlives=numlives-1
        #if koopa hits a bullet don't show this but if he touches the ground than output this
        if show_message==True:
            #output message box
            messagebox.showinfo("Magikoopa vs. Bullet Bill","You crash landed!")
        
#this generates the bullets
def bulletBill_spawner():
    #globalize variables
    global startgame
    global score
    #add the bullet to the list
    bulletBill_20.append(BulletBill(surface,surface.get_width()+50, random.randint(50,pygame.display.get_surface().get_height() - 30)))
#make the bullet move every second
def bulletBill_timer():
    #glabalize variables
    global surface
    global startgame
    global score
    global moveBullet
    #if move bullet is true the bullet will keep on moving until collision is detected
    if moveBullet==True:
        #goes through the list
        for b in bulletBill_20:
            #move the bullet
            b.move()
            #if bullet goes past the left side 
            if b.getX()== -75:
                #increase points by 100
                score+=100
            #if the bullet is too low it will set it a little higher to prevent being cut off
            if b.getY() + b.get_height() > surface.get_height()-30:
                b.setY(surface.get_height() - b.get_height()-30)
        

#score
score = 0
#this show the starting position and the click the spacebar to start output
show=True

os.environ['SDL_VIDEO_CENTERED'] = '1'
#initialize pygame modules 
pygame.init()
#create window
pygame.display.set_caption('Bullet Bill')
#hide mouse
pygame.mouse.set_visible(False)
pygame.key.set_repeat(50)

#variable to load the background
imgbackground = pygame.image.load('images/game-background.png')
#variable for the title 
imgtitle = pygame.image.load('images/title.png')

#set the size of the window with the background measurements
surface = pygame.display.set_mode((imgbackground.get_width(), imgbackground.get_height()))

#variable for fonts
score_font = pygame.font.Font('magicdreams.ttf', 28)
game_font = pygame.font.Font('magicdreams.ttf', 48)

#output variables for text and rendering
start_output = game_font.render('CLICK SPACEBAR TO START', True, pygame.Color('#426b94'))
score_output = score_font.render("{:<8s}{:<5d}".format('SCORE:', score), True, pygame.Color('#426b94'))
gameover_output = game_font.render('GAME OVER', True, pygame.Color('#426b94'))
#variable for window loop
done = False
#measurement for borders
TOP_BORDER, BOTTOM_BORDER = 50, pygame.display.get_surface().get_height() - 30

#the amount of lives and varible that is used to cycle through the images
imglives = [None] * 4
numlives = 3

#load koopa
koopaIMG=pygame.image.load("images/koopaEast.png")
#call the class
koopa=Magikoopa(surface)
#set x for koopa
koopa.setX(0)
#set y for koopa
koopa.setY(pygame.display.get_surface().get_height() // 2)

#the timers 
#the timer for koopa
pygame.time.set_timer(pygame.USEREVENT,10)
#timer for bullet generator
pygame.time.set_timer(pygame.USEREVENT + 1,1000)
#timer for bullet movement 
pygame.time.set_timer(pygame.USEREVENT + 2,10)
#this output most of the game if false the game wouldn't show up
redo_game=True
#startgame is the beginning like click the space bar and showing koopa
startgame=False
#If true the bullet will move
moveBullet=True
#list of bullets
bulletBill_20=[]
#if play is true you can press buttons if not then you cannot 
play=True
#shows the you crashed message if true
show_message=True
#go through the images for lives
for i in range(len(imglives)):
    imglives[i] = pygame.image.load('images/lives' + str(i) + '.png')
#start loop to output
while not done:
    #go through events
    for event in pygame.event.get():
        #if quit close window
        if event.type == pygame.QUIT:
            done = True
        #if this timer is chosen
        if event.type == pygame.USEREVENT:
            #output koopas timer
            koopa_timer()
        #if this timer is chosen
        if event.type == pygame.USEREVENT + 1:
            #output bullet spawners timer
            bulletBill_spawner()
        if event.type==pygame.USEREVENT + 2:
            #if koopa started moving
            if startgame==True:
                #output the bullet bill timer
                bulletBill_timer()
        #if play is true you can press buttons if not then you cannot 
        if play==True:
            #press a key
            if event.type==pygame.KEYDOWN:
                #if space key
                if event.key==K_SPACE:
                    #make koopa move
                    show=True
                    #make bullet move
                    startgame=True
                # if right or d key
                if event.key==K_d or event.key==K_RIGHT:
                    #make koopa move right 10 pixels
                    koopa.move_right(10)
                # if left or a key
                if event.key==K_a or event.key==K_LEFT:
                    #make koopa move left 10 pixels
                    koopa.move_left(10)
                # if w or up
                if event.key==K_w or event.key==K_UP:
                    #make koopa move up 10 pixels
                    koopa.move_up(10)
                # if s or a down
                if event.key==K_s or event.key==K_DOWN:
                    #make koopa move down 5 pixels
                    koopa.move_down(5)


    #add background            
    surface.blit(imgbackground, (0, 0))
    #add title
    surface.blit(imgtitle, (pygame.display.get_surface().get_width() // 2 - imgtitle.get_width() // 2, 10))
    #add lives
    surface.blit(imglives[numlives], (pygame.display.get_surface().get_width() - imglives[numlives].get_width() - 10, 15))
    
    #if lives are 0
    if numlives==0:
        #stop game
        redo_game=False
        #output game over
        surface.blit(gameover_output, (pygame.display.get_surface().get_width() // 2 - gameover_output.get_width() // 2,pygame.display.get_surface().get_height() // 2 - 115))
        #ask a question
        answer=messagebox.askyesno("Game Over", "GAME OVER! Would you like to play again")
        #if true
        if answer==True:
            #restart game
            redo_game=True
            score=0
            numlives=3
            bulletBill_20=[]
            
        # if false  
        if answer==False:
            #close the game or quit
            done=True
        
    #output the score    
    score_output = score_font.render("{:<8s}{:<5d}".format('SCORE:', score), True, pygame.Color('#426b94'))
    surface.blit(score_output, (15, 15))
    #if true run the game
    if redo_game==True:
        #output the beginning
        if startgame == False:
            #set x to 0 for koopa
            koopa.setX(0)
            #set koopa in the left middle
            koopa.setY(pygame.display.get_surface().get_height() // 2)
            #click spacebar output
            surface.blit(start_output, (pygame.display.get_surface().get_width() // 2 - start_output.get_width() // 2,
                pygame.display.get_surface().get_height() // 2 - 115))
            #show koopa
            surface.blit(koopaIMG,(0,pygame.display.get_surface().get_height() // 2))
            showkoopa=True
            #press keys
            play=True
            #able to move bullet bool
            moveBullet=True
            #show message bool
            show_message=True
        #start the beginning
        if startgame==True:
            #make koopa move
            koopa.move()
            #go through the bullets and show them
            for i,b in enumerate(bulletBill_20):
                if show==True:
                    b.showme()
                #if collide with koopa 
                if BulletBill.get_bounds(b).colliderect(Magikoopa.get_bounds(koopa)):
                    #show koopa dead
                    show=False
                    #reset bullets
                    bulletBill_20=[]
                    #don't move bullets
                    moveBullet=False
                    # don't display the message
                    show_message=False
                    
            #show false show koopa dead  
            if show==False:
                koopa.is_dead()
                #don't show koopa alive
                showkoopa=False
                #dont be able to press buttons
                play=False 
            #show koopa if true
            if showkoopa==True:
                koopa.showme()
    #update screen           
    pygame.display.update()
    #fill the background
    surface.blit(imgbackground, (0, 0))
