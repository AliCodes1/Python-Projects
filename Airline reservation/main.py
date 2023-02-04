"""
Name : Muhammad Ali
DATE: November 7th, 2021
PROGRAM: Airline Program
"""
#import
from tkinter import Tk, Frame, PhotoImage, Label, Button, Menu, simpledialog, messagebox, Toplevel, ttk, Scrollbar, END, filedialog
import os
#Function when assigning seat
def assign_seat(r,c):
    #global variables
    global aisle_num,aisles,passengers,file,waitlist
    #check bool
    check=False
    #waitlist function
    waitlist_info()
    #if buttons text is x
    if buttons[r][c].cget("text")=="x":    
        #go through passengers
        for x,z in enumerate(passengers):
            #if rows +1 =the seat number and column is the seat letter
            if r+1==passengers[x]["number"] and aisles[c]==passengers[x]["letter"]:
                #ask question message box
                response=messagebox.askyesno("Remove Passenger", "This seat is not available!\nWould you like to remove "+passengers[x]["first_name"]+" "+passengers[x]["last_name"]+" from "+str(passengers[x]["number"])+passengers[x]["letter"])
                #if response is yes
                if response==True:
                    #delete passengers at the index
                    del passengers[x]
                    #if wait list is not []
                    if waitlist!=[]:
                        #insert passenger
                        passengers.insert(x,{"first_name":waitlist[0]["first_name"],"last_name":waitlist[0]["last_name"],"number":r+1,"letter":aisles[c]})
                        #delete wait list at the index
                        del waitlist[0] 
                        #go through wait list                                        
                        for y,z in enumerate(waitlist):
                            #set the priority of the wait list
                            waitlist[y]["priority"]=y+1
                        #show info of message box
                        messagebox.showinfo("Add Passenger", passengers[x]["first_name"]+" "+passengers[x]["last_name"]+" has been removed from the waiting list and has been assigned "+str(passengers[x]["number"])+passengers[x]["letter"])
                    #if wait list is []
                    elif waitlist==[]:
                        #configure the button
                        buttons[r][c].config(highlightbackground="white",text=aisles[c])
                    #output functions
                    output_passenger()
                    output_waitlist()
    #if button is not x
    elif buttons[r][c].cget("text")!="x":
        #ask for the first name
        first_name=simpledialog.askstring("Add Passenger", "Enter passenger's first name:")
        #if first name is none
        if first_name==None:
            pass
        #if there is no first name or there is not an alphabet character
        elif first_name==""or first_name.isalpha()==False:
            #show error
            messagebox.showerror("Error", "Please enter a name!")
        #while the incorrect name is input
        while first_name==""or first_name.isalpha()==False or first_name==None:
            #ask for the name
            first_name=simpledialog.askstring("Add Passenger", "Enter passenger's first name:")
            #if no name
            if first_name==None:
                #output error
                messagebox.showerror("Error", "Please enter a name!")
            #if no alphabet in name
            elif first_name.isalpha()==False:
                #show error message
                messagebox.showerror("Error", "Please enter a name!")
        #ask last name
        last_name=simpledialog.askstring("Add Passenger", "Enter passenger's last name:")
        #if first name is none
        if last_name==None:
            pass
        #if the incorrect name is input
        elif last_name==""or last_name.isalpha()==False:
            #show error
            messagebox.showerror("Error", "Please enter a name!")
        #while the incorrect name is input
        while last_name==""or last_name.isalpha()==False or last_name==None:
            #ask for the name
            last_name=simpledialog.askstring("Add Passenger", "Enter passenger's last name:")
            #if no name
            if first_name==None:
                #ask error
                messagebox.showerror("Error", "Please enter a name!")
            #if no alphabet in name
            elif last_name.isalpha()==False:
                #show error message
                messagebox.showerror("Error", "Please enter a name!")
        #go through passengers
        for x,z in enumerate(passengers):
            #if the name are the same as the passengers name
            if first_name==passengers[x]["first_name"] and last_name==passengers[x]["last_name"]:
                #show error
                messagebox.showerror("Error",first_name+" "+last_name+" has already been assigned seat "+str(passengers[x]["number"])+passengers[x]["letter"]+"!")
                #bool variable
                check=True
        #if check is false
        if check==False:
            #configure the button
            buttons[r][c].config(highlightbackground="red",text="x")
            #add the passenger to the list
            passengers.append({"first_name":first_name,"last_name":last_name,"number":r+1,"letter":aisles[c]})
            #output function
            output_passenger()
#function to close the manifest 
def close_manifest():
    #show the window
    root.update()
    root.deiconify()
    #close the manifest
    tl_manifest.withdraw()
