from cardclass import Card
import random

class Deck:
    
    def __init__(self):
        self.__cardlist = [None] * 52
        self.__cardsRemaining = 52
        self.__cardsDealt = 0
        self.__cardindex = -1
        
        suits = ('SPADES', 'DIAMONDS', 'HEARTS', 'CLUBS')
        index = 0
        
        for x in range(2, 15):
            for s in suits:
                self.__cardlist[index] = Card()
                self.__cardlist[index].set_image('images/' + str(x) + s[0] + '.gif')
                self.__cardlist[index].set_value(x)
                self.__cardlist[index].set_suit(s)
                
                if x == 11:
                    self.__name = 'jack'
                elif x == 12:
                    self.__name = 'queen'
                elif x == 13:
                    self.__name = 'king'
                elif x == 14:
                    self.__name = 'ace'
                else:
                    self.__name = str(x)
                
                self.__name += ' OF ' + s
                
                index += 1
    
    def shuffle_deck(self):
        random.shuffle(self.__cardlist)
    
    def deal_card(self):
        for x in range(6):
            self.__cardindex += 1
            return self.__cardlist[self.__cardindex]