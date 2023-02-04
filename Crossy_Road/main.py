#import
from tkinter import Tk, PhotoImage, Canvas, messagebox
from car_chicken import cars,Direction,chicken
import random
import pygame

#play the sound effect function
def play_sound():
    #create sound
    soundEffect=pygame.mixer.Sound("sound_effect.wav")
    #play sound
    pygame.mixer.Sound.play(soundEffect)
#function for first car
def car_function0():
    #global variables
    global timerid0,rand,gameover
    #move the car
    car.move(0)
    #if the chicken collides with the car from the vertical and horizontal 
    if chicken.getBounds()[2] >= car.getBounds(0)[0] and chicken.getBounds()[0] <= car.getBounds(0)[2]:
        if chicken.getBounds()[3] >= car.getBounds(0)[1] and chicken.getBounds()[1] <= car.getBounds(0)[3]:
            #cancel the timer
            root.after_cancel(timerid0)
            #kill the chicken
            chicken.killChicken()
            #play the sound effect
            play_sound()
            #ask yes or no question
            response=messagebox.askyesno("Game Over", "You're dead!\nWould you like to play again?")
            #if response is yes
            if response==True:
                #reset the game
                reset()
            #if the response is no 
            elif response==False:
                #show message and exit
                messagebox.showinfo("Goodbye", "Thank you for playing Crossy Road")
                exit()
    #timer for the first car       
    timerid0=canvas.after(rand[0],car_function0)
#function for the second car      
def car_function1():
    #global variables
    global timerid1,rand
    #move the car
    car.move(1)
    #if the chicken collides with the car from the vertical and horizontal 
    if chicken.getBounds()[2] >= car.getBounds(1)[0] and chicken.getBounds()[0] <= car.getBounds(1)[2]:
        if chicken.getBounds()[3] >= car.getBounds(1)[1] and chicken.getBounds()[1] <= car.getBounds(1)[3]:
            #cancel the timer
            root.after_cancel(timerid1)
            #kill the chicken
            chicken.killChicken()
            #play the sound
            play_sound()
            #ask yes or no question
            response=messagebox.askyesno("Game Over", "You're dead!\nWould you like to play again?")
            #if response is yes
            if response==True:
                #reset the game
                reset()
            #if the response is no
            elif response==False:
                #show message and exit
                messagebox.showinfo("Goodbye", "Thank you for playing Crossy Road")
                exit()
    #timer for the second car                   
    timerid1=canvas.after(rand[1],car_function1)
#function third car
def car_function2():
    #global variables
    global timerid2,rand
    #move the car
    car.move(2)
    #if the chicken collides with the car from the vertical and horizontal 
    if chicken.getBounds()[2] >= car.getBounds(2)[0] and chicken.getBounds()[0] <= car.getBounds(2)[2]:
        if chicken.getBounds()[3] >= car.getBounds(2)[1] and chicken.getBounds()[1] <= car.getBounds(2)[3]:
            #cancel the timer
            root.after_cancel(timerid2)
            #kill the chicken
            chicken.killChicken()
            #play the sound
            play_sound()
            #ask yes or no question
            response=messagebox.askyesno("Game Over", "You're dead!\nWould you like to play again?")
            #if the response is yes
            if response==True:
                #reset the game
                reset()
            #if the response is no
            elif response==False:
                #show message
                messagebox.showinfo("Goodbye", "Thank you for playing Crossy Road")
                #exit
                exit()
    #timer for the third car       
    timerid2=canvas.after(rand[2],car_function2)