#function to open the manifest
def view_manifest():
    #close the manifest
    root.withdraw()
    #show the manifest window
    tl_manifest.update()
    tl_manifest.deiconify()
#function to close wait list
def close_waitlist():
    #show the window 
    root.update()
    root.deiconify()
    #close the wait list window
    tl_waitlist.withdraw()
#function for showing the wait list
def view_waitlist():
    #hide the window
    root.withdraw()
    #show wait list window
    tl_waitlist.update()
    tl_waitlist.deiconify()
    #output wait list
    waitlist_info()
#function to get wait list info
def waitlist_info():
    #global variables
    global waitlist,file,num
    #if num=0
    if num==0:
        #try this block of code
        try:
            #read the file
            with open(file,"r") as reader:
                #read the file
                data=reader.read()
                #split the data
                data=data.split("\n")
                #index
                index=0
                #go through the data
                for x in data:
                    #Split the data
                    data=x.split(",")
                    #add to the index
                    index+=1
                    #index is larger 82 and the data is not ""
                    if index>82 and not data=="":
                        #add to the wait list 
                        waitlist.append({"first_name":data[0],"last_name":data[1],"priority":int(data[2])})    
            #function to output the wait list  
            output_waitlist()
            #add to num variable
            num+=1
        #raise exception
        except NameError:
            #show error
            messagebox.showerror("Error", "Please select a file!")
#function to output wait list 
def output_waitlist():
    #global variable
    global waitlist
    # Delete/clear all the items in the tree view
    for i in tview_waitlist.get_children():
        tview_waitlist.delete(i)
    # Insert each item from the dictionary to the treeview
    for x in waitlist:
        tview_waitlist.insert("",END,values=(x["first_name"]+", "+x["last_name"],str(x["priority"])))
#function to open file
def file_open():
    #global variables
    global aisle_num,aisles,passengers,file,selected
    #if selected is true 
    if selected==True:
        #open a file
        file=filedialog.askopenfilename(initialdir=os.getcwd(),filetypes=[("Text files (*.txt)", "*.txt")])
        #read the file
        with open(file,"r") as reader:
            #read the data
            data=reader.read()
            #split the data
            data=data.split("\n")
        #variables
        index=0
        num=0     
        #go through data
        for x in data:
            #split the data
            data=x.split(",")
            #add to the index
            index+=1
            #if index is equal to or larger than 3 and not larger than 82
            if index>=3 and not index>82:
                #append to the passenger
                passengers.append({"first_name":data[0],"last_name":data[1],"number":int(data[2]),"letter":data[3]})
                #set the column
                c=passengers[num]["letter"]
                #set the row
                r=passengers[num]["number"]
                #go through aisles
                for x,z in enumerate(aisles):
                    #if column=z
                    if c==z:
                        #configure the button
                        buttons[int(r)-1][x].config(highlightbackground="red",text="x")
                        #add to num
                        num+=1
        #output the passenger
        output_passenger()
        #bool variable
        selected=False
    #if select=false
    elif selected==False:
        #show error
        messagebox.showerror("Error", "File has been selected!")
#function to output the passenger      
def output_passenger():
    #global variable
    global passengers
    # Delete/clear all the items in the tree view
    for i in tview_manifest.get_children():
        tview_manifest.delete(i)
    # Insert each item from the dictionary to the treeview
    for x in passengers:
        tview_manifest.insert("",END,values=(x["first_name"]+", "+x["last_name"],str(x["number"])+x["letter"]))
#sort the column
def sort_column(column):
    #global variables
    global passengers
    #if the column = 1
    if column==1:
        #sort the passengers
        passengers=sorted(passengers,key=lambda x:x["first_name"])
    #if the column=2
    elif column==2:
        #sort the passengers
        passengers=sorted(passengers,key=lambda x:(x["number"],x["letter"]))
    #output passenger function
    output_passenger()
#function to sort wait list
def waitlist_sort(column):
    #global variables
    global waitlist
    #if column = 1
    if column==1:
        #sort the wait list
        waitlist=sorted(waitlist,key=lambda x:x["first_name"])
    #if column = 2
    elif column==2:
        #sort the wait list
        waitlist=sorted(waitlist,key=lambda x:(x["priority"]))
    #output wait list
    output_waitlist()
#function for selected wait list
def selected_(event): 
    #global variables
    global select,item
    #select the wait list
    select=tview_waitlist.selection()
    #get item from the wait list
    item=tview_waitlist.item(select)
