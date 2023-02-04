from tkinter import PhotoImage

class Card:
    
    def __init__(self):
        self.__imgCard = PhotoImage(file='images/back.png')
        self.__value = 0
        self.__suit = None
        self.__name = None
        self.__width = self.__imgCard.width()
        self.__height = self.__imgCard.height()
    
    def get_image(self):
        return self.__imgCard

    def get_value(self):
        return self.__value
    
    def get_suit(self):
        return self.__suit
    
    def get_name(self):
        return self.__name
    
    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height
    
    def get_dimensions(self):
        return (self.__width, self.__height)
    
    def set_image(self, img):
        self.__imgCard = PhotoImage(file=img)
        self.__width = self.__imgCard.width()
        self.__height = self.__imgCard.height()
    
    def set_value(self, val):
        self.__value = val
    
    def set_name(self, name):
        self.__name = name
    
    def set_width(self, w):
        self.__width = w
    
    def set_height(self, h):
        self.__height = h
    
    def set_suit(self, suit):
        self.__suit = suit