#function for the 4th car
def car_function3():
    #global variables
    global timerid3,rand
    #move the car
    car.move(3)
    #if the chicken collides with the car from the vertical and horizontal 
    if chicken.getBounds()[2] >= car.getBounds(3)[0] and chicken.getBounds()[0] <= car.getBounds(3)[2]:
        if chicken.getBounds()[3] >= car.getBounds(3)[1] and chicken.getBounds()[1] <= car.getBounds(3)[3]:
            #cancel the timer
            root.after_cancel(timerid3)
            #kill the chicken
            chicken.killChicken()
            #play the sound effect
            play_sound()
            #ask yes or no question
            response=messagebox.askyesno("Game Over", "You're dead!\nWould you like to play again?")
            #if response is yes
            if response==True:
                #reset the game
                reset()
            #if the response is no 
            elif response==False:
                #show message and exit
                messagebox.showinfo("Goodbye", "Thank you for playing Crossy Road")
                exit()
    #timer for the 4th car        
    timerid3=canvas.after(rand[3],car_function3)
#function for the 5th car
def car_function4():
    #global variables
    global timerid4,rand
    #move the car
    car.move(4)
    #if the chicken collides with the car from the vertical and horizontal 
    if chicken.getBounds()[2] >= car.getBounds(4)[0] and chicken.getBounds()[0] <= car.getBounds(4)[2]:
        if chicken.getBounds()[3] >= car.getBounds(4)[1] and chicken.getBounds()[1] <= car.getBounds(4)[3]:
            #cancel the timer
            root.after_cancel(timerid4)
            #kill the chicken
            chicken.killChicken()
            #play the sound effect
            play_sound()
            #ask yes or no question
            response=messagebox.askyesno("Game Over", "You're dead!\nWould you like to play again?")
            #if response is yes
            if response==True:
                #reset the game
                reset()
            #if the response is no 
            elif response==False:
                #show message and exit
                messagebox.showinfo("Goodbye", "Thank you for playing Crossy Road")
                exit()
    #timer for the 5th car       
    timerid4=canvas.after(rand[4],car_function4)
#function for the 6th car
def car_function5():
    #global variables
    global timerid5,rand
    #move the car
    car.move(5)
    #if the chicken collides with the car from the vertical and horizontal 
    if chicken.getBounds()[2] >= car.getBounds(5)[0] and chicken.getBounds()[0] <= car.getBounds(5)[2]:
        if chicken.getBounds()[3] >= car.getBounds(5)[1] and chicken.getBounds()[1] <= car.getBounds(5)[3]:
            #cancel the timer
            root.after_cancel(timerid5)
            #kill the chicken
            chicken.killChicken()
            #play the sound effect
            play_sound()
            #ask yes or no question
            response=messagebox.askyesno("Game Over", "You're dead!\nWould you like to play again?")
            #if response is yes
            if response==True:
                #reset the game
                reset()
            #if the response is no 
            elif response==False:
                #show message and exit
                messagebox.showinfo("Goodbye", "Thank you for playing Crossy Road")
                exit()
    #timer for the 6th car       
    timerid5=canvas.after(rand[5],car_function5)
#function for the 7th car
def car_function6():
    #global variables
    global timerid6,rand
    #move the car
    car.move(6)
    #if the chicken collides with the car from the vertical and horizontal 
    if chicken.getBounds()[2] >= car.getBounds(6)[0] and chicken.getBounds()[0] <= car.getBounds(6)[2]:
        if chicken.getBounds()[3] >= car.getBounds(6)[1] and chicken.getBounds()[1] <= car.getBounds(6)[3]:
            #cancel the timer
            root.after_cancel(timerid6)
            #kill the chicken
            chicken.killChicken()
            #play the sound effect
            play_sound()
            #ask yes or no question
            response=messagebox.askyesno("Game Over", "You're dead!\nWould you like to play again?")
            #if response is yes
            if response==True:
                #reset the game
                reset()
            #if the response is no 
            elif response==False:
                #show message and exit
                messagebox.showinfo("Goodbye", "Thank you for playing Crossy Road")
                exit()
    #timer for the 7th car        
    timerid6=canvas.after(rand[6],car_function6)
