from tkinter import Tk, Frame, Label, Button, font
from Diceclass import  Diceclass
def rolldice():
    lblleft.config(image=myDice[0].roll())
    lblright.config(image=myDice[1].roll())

    lblOutput.config(text="You rolled a "+str(myDice[0].getValue()+myDice[1].getValue())+"!" )
root = Tk()
root.title("Dice Class")

frame = Frame(root, padx=20, pady=20)
frame.pack()

lblOutput = Label(frame, text="Click ROLL to begin", font=font.Font(family="Britannic Bold", size=14))
lblOutput.grid(row=2, column=0, columnspan=2, pady=5)

btnRoll = Button(frame, text="ROLL", width=15,command=rolldice)
btnRoll.grid(row=1, column=0, pady=5)
btnClear = Button(frame, text="CLEAR", width=15)
btnClear.grid(row=1, column=1, pady=5)

myDice=[]
for x in range(2):
    myDice.append(Diceclass())
lblleft=Label(frame,image=myDice[0].getImage())
lblleft.grid(row=0,column=0)

lblright=Label(frame,image=myDice[1].getImage())
lblright.grid(row=0,column=1)
root.mainloop()