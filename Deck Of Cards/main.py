from tkinter import Tk, Frame, Label, Button, FLAT
from cardclass import Card
from deckclass import Deck

def deal():
    firstCard = deckofcards.deal_card()
    lblFirst.config(image=firstCard.get_image())
    
    secondCard = deckofcards.deal_card()
    print(secondCard.get_name)
    lblSecond.config(image=secondCard.get_image(), text=secondCard.get_name())
    
root = Tk()
root.title("Deck of Cards")

firstCard = Card()
secondCard = Card()

deckofcards = Deck()
deckofcards.shuffle_deck()

frame = Frame(root, padx=10, pady=10, bd=1, relief=FLAT)
frame.pack()

lblFirst = Label(frame, wraplength=70, compound='top', image=firstCard.get_image())
lblFirst.grid(row=1, column=0, padx=5)

lblSecond = Label(frame, wraplength=70, compound='top', text='', image=secondCard.get_image())
lblSecond.grid(row=1, column=1, padx=5)

btnDeal = Button(frame, text="DEAL", width=10, command=deal)
btnDeal.grid(row=2, column=0, sticky="e", padx=5, pady=5)

btnReset = Button(frame, text="RESET", width=10)
btnReset.grid(row=2, column=1, sticky="w", padx=5, pady=5)

lblRemaining = Label(frame, text="Click DEAL to begin", font="TkDefaultFont 9 bold")
lblRemaining.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()