#function for the 8th car
def car_function7():
    #global variables
    global timerid7,rand
    #move the car
    car.move(7)
    #if the chicken collides with the car from the vertical and horizontal 
    if chicken.getBounds()[2] >= car.getBounds(7)[0] and chicken.getBounds()[0] <= car.getBounds(7)[2]:
        if chicken.getBounds()[3] >= car.getBounds(7)[1] and chicken.getBounds()[1] <= car.getBounds(7)[3]:
            #cancel the timer
            root.after_cancel(timerid7)
            #kill the chicken
            chicken.killChicken()
            #play the sound effect
            play_sound()
            #ask yes or no question
            response=messagebox.askyesno("Game Over", "You're dead!\nWould you like to play again?")
            #if response is yes
            if response==True:
                #reset the game
                reset()
            #if the response is no 
            elif response==False:
                #show message and exit
                messagebox.showinfo("Goodbye", "Thank you for playing Crossy Road")
                exit()
    #timer for the 8th car        
    timerid7=canvas.after(rand[7],car_function7)
#function for the 9th car
def car_function8():
    #global variables
    global timerid8,rand
    #move the car
    car.move(8)
    #if the chicken collides with the car from the vertical and horizontal 
    if chicken.getBounds()[2] >= car.getBounds(8)[0] and chicken.getBounds()[0] <= car.getBounds(8)[2]:
        if chicken.getBounds()[3] >= car.getBounds(8)[1] and chicken.getBounds()[1] <= car.getBounds(8)[3]:
            #cancel the timer
            root.after_cancel(timerid8)
            #kill the chicken
            chicken.killChicken()
            #play the sound effect
            play_sound()
            #ask yes or no question
            response=messagebox.askyesno("Game Over", "You're dead!\nWould you like to play again?")
            #if response is yes
            if response==True:
                #reset the game
                reset()
            #if the response is no 
            elif response==False:
                #show message and exit
                messagebox.showinfo("Goodbye", "Thank you for playing Crossy Road")
                exit()
    #timer for the 9th car        
    timerid8=canvas.after(rand[8],car_function8)
#function for the 10th car
def car_function9():
    #global variables
    global timerid9,rand
    #move the car
    car.move(9)
    #if the chicken collides with the car from the vertical and horizontal 
    if chicken.getBounds()[2] >= car.getBounds(9)[0] and chicken.getBounds()[0] <= car.getBounds(9)[2]:
        if chicken.getBounds()[3] >= car.getBounds(9)[1] and chicken.getBounds()[1] <= car.getBounds(9)[3]:
            #cancel the timer
            root.after_cancel(timerid0)
            #kill the chicken
            chicken.killChicken()
            #play the sound effect
            play_sound()
            #ask yes or no question
            response=messagebox.askyesno("Game Over", "You're dead!\nWould you like to play again?")
            #if response is yes
            if response==True:
                #reset the game
                reset()
            #if the response is no 
            elif response==False:
                #show message and exit
                messagebox.showinfo("Goodbye", "Thank you for playing Crossy Road")
                exit()
    #timer for the 10th car        
    timerid9=canvas.after(rand[9],car_function9)
#function for the 11th car
def car_function10():
    #global variables
    global timerid10,rand
    #move the car
    car.move(10)
    #if the chicken collides with the car from the vertical and horizontal 
    if chicken.getBounds()[2] >= car.getBounds(10)[0] and chicken.getBounds()[0] <= car.getBounds(10)[2]:
        if chicken.getBounds()[3] >= car.getBounds(10)[1] and chicken.getBounds()[1] <= car.getBounds(10)[3]:
            #cancel the timer
            root.after_cancel(timerid10)
            #kill the chicken
            chicken.killChicken()
            #play the sound effect
            play_sound()
            #ask yes or no question
            response=messagebox.askyesno("Game Over", "You're dead!\nWould you like to play again?")
            #if response is yes
            if response==True:
                #reset the game
                reset()
            #if the response is no 
            elif response==False:
                #show message and exit
                messagebox.showinfo("Goodbye", "Thank you for playing Crossy Road")
                exit()
    #timer for the 11th car        
    timerid10=canvas.after(rand[10],car_function10)
