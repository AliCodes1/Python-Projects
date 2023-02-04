from tkinter import Canvas,PhotoImage
import random
from enum import Enum
class Direction(Enum):

    # Directions
    EAST = 0
    WEST = 1
    NORTH = 2
    SOUTH = 3

class cars:

    def __init__(self,canvas,num=random.randint(1,9)):
        '''
        declare the variables 
        :param canvas:Canvas
        :param num:random int
        '''
        #set the canvas
        self.__canvas = canvas
        #set the canvas width and height
        self.__canvas_width = self.__canvas.winfo_width()
        self.__canvas_height = self.__canvas.winfo_height()
        #create images of the cars in the west and east positions
        self.__imgcarEast=[PhotoImage(file="sprites/car"+str(num)+"East.png").subsample(3)]
        self.__imgcarWest=[PhotoImage(file="sprites/car"+str(num)+"West.png").subsample(3)]
       
       #go through in range of 13
        for x in range(13):
            #create random number to generate cars
            num=random.randint(1,9)
            num2=random.randint(1,9)
            #add the image to the list
            self.__imgcarEast.append(PhotoImage(file="sprites/car"+str(num)+"East.png").subsample(3))
            self.__imgcarWest.append(PhotoImage(file="sprites/car"+str(num2)+"West.png").subsample(3))
            #set direction variable
            self.__direction=[]
        #create a list for 13 cars
        self.__imgcar=[]*13
        #go through 7 times
        for i in range(7):
            #add the car to the car string and add direction to the direction string
            self.__imgcar.append(self.__imgcarEast[i])
            self.__direction.append(Direction.EAST)
            self.__imgcar.append(self.__imgcarWest[i])
            self.__direction.append(Direction.WEST)

        #the cars speed variable
        self.__carspeed=0
        #set y and x position list
        self.__xpos=[-62,497,-62,497,-62,497,-62,497,-62,497,-62,497,-62,497,-62]
        self.__ypos=(645,605,565,485,445,405,365,325,285,245,165,125,85,45)
        
        #set the width and height of the car at the index
        self.__width=self.__imgcar[0].width()
        self.__height=self.__imgcar[0].height()
       
        #list to hold the cars for outputting
        self.__imgcarScreen=[]
        #index list variable
        self.__index=[]
      
    def getImage(self):
        '''
        Get the image of the car
        '''
        
        return self.__imgcar
    
    def getHeight(self):
        '''
        get the height of the car
        '''
        return self.__height
    
    def getLocation(self):
        '''
        return the location of the car
        '''
        return self.__xpos,self.__ypos
    
    def getWidth(self):
        '''
        return width of the car
        '''
        return self.__width
    
    def getX(self,i):
        '''
        get the x position at the specified index
        :param i:int
        '''
        return self.__xpos[self.__index[i]]
    
    def getY(self,i):
        '''
        get the y position at the specified index
        :param i: int
        '''
        return self.__ypos[self.__index[i]]

    def placeImage(self,i):
        '''
        create the image object on the canvas at the specified location
        :param i:int
        '''
        self.__index.append(i)
        self.__imgcarScreen.append(self.__canvas.create_image(self.__xpos[self.__index[i]], self.__ypos[self.__index[i]], image=self.__imgcar[self.__index[i]], anchor='nw'))
    
    def move(self,i,speed=3):
        '''
        move the car at the specified speed 
        :param i:int
        :param speed:int
        '''
        #if the direction is east
        if self.__direction[self.__index[i]]==Direction.EAST:
            #get the cars x position and increase it by the speed
            self.__xpos[self.__index[i]]+=speed
            #if the x position is more than or equal to 497
            if self.__xpos[self.__index[i]]>=497:
                #set the position to -62
                self.__xpos[self.__index[i]]=-62
        #if direction is west
        if self.__direction[self.__index[i]]==Direction.WEST:
            #get the cars x position and decrease it by the speed
            self.__xpos[self.__index[i]]-=speed
            #if the x position is less than or equal to -62
            if self.__xpos[self.__index[i]]<=-62:
                #set x position to 497
                self.__xpos[self.__index[i]]=497
        #update the images
        self.updateChar(i)

    
    def updateChar(self,i):
        '''
        update the image of the cars at the new location
        :param i:int
        '''
        self.__canvas.itemconfig(self.__imgcarScreen[self.__index[i]], image=self.__imgcar[self.__index[i]])
        self.__canvas.coords(self.__imgcarScreen[self.__index[i]], self.__xpos[self.__index[i]], self.__ypos[self.__index[i]])

    def reset(self):
        '''
        reset the x and y positions of the cars
        '''
        self.__xpos=[-62,497,-62,497,-62,497,-62,497,-62,497,-62,497,-62,497,-62]
        self.__ypos=(645,605,565,485,445,405,365,325,285,245,165,125,85,45)
        #go through each car and update the new location
        for i in range(12):
            self.updateChar(i)
    
    def getBounds(self,i):
        '''
        get the boundaries of the cars
        :param i:int
        '''
        x1 = self.__canvas.bbox(self.__imgcarScreen[i])[0]# Left side
        y1 = self.__canvas.bbox(self.__imgcarScreen[i])[1] # Top side
        x2 = self.__canvas.bbox(self.__imgcarScreen[i])[2] # Right side
        y2 = self.__canvas.bbox(self.__imgcarScreen[i])[3] # Bottom side
        #put the boundaries in a string and return it 
        bounds = [x1, y1, x2, y2]
        return bounds
