from tkinter import PhotoImage
import random
class Diceclass:
    
    
    #Define our constructer
    def __init__(self):
        self.__diceValue=0
        self.__img=PhotoImage(file="images/dice"+str(self.__diceValue)+".png")
        
    def getImage(self):
        return self.__img
    
    def roll(self):
        self.__diceValue=random.randint(1,6)
        self.__img=PhotoImage(file="images/dice"+str(self.__diceValue)+".png")
        return self.__img
    
    def getValue(self):
        return self.__diceValue