#function for the 12th car
def car_function11():
    #global variables
    global timerid11,rand
    #move the car
    car.move(11)
    #if the chicken collides with the car from the vertical and horizontal 
    if chicken.getBounds()[2] >= car.getBounds(11)[0] and chicken.getBounds()[0] <= car.getBounds(11)[2]:
        if chicken.getBounds()[3] >= car.getBounds(11)[1] and chicken.getBounds()[1] <= car.getBounds(11)[3]:
            #cancel the timer
            root.after_cancel(timerid11)
            #kill the chicken
            chicken.killChicken()
            #play the sound effect
            play_sound()
            #ask yes or no question
            response=messagebox.askyesno("Game Over", "You're dead!\nWould you like to play again?")
            #if response is yes
            if response==True:
                #reset the game
                reset()
            #if the response is no 
            elif response==False:
                #show message and exit
                messagebox.showinfo("Goodbye", "Thank you for playing Crossy Road")
                exit()
    #timer for the 12th car        
    timerid11=canvas.after(rand[11],car_function11)
#function for the 13th car
def car_function12():
    #global variables
    global timerid12,rand
    #move the car
    car.move(12)
    #if the chicken collides with the car from the vertical and horizontal 
    if chicken.getBounds()[2] >= car.getBounds(12)[0] and chicken.getBounds()[0] <= car.getBounds(12)[2]:
        if chicken.getBounds()[3] >= car.getBounds(12)[1] and chicken.getBounds()[1] <= car.getBounds(12)[3]:
            #cancel the timer
            root.after_cancel(timerid12)
            #kill the chicken
            chicken.killChicken()
            #play the sound effect
            play_sound()
            #ask yes or no question
            response=messagebox.askyesno("Game Over", "You're dead!\nWould you like to play again?")
            #if response is yes
            if response==True:
                #reset the game
                reset()
            #if the response is no 
            elif response==False:
                #show message and exit
                messagebox.showinfo("Goodbye", "Thank you for playing Crossy Road")
                exit()
    #timer for the 13th car        
    timerid12=canvas.after(rand[12],car_function12)
#if key is pressed
def onkeypress(event):
    #global variables
    global score_output,score,index,gameover,level,rand
    #if the key is s or down button
    if event.char == 's' or event.keysym == 'Down':
        #subtract 1 from the index
        index-=1
        #if on the road after the grass
        if chicken.getY()==485 or chicken.getY()==165 or (level>1 and chicken.getY()==645):
            #add 1 to the score
            score+=1
        #subtract 1 if not on the starting position
        if chicken.getX()!=685:
            score-=1
        #if index is -1
        if index==-1:
            #set scor and index to 0
            index=0
            score=0
        #move the chicken down
        chicken.movedown(i=index)
        #if the score is not -1
        if score!=-1:
            #output the score
            canvas.itemconfig(score_output, text='{:<10s}{:d}'.format('SCORE:', score))  
    #if the key is w or up key
    if event.char == "w" or event.keysym == "Up":
        #add 1 to the index
        index+=1
        #move the chicken up
        chicken.moveup(i=index) 
        #if on the road after the grass
        if chicken.getY()==485 or chicken.getY()==165 or (level>1 and chicken.getY()==645):
            #subtract 1 from the score
            score-=1
        #add 1 to the score if not in starting position
        if chicken.getX()!=685:
            score+=1
        #output the score
        canvas.itemconfig(score_output, text='{:<10s}{:d}'.format('SCORE:', score))  
        #y pos =45
        if chicken.getY()==45:
            #reset the chicken
            chicken.reset()
            #show message 
            messagebox.showinfo("Crossy Road", "Congratulations! You completed Level "+str(level)+"\nGet ready for Level "+str(level+1))
            #increase the level by 1
            level+=1
            #output the level
            canvas.itemconfig(level_output,text='{:<10s}{:d}'.format('LEVEL:', level))
            #set index to 0
            index=0
            #go through 13 times
            for i in range(13):
                #decrease the timer values by 100
                rand[i]-=100
                #if the timer is less than or = to 0
                if rand[i]<=0:
                    #set it to 1
                    rand[i]=1