#create class for chicken      
class chicken:
    
    def __init__(self,canvas):
        '''
        declare variables used in the class
        :param canvas:Canvas
        '''
        #make the chicken and the dead chicken images
        self.__imgchicken=PhotoImage(file="sprites/chicken_small.png")
        self.__imgdead=PhotoImage(file="sprites/dead_chicken.png")
        
        #set the canvas
        self.__canvas=canvas
        #set x and y positions
        self.__xpos=249
        self.__ypos=685
        #the list of positions
        self.__yposlist=(685,645,605,565,525,485,445,405,365,325,285,245,205,165,125,85,45)
        
        #set width and height of the chicken
        self.__width=self.__imgchicken.width()
        self.__height=self.__imgchicken.height()
        
        #boolean variables if dead or reset
        self.__reset=False
        self.__dead=False
        
        #string for placeimage variable
        self.__placeImage=""
    def getWidth(self):
        '''
        get the width of the chicken
        '''
        return self.__width
    
    def getHeight(self):
        '''
        return the height of the chicken
        '''
        return self.__height
    
    def getLocation(self):
        '''
        return the location of the chicken
        '''
        return self.__xpos,self.__ypos
    
    def setY(self,y):
        '''
        set the y position of the chicken
        :param y:int
        '''
        self.__ypos=y
    
    def setX(self,x):
        '''
        set x position of the string
        :param x:int
        '''
        self.__xpos=x
    
    def getY(self):
        '''
        get the y position of the chicken
        '''
        return self.__ypos
    
    def getX(self):
        '''
        return the x position of the chicken
        '''
        return self.__xpos
    
    def isItDead(self):
        '''
        return if the chicken is dead 
        '''
        return self.__dead
    
    def moveup(self,i):
        '''
        go through the y positions and set them 
        :param i:int
        '''
        self.__ypos=self.__yposlist[i]
        #output the chicken
        self.output()
    def movedown(self,i):
        '''
        go through the y positions and set them 
        :param i:int
        '''
        self.__ypos=self.__yposlist[i]
        #output the chicken
        self.output()

    def killChicken(self):
        '''
        if the chicken is dead place the dead image at the location
        '''
        self.__canvas.itemconfig(self.__placeImage,image=self.__imgdead)
        self.__canvas.coords(self.__placeImage,self.__xpos,self.__ypos)
        
    def reset(self):
        '''
        if reset than set y and x positions to the original and output the chicken
        '''
        self.__xpos=249
        self.__ypos=685
        self.output()
        
    def placeImage(self):
        '''
        place the image of the chicken
        '''
        self.__placeImage=self.__canvas.create_image(self.__xpos,self.__ypos,image=self.__imgchicken,anchor="nw")

    def output(self):
        '''
        ouput the chicken at the location
        '''
        self.__canvas.itemconfig(self.__placeImage,image=self.__imgchicken)
        self.__canvas.coords(self.__placeImage,self.__xpos,self.__ypos)
    
    def getBounds(self):
        '''
        return the boundaries of the chicken 
        '''
        return [(self.__canvas.bbox(self.__placeImage)[0] + 4), (self.__canvas.bbox(self.__placeImage)[1]), (self.__canvas.bbox(self.__placeImage)[2] - 4),(self.__canvas.bbox(self.__placeImage)[3])] 
