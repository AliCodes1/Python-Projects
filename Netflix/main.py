from tkinter import Tk, Frame, Button, Label, Entry, PhotoImage, font,END
from Movie import Movie
root = Tk()
root.title("Netflix")

def add_save():
    global currentindex
    if btnAdd.cget("text")=="SAVE":
        btnAdd.config(text="ADD")
        m=Movie()
        m.set_title(txtInput[0].get())
        m.set_director(txtInput[1].get())
        m.set_length(txtInput[2].get())
        m.set_genre(txtInput[3].get())
        m.set_year(txtInput[4].get())
        movielist.append(m)
        
        for x in range(len(txtInput)):
            txtInput[x].config(state="disabled")
            
        print(movielist[0].get_movieinfo())
    elif btnAdd.cget("text")=="ADD":
        btnAdd.config(text="Save")
        for x in range(len(txtInput)):
            txtInput[x].config(state="normal")
            txtInput[x].delete(0,END)
        txtInput[0].focus()
        currentindex+=1
        
def go_back():
    global currentindex
    currentindex-=1
    clear_entries()
    movie_tuple=movielist[currentindex].get_info()
    
    txtInput[0].insert(END,movielist[currentindex].get_title())

def enable_entries():
    for x in range(len(txtInput)):
        txtInput[x].config(state="normal")
def clear_entries():
    for x in range(len(txtInput)):
        txtInput[x].config(state="normal")
        txtInput[x].delete(0,END)
def disable_entries():
    for x in range(len(txtInput)):
        txtInput[x].config(state="normal")
        txtInput[x].delete(0,END)

frame = Frame(root, padx=20, pady=20, background="#b9090b")
frame.pack()

bottomFrame = Frame(frame, padx=10, pady=10, background="#b9090b")
bottomFrame.grid(row=6, column=0, columnspan=2)

btnBack = Button(bottomFrame, text="BACK", width=13, height=2, font=font.Font(family="TkDeafultFont", size=9, weight="bold"),command=go_back)
btnBack.grid(row=0, column=0, padx=5)

btnForward = Button(bottomFrame, text="FORWARD", width=13, height=2, font=font.Font(family="TkDeafultFont", size=9, weight="bold"))
btnForward.grid(row=0, column=2, padx=5)

btnAdd = Button(bottomFrame, text="ADD", width=13, height=2, font=font.Font(family="TkDeafultFont", size=9, weight="bold"),command=add_save)
btnAdd.grid(row=0, column=1, padx=5)

lblList = [0] * 5
lblText = ["TITLE:", "DIRECTOR:", "LENGTH (mins):", "GENRE:", "YEAR:"]

for index in range(len(lblList)):
    lblList[index] = Label(frame, text=lblText[index], pady=5, width=15, anchor="w", padx=5, background="#b9090b", fg="white",
                           font=font.Font(family="TkDefaultFont", weight="bold", size=10))
    lblList[index].grid(row=index + 1, column=0, sticky="nw", padx=5, pady=5)

txtInput = [0] * 5

for index in range(len(txtInput)):
    txtInput[index] = Entry(frame, width=30, justify="center", borderwidth=2, state="disable")
    txtInput[index].grid(row=index + 1, column=1, padx=5)

imgNetflix = PhotoImage(file="netflix_logo.png")
imgNetflix = imgNetflix.subsample(2)
lblTitle = Label(frame, image=imgNetflix, border=0)
lblTitle.grid(row=0, column=0, columnspan=2)

movielist=[]
currentindex=""
root.mainloop()