#function to remove from wait list
def remove_():
    #global variables
    global select,item,waitlist
    #get the selected wait list
    select=tview_waitlist.selection()
    #get the index of the wait list
    index=tview_waitlist.index(select)
    #if the wait list is empty 
    if waitlist==[]:
        #configure remove button
        btnRemove.config(state="disabled")
    #if selection is not empty
    elif select!=():
        #configure remove button
        btnRemove.config(state="normal")
        #get the values of the wait list
        name=tview_waitlist.item(select)["values"]
        #ask question
        response=messagebox.askyesno("Remove Player", "Are you sure you want to remove "+name[0].replace(", "," ")+"?")
        #if response = true
        if response==True:
            #delete wait list
            tview_waitlist.delete(select)
            #delete wait list at the index
            del waitlist[index]
            #go through the wait list
            for x,z in enumerate(waitlist):
                #set the priority
                waitlist[x]["priority"]=x+1
            #output wait list
            output_waitlist()
        #response = false
        if response==False:
            pass
    #if selection is empty
    elif select==():
        #show error
        messagebox.showerror("Error", "Please select a wait list member to remove!")
#add function
def add_():
    #global variables
    global waitlist,same,passengers
    #if the length of the passengers = 80
    if len(passengers)==80:
        #ask for the first name
        first_name=simpledialog.askstring("Add Passenger", "Enter passenger's first name:")
        if first_name==None:
            #close the question
            exit()
    
        if first_name==""or first_name.isalpha()==False:
            #show error
            messagebox.showerror("Error", "Please enter a name!")
        #while the incorrect name is input
        while first_name==""or first_name.isalpha()==False:
            #ask for the name
            first_name=simpledialog.askstring("Add Passenger", "Enter passenger's first name:")
            #if not an alphabet
            if first_name.isalpha()==False:
                #show error message
                messagebox.showerror("Error", "Please enter a name!")
        #ask for the passengers last name
        last_name=simpledialog.askstring("Add Passenger", "Enter passenger's last name:")
        
        if last_name==None:
            pass
        if last_name==""or last_name.isalpha()==False:
            #show error
            messagebox.showerror("Error", "Please enter a name!")
       
        #while the incorrect name is input
        while last_name==""or last_name.isalpha()==False:
            #ask for the name
            last_name=simpledialog.askstring("Add Passenger", "Enter passenger's last name:")
            #if not an alphabet
            if last_name.isalpha()==False:
                #show error message
                messagebox.showerror("Error", "Please enter a name!")
        #go through the wait list
        for x,z in enumerate(waitlist):
            #if the first and last name are the same 
            if first_name==waitlist[x]["first_name"] and last_name==waitlist[x]["last_name"]:
                #show error
                messagebox.showerror("Error",first_name+" "+last_name+" is already on the wait list!")
                #bool variable
                same=True
        #if same = False
        if same==False:
            #select the wait list
            select=tview_waitlist.selection()
            #get the index at the wait list
            index=tview_waitlist.index(select)
            #if index is 0
            if index==0:
                #make index the length of the wait list
                index=len(waitlist)
            #add to the wait list
            waitlist.insert(index+1,{"first_name":first_name,"last_name":last_name,"priority":int(index+1)})      
            #go through the wait list
            for x,z in enumerate(waitlist):
                #set the priority of the wait list
                waitlist[x]["priority"]=x+1
            #output the wait list
            output_waitlist()
    #anything else        
    else:
        #show error
        messagebox.showerror("Error", "You cannot add a passenger to the wait list while there are seats available.")
#function to go up
def up_():
    #global variable
    global waitlist
    #if wait list is empty
    if waitlist==[]:
        #disable button
        btnUp.config(state="disabled")
    #else
    else:
        #enable the button
        btnUp.config(state="normal")
        #select from the wait list
        iids = tview_waitlist.selection()
        #go through the wait list selection
        for iids in iids:
            #get the index of the wait list
            index=tview_waitlist.index(iids)
            #get the first name
            name1=waitlist[index-1].get("first_name")
            #get the last name
            name2=waitlist[index-1].get("last_name")
            #get the first name
            name3=waitlist[index].get("first_name")
            #get the last name
            name4=waitlist[index].get("last_name")
            #update the wait list
            waitlist[index].update({"first_name":name1,"last_name":name2})
            #update the wait list
            waitlist[index-1].update({"first_name":name3,"last_name":name4})
            #output wait list
            output_waitlist()