#reset function
def reset():
    #global variables
    global rand,score,level,index
    #output the score
    canvas.itemconfig(score_output,text='{:<10s}{:d}'.format('SCORE:', 0))
    #set the score to -1
    score=-1
    #reset the level
    level=1
    #output the level
    canvas.itemconfig(level_output,text='{:<10s}{:d}'.format('LEVEL:', level))
    #set index to 0
    index=0
    #reset the cars and the chicken
    car.reset()
    chicken.reset()
    #reset timer list
    rand=[]
    #go through 13 times
    for i in range(13):
        #add the rand int to the list
        rand.append(random.randint(300,600))
    #call the car functions
    car_function0()
    car_function1()
    car_function2()
    car_function3()
    car_function4()
    car_function5()
    car_function6()
    car_function7()
    car_function8()
    car_function9()
    car_function10()
    car_function11()
    car_function12()
    #call the press function
    root.bind('<KeyPress>', onkeypress)
#close function
def close_button():
    #output message
    response=messagebox.askyesno("Exit", "Are you sure you want to exit!")
    #if response is yes
    if response == True:
        #output messageand exit
        messagebox.showinfo("Goodbye", "Thank you for playing Crossy Road!")
        exit()
#set variable, lists ,tuples
score, level = -1, 1
tree_coords = ((65, 145), (320, 145), (600, 145), (20, 465), (120, 465), (350, 465))
tree_list = []
rand=[]
index=0
#create root
root = Tk()
#set title of the window
root.title('Crossy Road')
#call the close button function
root.protocol('WM_DELETE_WINDOW',close_button)
#set background image
imgBackground = PhotoImage(file='sprites/main_screen_final.png')
#set the tree image
imgTree = PhotoImage(file='sprites/tree.png')
#set the window to the center
root.geometry("%dx%d+%d+%d" % (imgBackground.width(), imgBackground.height(), root.winfo_screenwidth() // 2 - imgBackground.width() // 2,
    root.winfo_screenheight() // 2 - imgBackground.height() // 2))
#create and set properties of the canvas
canvas = Canvas(root, width=imgBackground.width(), height=imgBackground.height())
#place the canvas
canvas.pack()
#create image on the canvas
canvas.create_image(0, 0, image=imgBackground, anchor='nw')
#set the sound for the background
pygame.mixer.init()
#selct file
pygame.mixer.music.load("Busy_Traffic_Sound_Effects.wav")
#play the sound
pygame.mixer.music.play()
#create and set properties of the score and label text
score_output = canvas.create_text(canvas.winfo_reqwidth() - 160, canvas.winfo_reqheight() - 40, text='{:<10s}{:d}'.format('SCORE:', 0), font=('Britannic Bold', 18), fill='#565656', anchor='w')
level_output = canvas.create_text(20, canvas.winfo_reqheight() - 40, text='{:<10s}{:d}'.format('LEVEL:', level), font=('Britannic Bold', 18), fill='#565656', anchor='w')
#call the chicken and cars class
chicken=chicken(canvas)
chicken.placeImage()
car=cars(canvas)
#place all 13 of the cars
for i in range(13):
    car.placeImage(i)
#create 13 randomtimer values for the cars
for i in range(13):
    rand.append(random.randint(300,600))
#call the car functions
car_function0()
car_function1()
car_function2()
car_function3()
car_function4()
car_function5()
car_function6()
car_function7()
car_function8()
car_function9()
car_function10()
car_function11()
car_function12()
#output the trees 6 times
for i in range(6):
    canvas.create_image(tree_coords[i][0], tree_coords[i][1], image=imgTree, anchor='nw')
#check for any key clicks
root.bind('<KeyPress>', onkeypress)
#run the window
root.mainloop()