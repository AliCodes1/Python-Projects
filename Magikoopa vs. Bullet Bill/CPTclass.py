import pygame
'''
Name: Muhammad Ali
Date: Friday, April 9th, 2021 
Course Code: ICS3U1-02
Program: Magikoopa vs. Bullet Bill
'''
#magikoopa class
class Magikoopa:
    #constructor
    def __init__(self,surface,x=0,y=0):
        #east koopa
        self.__imgEast=pygame.image.load("images/koopaEast.png")
        #west koopa
        self.__imgWest=pygame.image.load("images/koopaWest.png")
        #east dead koopa
        self.__imgEastDead=pygame.image.load("images/deadEast.png")
        #westdead koopa
        self.__imgWestDead=pygame.image.load("images/deadWest.png")
        #x position variable
        self.__xpos=x
        #y position variable
        self.__ypos=y
        #width of koopa
        self.__width=self.__imgEast.get_width()
        #height of koopa
        self.__height=self.__imgEast.get_height()
        #bool to check if koopa is dead
        self.__dead=False
        #surface
        self.__surface=surface
        #direction
        self.__direction="east"
    
    #function to move koopa up
    def move_up(self, byhowmuch):
        self.__ypos -= byhowmuch
    #function kill koopa
    def is_dead(self):
        if self.__direction=="east":
            self.__surface.blit(self.__imgEastDead, (self.__xpos, self.__ypos))
            
        else:
            self.__surface.blit(self.__imgWestDead, (self.__xpos, self.__ypos))    
    #function to move down by a number
    def move_down(self, byhowmuch):
        self.__ypos += byhowmuch
    #function to move right by a number
    def move_right(self, byhowmuch):
        self.__xpos += byhowmuch
        self.__direction = "east"

    #function to move left by a number
    def move_left(self, byhowmuch):
        self.__xpos -= byhowmuch
        self.__direction = "west"

    #get the height of koopa 
    def get_height(self):
        return self.__height
    #get the width of koopa
    def get_width(self):
        return self.__width
    #set the x and y for koopa
    def set_location(self, x, y):
        self.__xpos = x
        self.__ypos = y
    #show koopa according to his direction
    def showme(self):
        if self.__direction=="east":
            self.__surface.blit(self.__imgEast, (self.__xpos, self.__ypos))
        else:
            self.__surface.blit(self.__imgWest, (self.__xpos, self.__ypos))

    #set the x for koopa
    def setX(self, x):
        self.__xpos = x
    #set y for koopa
    def setY(self, y):
        self.__ypos = y
    #move koopa down
    def move(self, move=True):
        self.__ypos +=1
    #get x for koopa
    def getX(self):
        return self.__xpos
    #get y for koopa
    def getY(self):
        return self.__ypos
    #get the boundaries koopa is within
    def get_bounds(self):
        return pygame.Rect(self.__xpos, self.__ypos,self.__width, self.__height)
#bullet bill class
class BulletBill():
    #constructor
    def __init__(self,surface,x=0,y=0):
        #image of the bullet
        self.__imgBullet=pygame.image.load("images/bulletWest.png")
        #the x pos
        self.__xpos=x
        #the y pos
        self.__ypos=y
        #the width of the bullet 
        self.__width=self.__imgBullet.get_width()
        #the height of the bullet
        self.__height=self.__imgBullet.get_height()
        #the surface
        self.__surface=surface
    #get the boundaries bill is within
    def get_bounds(self):
        return pygame.Rect(self.__xpos, self.__ypos,self.__width, self.__height)
    #Set x for bill
    def setX(self, x):
        self.__xpos = x
    #set y for bill
    def setY(self, y):
        self.__ypos = y
    #get x pos for bill
    def getX(self):
        return self.__xpos
    #get y pos for bill
    def getY(self):
        return self.__ypos
    #get bills height
    def get_height(self):
        return self.__height
    #get bill width
    def get_width(self):
        return self.__width
    #move bill to the left
    def move(self):
        self.__xpos -=1
    #show bill
    def showme(self):
        self.__surface.blit(self.__imgBullet, (self.__xpos, self.__ypos))
    # set x and y pos for bill  
    def set_position(self, x, y):
        self.__xpos = x
        self.__ypos = y
    