#function to go down   
def down_():
    #global variable
    global waitlist
    #if wait list is empty
    if waitlist==[]:
        #disable the button
        btnDown.config(state="disabled")
    #anything else
    else:
        #enable the button
        btnDown.config(state="normal")
        #get the selected person in the wait list
        iids = tview_waitlist.selection()
        #go through the id
        for iids in iids:
            #get the index of the id
            index=tview_waitlist.index(iids)
            #get the first name
            name1=waitlist[index+1].get("first_name")
            #get the last name
            name2=waitlist[index+1].get("last_name")
            #get the first name
            name3=waitlist[index].get("first_name")
            #get the last name
            name4=waitlist[index].get("last_name")
            #update the wait list
            waitlist[index].update({"first_name":name1,"last_name":name2})
            waitlist[index+1].update({"first_name":name3,"last_name":name4})
            #output the wait list
            output_waitlist()
#function to save the file
def file_save():
    #global variables
    global waitlist,passengers
    #output the wait list
    waitlist_info()
    #get the length of the wait list 
    len1=len(waitlist)
    #get the length of the passengers
    len2=len(passengers)
    #save the file 
    file=filedialog.asksaveasfilename(initialdir=os.getcwd(),filetypes=[("Text files (*.txt)", "*.txt")])
    #while file is empty
    while file=="":
        #show error 
        messagebox.showerror("Error", "Please select a file!")
        #save the file
        file=filedialog.asksaveasfilename(initialdir=os.getcwd(),filetypes=[("Text files (*.txt)", "*.txt")])
    #write in the file
    with open(file,"w") as writer:
        writer.write(str(len2)+'\n'+str(len1)+"\n")
        #go through in the length of the passengers
        for x in range(len(passengers)):
            writer.write(passengers[x]["first_name"]+","+passengers[x]["last_name"]+","+str(passengers[x]["number"])+","+passengers[x]["letter"]+"\n")
        #go through in the length of wait list
        for y in range(len(waitlist)):
            writer.write(waitlist[y]["first_name"]+","+waitlist[y]["last_name"]+","+str(waitlist[y]["priority"])+"\n")
#function to exit the program
def exit_program():
    #ask question
    response=messagebox.askyesno("Exit", "Would you like to exit the program?")
    #if response is yea
    if response==True:
        #exit
        exit()
    #if response is false
    if response==False:
        pass
#set variables
aisles = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
aisle_num=["1","2","3","4","5","6","7","8","9","10"]
passengers=[]
waitlist=[]
same=False
selected = True
num=0
#set height and width of window
WINDOW_WIDTH, WINDOW_HEIGHT = 668, 734
#create window
root = Tk()
#set title of window
root.title('Airline Reservation')
#place the window in the middle of the screen
root.geometry('%dx%d+%d+%d' % (WINDOW_WIDTH, WINDOW_HEIGHT, root.winfo_screenwidth() // 2 - WINDOW_WIDTH // 2, root.winfo_screenheight() // 2 - WINDOW_HEIGHT // 2))
root.resizable(False, False)
#create menu bar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
#label the menu 
filemenu.add_command(label='Open', command=file_open)
#label the menu 
filemenu.add_command(label='Save', command=file_save)
menubar.add_cascade(label="File", menu=filemenu)
#create menu in the munu bar
viewmenu = Menu(menubar, tearoff=0)
#label the menu 
viewmenu.add_command(label='Manifest', command=view_manifest)
#label the menu 
viewmenu.add_command(label='Wait List', command=view_waitlist)
menubar.add_cascade(label='View', menu=viewmenu)
#configure root
root.config(menu=menubar)
#exit program when function is called
root.protocol("WM_DELETE_WINDOW", exit_program)
#create and set properties of the frame
frame = Frame(root, padx=20, pady=20, bg='white')
#pack the frame
frame.pack()
#create image
imgLogo = PhotoImage(file='images/air-canada-logo.png')
#insert image in the label
lblLogo = Label(frame, image=imgLogo, borderwidth=0, padx=10, pady=10, bg='white')
#place the image
lblLogo.grid(row=0, column=0, padx=10, pady=10, columnspan=11)
#2D list of buttons
buttons = [[0 for cols in range(8)] for rows in range(10)]
#set variables
labels = []
rownum, colnum = 1, 0
#go through the rows
for rows in range(len(buttons)):
    #add to the label
    labels.append(Label(frame, width=2, height=1, text=str(rownum), font='TkDefaultFont 10 bold', fg='red', bg='white', padx=2, pady=2).grid(row=rownum, column=colnum))
    #add 1 to colnum
    colnum += 1
    #go through the columns
    for cols in range(len(buttons[rows])):
        #create and set properties of the button
        buttons[rows][cols] = Button(frame, width=5, height=2, text=aisles[cols],command=lambda rows=rows,cols=cols:assign_seat(rows,cols))
        #place the buttons
        buttons[rows][cols].grid(row=rownum, column=colnum, padx=3, pady=3)
        #add 1 to colnum
        colnum += 1
        #if column is 1 or 5
        if cols == 1 or cols == 5:
            #add to the labels list
            labels.append(Label(frame, width=6, height=3, bg='white').grid(row=rownum, column=colnum))
            #add 1 to colnum
            colnum += 1
    #set variables
    colnum = 0
    #add 1 to rownum
    rownum += 1
#create image
img = PhotoImage(file='images/air-canada-alternate.png')
#create and set properties of the top level widget
tl_manifest = Toplevel(padx=10, pady=10, bg='white')
#title the window
tl_manifest.title('Manifest')
tl_manifest.resizable(False, False)
#close when close is clicked
tl_manifest.protocol('WM_DELETE_WINDOW', close_manifest)
#don't show the window
tl_manifest.withdraw()
#create label for image
lblImg = Label(tl_manifest, image=img, borderwidth=0)
#place the label
lblImg.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
#create style
style = ttk.Style()
#configure style
style.configure('mystyle.Treeview.Heading', font=('Consolas', 11, 'bold'), bg='white')
#configure style
style.configure('mystyle.Treeview', font=('Consolas', 11))
#create and set properties of the tree view widget 
tview_manifest = ttk.Treeview(tl_manifest, selectmode='browse', columns=('1', '2'), show='headings', height=20, style='mystyle.Treeview')
#place the widget
tview_manifest.grid(row=1, column=0, pady=5)
#variables
info=[]
#headings for the manifest
manifest_headings = ('NAME', 'SEAT')
#set column widths
columnwidths = [250, 100]
#go through 2 times
for i in range(2):
    #configure the column of the tree view widget
    tview_manifest.column(str(i+1), width=columnwidths[i], anchor='w')
    #set heading for the tree view widget
    tview_manifest.heading(str(i+1), text=manifest_headings[i], anchor='w',command=lambda column=i+1:sort_column(column))
#create and set properties of the scroll bar
vscroll_manifest = Scrollbar(tl_manifest, orient='vertical', command=tview_manifest.yview)
#place the scroll bar
vscroll_manifest.grid(row=1, column=1, sticky='ns')
#create top level widget
tl_waitlist = Toplevel(padx=10, pady=10, bg='white')
#set title 
tl_waitlist.title('Wait List')
tl_waitlist.resizable(False, False)
#close when close is clicked
tl_waitlist.protocol('WM_DELETE_WINDOW', close_waitlist)
#hide the window
tl_waitlist.withdraw()
#label for the image
lblWaitLogo = Label(tl_waitlist, image=img, borderwidth=0)
#place the label
lblWaitLogo.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
#create and set properties of the tree view widget
tview_waitlist = ttk.Treeview(tl_waitlist, selectmode='browse', columns=('1', '2'), show='headings', height=10, style='mystyle.Treeview')
#place the label
tview_waitlist.grid(row=1, column=0, pady=5)
#headings for the wait list window
waitlist_headings = ('NAME', 'PRIORITY')
#get selected wait list member
tview_waitlist.bind("<<TreeviewSelect>>", selected_)
#go through 2 times
for i in range(2):
    #set the properties for the tree view column
    tview_waitlist.column(str(i+1), width=columnwidths[i], anchor='w')
    #set the headings for the tree view
    tview_waitlist.heading(str(i+1), text=waitlist_headings[i], anchor='w',command=lambda column=i+1: waitlist_sort(column))
#create and set properties of the scroll bar
vscroll_waitlist = Scrollbar(tl_waitlist, orient='vertical', command=tview_waitlist.yview)
#place the scroll bar
vscroll_waitlist.grid(row=1, column=1, sticky='ns')
#create and set properties of the buttons and place them
buttonFrame = Frame(tl_waitlist, padx=5, bg='white')
buttonFrame.grid(row=2, column=0, columnspan=2)
btnUp = Button(buttonFrame, text='\u2191', padx=10, pady=2,command=up_)
btnUp.grid(row=0, column=0, pady=5, padx=2)
btnAdd = Button(buttonFrame, text='ADD', padx=10, pady=2,command=add_)
btnAdd.grid(row=0, column=1, pady=5, padx=2)
btnRemove = Button(buttonFrame, text='REMOVE', padx=10, pady=2,command=remove_)
btnRemove.grid(row=0, column=2, pady=5, padx=2)
btnDown = Button(buttonFrame, text='\u2193', padx=10, pady=2,command=down_)
btnDown.grid(row=0, column=3, pady=5, padx=2)
#run the window
root.mainloop()