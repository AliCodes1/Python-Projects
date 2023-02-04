from tkinter import Tk,Frame,Label,IntVar,LabelFrame,Button,messagebox,END,PhotoImage,font,Radiobutton,Checkbutton,BooleanVar
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter.constants import DISABLED, NORMAL
'''
Name: Muhammad Ali
Date: Friday, September 24th, 2021 
Course Code: ICS4U1-01
Program: Rogers Wireless
'''

#-------------------------------------- functions
#this function outputs the phone
def show_phone():
    #globalize variables
    global phone_img,phone_colour
    #if red phone is chosen
    if var_phone.get()==0:
        #get the image resize it and then output 
        phone_img=PhotoImage(file=img_file[0])
        phone_img=phone_img.subsample(6)
        phone_lbl=Label(frame,image=phone_img)
        phone_lbl.grid(row=0,rowspan=4)
        #variable for phone color
        phone_colour="Red"
    #if blue phone is chosen
    if var_phone.get()==1:
        #get the image resize it and then output 
        phone_img=PhotoImage(file=img_file[1])
        phone_img=phone_img.subsample(6)
        phone_lbl=Label(frame,image=phone_img)
        phone_lbl.grid(row=0,rowspan=4)
        #variable for phone color
        phone_colour="Blue"
    #if white phone is chosen
    if var_phone.get()==2:
        #get the image resize it and then output 
        phone_img=PhotoImage(file=img_file[2])
        phone_img=phone_img.subsample(6)
        phone_lbl=Label(frame,image=phone_img)
        phone_lbl.grid(row=0,rowspan=4) 
        #variable for phone color
        phone_colour="White"
    #if black phone is chosen
    if var_phone.get()==3:
        #get the image resize it and then output 
        phone_img=PhotoImage(file=img_file[3])
        phone_img=phone_img.subsample(6)
        phone_lbl=Label(frame,image=phone_img)
        phone_lbl.grid(row=0,rowspan=4)
        #variable for phone color
        phone_colour="Black"

#when the 64 gb button is clicked
def _64gb():
    #globalize variables
    global price_,amount_gb
    #set the the states to normal
    btn_128.config(state=NORMAL)
    btn_256.config(state=NORMAL)
    btn_512.config(state=NORMAL)
    #disable the state of the button    
    btn_64.config(state=DISABLED)
    #price of the phone
    price_=1379.99
    #output the price
    phone_price.config(text="$"+"{:.2f}".format(price_))
    #storage of the phone
    amount_gb="64 GB"
#when the 128 gb button is clicked
def _128gb():
    #globalize variables
    global price_,amount_gb
    #set the the states to normal
    btn_64.config(state=NORMAL)
    btn_256.config(state=NORMAL)
    btn_512.config(state=NORMAL)
    #disable the state of the button    
    btn_128.config(state=DISABLED)
    #price of the phone
    price_=1589.99
    #output the price
    phone_price.config(text="$"+"{:.2f}".format(price_))
    #storage of the phone
    amount_gb="128 GB"
#when the 256 gb button is clicked
def _256gb():
    #globalize variables
    global price_,amount_gb
    #set the the states to normal
    btn_128.config(state=NORMAL)
    btn_64.config(state=NORMAL)
    btn_512.config(state=NORMAL)
    #disable the state of the button        
    btn_256.config(state=DISABLED)
    #price of the phone
    price_=1799.00
    #output the price
    phone_price.config(text="$"+"{:.2f}".format(price_))
    #storage of the phone
    amount_gb="256 GB"
#when the 512 gb button is clicked
def _512gb():
    global price_,amount_gb
    #set the the states to normal
    btn_128.config(state=NORMAL)
    btn_256.config(state=NORMAL)
    btn_64.config(state=NORMAL)
    #disable the state of the button        
    btn_512.config(state=DISABLED)
    #price of the phone
    price_=1999.99
    #output the price
    phone_price.config(text="$"+"{:.2f}".format(price_))
    #storage of the phone
    amount_gb="512 GB"
#if the first app is clicked
def check_app1():
    #globalize variable
    global numclick,price_app,name_app
    #numclick sees how many times the button was clicked 
    numclick+=1
    #if the checkbutton is selected and numclick is 2
    if check_btn1.get()==True and numclick>2:
        #add 2.99 to the price
        price_app+=2.99
        #output the price
        app_price.config(text="$"+"{:.2f}".format(price_app))
    #if the checkbutton is selected
    if check_btn1.get()==True: 
        #put the name of the app in a list  
        name_app[0]="- Plants vs Zombies"
    #if the button is deselected
    if check_btn1.get()==False:
        #and this is true
        if numclick==2 or numclick==3:
            #make the price =0
            price_app=0.00
            #output price
            app_price.config(text="$"+"{:.2f}".format(price_app))
            #numclick -2 
            numclick-=2
            #set the name to ""
            name_app[0]=""
        #anything else
        else:
            #subtract 2.99
            price_app-=2.99
            #numclick -2 
            numclick-=2
            #output price
            app_price.config(text="$"+"{:.2f}".format(price_app))
            #set the name to ""
            name_app[0]=""


        
#check the second app
def check_app2():
    #globalize variables
    global numclick,price_app,name_app
    #add 1 to numclcick
    numclick+=1
    #check if button 2 is selected and numclcick is less than 2
    if check_btn2.get()==True and numclick>2:
        #add 2.99 to the price
        price_app+=2.99
        #output the price
        app_price.config(text="$"+"{:.2f}".format(price_app))
    #if the button is selected
    if check_btn2.get()==True:  
        #put the name of the app in a list         
        name_app[1]="- Where's My Water?"
    #if it is not selected 
    if check_btn2.get()==False:
        #and numclick ==2 or 3
        if numclick==2 or numclick==3:
            #set price to 0
            price_app=0.00
            #ouput the price
            app_price.config(text="$"+"{:.2f}".format(price_app))
            #subtract 2 from numclick
            numclick-=2
            #set name of app=""
            name_app[1]=""
        # anything else
        else:
            #subtract 2.99 from the price
            price_app-=2.99
            #output the price
            app_price.config(text="$"+"{:.2f}".format(price_app))
            #subtract 2 from numclick
            numclick-=2
            #set name of app=""
            name_app[1]=""
#if app 3 is selected
def check_app3():
    #globalize variables
    global numclick,price_app,name_app
    #add 1 to numclick
    numclick+=1
    #check if button 2 is selected and numclcick is less than 2

    if check_btn3.get()==True and numclick>2:
        #add 2.99 to the price
        price_app+=2.99
        #output the price
        app_price.config(text="$"+"{:.2f}".format(price_app))
    #if the checkbutton is selected
    if check_btn3.get()==True:   
        #put the name of the app in a list     
        name_app[2]="- Fruit Ninja"
    #if it is not selected 
    if check_btn3.get()==False:
        #and numclick ==2 or 3
        if numclick==2 or numclick==3:
            #set price to 0
            price_app=0.00
            #output the price
            app_price.config(text="$"+"{:.2f}".format(price_app))
            #subtract 2 from numclick
            numclick-=2
            #set name of app=""
            name_app[2]=""
        # anything else
        else:
            price_app-=2.99
            #output the price
            app_price.config(text="$"+"{:.2f}".format(price_app))
            numclick-=2
            name_app[2]=""
#check the 4th app
def check_app4():
    global numclick,price_app,name_app
    numclick+=1
    #check if button 2 is selected and numclcick is less than 2

    if check_btn4.get()==True and numclick>2:
        #add 2.99 to the price
        price_app+=2.99
        #output the price
        app_price.config(text="$"+"{:.2f}".format(price_app))
    #if the checkbutton is selected
    if check_btn4.get()==True:   
        #put the name of the app in a list       
        name_app[3]="- Bejeweled Blitz"
    #if it is not selected 
    if check_btn4.get()==False:
        #and numclick ==2 or 3
        if numclick==2 or numclick==3:
            #set price to 0
            price_app=0.00
            #output the price
            app_price.config(text="$"+"{:.2f}".format(price_app))
            #subtract 2 from numclick
            numclick-=2
            #set name of app=""
            name_app[3]=""
        # anything else
        else:
            price_app-=2.99
            #output the price
            app_price.config(text="$"+"{:.2f}".format(price_app))
            #subtract 2 from numclick
            numclick-=2
            #set name of app=""
            name_app[3]=""
#check the 5th app
def check_app5():
    global numclick,price_app,name_app
    numclick+=1
    #check if button 2 is selected and numclcick is less than 2

    if check_btn5.get()==True and numclick>2:
        #add 2.99 to the price
        price_app+=2.99
        #output the price
        app_price.config(text="$"+"{:.2f}".format(price_app))
    #if the checkbutton is selected
    if check_btn5.get()==True:    
        #put the name of the app in a list      
        name_app[4]="- Subway Surfers"
    #if it is not selected 
    if check_btn5.get()==False:
        #and numclick ==2 or 3
        if numclick==2 or numclick==3:
            #set price to 0
            price_app=0.00
            #output the price
            app_price.config(text="$"+"{:.2f}".format(price_app))
            #subtract 2 from numclick
            numclick-=2
            #set name of app=""
            name_app[4]=""
        # anything else
        else:
            price_app-=2.99
            #output the price
            app_price.config(text="$"+"{:.2f}".format(price_app))
            #subtract 2 from numclick
            numclick-=2
            #set name of app=""
            name_app[4]=""

#check the 6th app
def check_app6():
    global numclick,price_app,name_app
    numclick+=1
    #check if button 2 is selected and numclcick is less than 2

    if check_btn6.get()==True and numclick>2:
        #add 2.99 to the price
        price_app+=2.99
        #output the price
        app_price.config(text="$"+"{:.2f}".format(price_app))
    #if the checkbutton is selected
    if check_btn6.get()==True:
        #put the name of the app in a list  
        name_app[5]="- Cut the Rope"
    #if it is not selected 
    if check_btn6.get()==False:
        #and numclick ==2 or 3
        if numclick==2 or numclick==3:
            #set price to 0
            price_app=0.00
            #output the price
            app_price.config(text="$"+"{:.2f}".format(price_app))
            #subtract 2 from numclick
            numclick-=2
            #set name of app=""
            name_app[5]=""
        # anything else
        else:
            price_app-=2.99
            #output the price
            app_price.config(text="$"+"{:.2f}".format(price_app))
            #subtract 2 from numclick
            numclick-=2
            #set name of app=""
            name_app[5]=""
#check the 7th app
def check_app7():
    global numclick,price_app,name_app
    numclick+=1
    #check if button 2 is selected and numclcick is less than 2

    if check_btn7.get()==True and numclick>2:
        #add 2.99 to the price
        price_app+=2.99
        #output the price
        app_price.config(text="$"+"{:.2f}".format(price_app))
    #if the checkbutton is selected
    if check_btn7.get()==True:
        #put the name of the app in a list  
        name_app[6]="- Temple Run"
    #if it is not selected 
    if check_btn7.get()==False:
        #and numclick ==2 or 3
        if numclick==2 or numclick==3:
            #set price to 0
            price_app=0.00
            #output the price
            app_price.config(text="$"+"{:.2f}".format(price_app))
            #subtract 2 from numclick
            numclick-=2
            #set name of app=""
            name_app[6]=""
        # anything else
        else:
            price_app-=2.99
            #output the price
            app_price.config(text="$"+"{:.2f}".format(price_app))
            #subtract 2 from numclick
            numclick-=2
            #set name of app=""
            name_app[6]=""

#check the 8th app
def check_app8():
    global numclick,price_app,name_app
    numclick+=1
    #check if button 2 is selected and numclcick is less than 2

    if check_btn8.get()==True and numclick>2:
        #add 2.99 to the price
        price_app+=2.99
        #output the price
        app_price.config(text="$"+"{:.2f}".format(price_app))
    #if the checkbutton is selected
    if check_btn8.get()==True:    
        #put the name of the app in a list      
        name_app[7]="- Jetpack Joyride"
    #if it is not selected 
    if check_btn8.get()==False:
        #and numclick ==2 or 3
        if numclick==2 or numclick==3:
            #set price to 0
            price_app=0.00
            #output the price
            app_price.config(text="$"+"{:.2f}".format(price_app))
            #subtract 2 from numclick
            numclick-=2
            #set name of app=""
            name_app[7]=""
        # anything else
        else:
            price_app-=2.99
            #output the price
            app_price.config(text="$"+"{:.2f}".format(price_app))
            #subtract 2 from numclick
            numclick-=2
            #set name of app=""
            name_app[7]=""
#check the 9th app
def check_app9():
    global numclick,price_app,name_app
    numclick+=1
    #check if button 2 is selected and numclcick is less than 2

    if check_btn9.get()==True and numclick>2:
        #add 2.99 to the price
        price_app+=2.99
        #output the price
        app_price.config(text="$"+"{:.2f}".format(price_app))
    #if the checkbutton is selected
    if check_btn9.get()==True:  
        #put the name of the app in a list  
        name_app[8]="- Joe Danger"
    #if it is not selected 
    if check_btn9.get()==False:
        #and numclick ==2 or 3
        if numclick==2 or numclick==3:
            #set price to 0
            price_app=0.00
            #output the price
            app_price.config(text="$"+"{:.2f}".format(price_app))
            #subtract 2 from numclick
            numclick-=2
            #set name of app=""
            name_app[8]=""
        # anything else
        else:
            price_app-=2.99
            #output the price
            app_price.config(text="$"+"{:.2f}".format(price_app))
            #subtract 2 from numclick
            numclick-=2
            #set name of app=""
            name_app[8]=""

#check the 10th app
def check_app10():
    global numclick,price_app,name_app
    numclick+=1
    #check if button 2 is selected and numclcick is less than 2

    if check_btn10.get()==True and numclick>2:
        #add 2.99 to the price
        price_app+=2.99
        #output the price
        app_price.config(text="$"+"{:.2f}".format(price_app))
    #if the checkbutton is selected
    if check_btn10.get()==True:
        #put the name of the app in a list  
        name_app[9]="- Bad Piggies"
    #if it is not selected 
    if check_btn10.get()==False:
        #and numclick ==2 or 3
        if numclick==2 or numclick==3:
            #set price to 0
            price_app=0.00
            #output the price
            app_price.config(text="$"+"{:.2f}".format(price_app))
            #subtract 2 from numclick
            numclick-=2
            #set name of app=""
            name_app[9]=""
        # anything else
        else:
            price_app-=2.99
            #output the price
            app_price.config(text="$"+"{:.2f}".format(price_app))
            #subtract 2 from numclick
            numclick-=2
            #set name of app=""
            name_app[9]=""

#check the 11th app
def check_app11():
    global numclick, price_app,name_app
    numclick+=1
    #check if button 2 is selected and numclcick is less than 2

    if check_btn11.get()==True and numclick>2:
        #add 2.99 to the price
        price_app+=2.99
        #output the price
        app_price.config(text="$"+"{:.2f}".format(price_app))
    #if the checkbutton is selected
    if check_btn11.get()==True:
        #put the name of the app in a list  
        name_app[10]="- Clash of Clans"
    #if it is not selected 
    if check_btn11.get()==False:
        #and numclick ==2 or 3
        if numclick==2 or numclick==3:
            #set price to 0
            price_app=0.00
            #output the price
            app_price.config(text="$"+"{:.2f}".format(price_app))
            #subtract 2 from numclick
            numclick-=2
            #set name of app=""
            name_app[10]=""
        # anything else
        else:
            price_app-=2.99
            #output the price
            app_price.config(text="$"+"{:.2f}".format(price_app))
            #subtract 2 from numclick
            numclick-=2
            #set name of app=""
            name_app[10]=""
#check the 12th app
def check_app12():
    global numclick,price_app,name_app
    
    numclick+=1
    #check if button 2 is selected and numclcick is less than 2
    if check_btn12.get()==True and numclick>2:
        #add 2.99 to the price
        price_app+=2.99
        #output the price
        app_price.config(text="$"+"{:.2f}".format(price_app))
    #if the checkbutton is selected
    if check_btn12.get()==True:
        #put the name of the app in a list  
        name_app[11]="- SPY Mouse"
    #if it is not selected 
    if check_btn12.get()==False:
        #and numclick ==2 or 3
        if numclick==2 or numclick==3:
            #set price to 0
            price_app=0.00
            #output the price
            app_price.config(text="$"+"{:.2f}".format(price_app))
            #subtract 2 from numclick
            numclick-=2
            #set name of app=""
            name_app[11]=""

        # anything else     
        else:
            price_app-=2.99
            #output the price
            app_price.config(text="$"+"{:.2f}".format(price_app))
            #subtract 2 from numclick
            numclick-=2
            #set name of app=""
            name_app[11]=""

#if data is selected from combobox
def price_data(event):
    #globalize variables
    global monthly_price,price_mins,price_canada
    global price_inter,data_price,data_plan_recipt,cbo
    #if 1st combobox is selected
    if cbo.current()==0:
        #price of data
        data_price=0
        #output price
        d_plan.config(text="{:.2f}".format(data_price))
        #amount of data
        data_plan_recipt="0 GB"
    #if 2nd combobox is selected   
    if cbo.current()==1:
        #price of data
        data_price=10
        #output price
        d_plan.config(text="{:.2f}".format(data_price))
        #amount of data
        data_plan_recipt="1 GB"
    #if 3rd combobox is selected
    if cbo.current()==2:
        #price of data
        data_price=20
        #output price
        d_plan.config(text="{:.2f}".format(data_price))
        #amount of data
        data_plan_recipt="2 GB"
    #if 4th combobox is selected
    if cbo.current()==3:
        #price of data
        data_price=30
        #output price
        d_plan.config(text="{:.2f}".format(data_price))
        #amount of data
        data_plan_recipt="5 GB"
    #if 5th combobox is selected
    if cbo.current()==4:
        #price of data
        data_price=60
        #output price
        d_plan.config(text="{:.2f}".format(data_price))
        #amount of data
        data_plan_recipt="10 GB"

    if cbo.current()==5:
        #price of data
        data_price=80
        #output price
        d_plan.config(text="{:.2f}".format(data_price))
        #amount of data
        data_plan_recipt="UNLIMITED"
    #output total monthly cost
    monthly_price.config(text="$"+"{:.2f}".format(data_price+price_mins+price_canada+price_inter))

#if local mins are selected 
def price_mins_local(event2):
    #globalize variables
    global monthly_price,price_canada
    global price_inter,data_price,price_mins,lmins_recipt,cbo1
    #if 1st combobox is selected
    if cbo1.current()==0:
        #price for the mins
        price_mins=0
        #output the price
        l_min.config(text="{:.2f}".format(price_mins))
        #amount of mins
        lmins_recipt="0"
    #if 2nd combobox is selected
    if cbo1.current()==1:
        #price for the mins
        price_mins=20
        #output the price
        l_min.config(text="{:.2f}".format(price_mins))
        #amount of mins
        lmins_recipt="250"
    #if 3rd combobox is selected
    if cbo1.current()==2:
        #price for the mins
        price_mins=30
        #output the price
        l_min.config(text="{:.2f}".format(price_mins))
        #amount of mins
        lmins_recipt="1000"
    #if 4th combobox is selected
    if cbo1.current()==3:
        #price for the mins
        price_mins=40
        #output the price
        l_min.config(text="{:.2f}".format(price_mins))
        #amount of mins
        lmins_recipt="UNLIMITED"
    #total monthly cost
    monthly_price.config(text="$"+"{:.2f}".format(data_price+price_mins+price_canada+price_inter))
#if canada mins is selected
def price_mins_canada(event3):
    #globalize variables
    global monthly_price,price_mins,price_inter
    global data_price,price_canada,cmins_recipt,cbo2
    #if 1st combobox is selected
    if cbo2.current()==0:
        #price for the mins
        price_canada=0
        #output price
        c_min.config(text="{:.2f}".format(price_canada))
        #amount of mins
        cmins_recipt="0"
    #if 2nd combobox is selected
    if cbo2.current()==1:
        #price for the mins
        price_canada=10
        #output price
        c_min.config(text="{:.2f}".format(price_canada))
        #amount of mins
        cmins_recipt="250"
    #if 3rd combobox is selected
    if cbo2.current()==2:
        #price for the mins
        price_canada=20
        #output price
        c_min.config(text="{:.2f}".format(price_canada))
        #amount of mins
        cmins_recipt="1000"
    #if 4th combobox is selected
    if cbo2.current()==3:
        #price for the mins
        price_canada=30
        #output price
        c_min.config(text="{:.2f}".format(price_canada))
        #amount of mins
        cmins_recipt="UNLIMITED"
    #monthly total
    monthly_price.config(text="$"+"{:.2f}".format(data_price+price_mins+price_canada+price_inter))
#if international mins is selected  
def price_inter_mins(event4):
    #globalize variables 
    global monthly_price,price_mins
    global price_canada,data_price,price_inter,imins_recipt,cbo3
    #if 1st combobox is selected
    if cbo3.current()==0:
        #price for the mins
        price_inter=0
        #output price
        i_min.config(text="{:.2f}".format(price_inter))
        #amount of mins
        imins_recipt="0"
    #if 2nd combobox is selected
    if cbo3.current()==1:
        #price for the mins
        price_inter=10
        #output price
        i_min.config(text="{:.2f}".format(price_inter))
        #amount of mins
        imins_recipt="250"
    #if 3rd combobox is selected
    if cbo3.current()==2:
        #price for the mins
        price_inter=20
        #output price
        i_min.config(text="{:.2f}".format(price_inter))
        #amount of mins
        imins_recipt="1000"
    #if 4th combobox is selected
    if cbo3.current()==3:
        #price for the mins
        price_inter=30
        #output price
        i_min.config(text="{:.2f}".format(price_inter))
        #amount of mins
        imins_recipt="UNLIMITED"
    #monthly total
    monthly_price.config(text="$"+"{:.2f}".format(data_price+price_mins+price_canada+price_inter))

#create function to close the window or exit with the exit button
def close_button():
    #Ask the user if they want to exit
    users_response = messagebox.askyesno('Rogers Wireless', 'Are you sure you want to exit?')
    #if they do want to exit 
    if users_response == True:
        messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers!")
        #exit from the program
        exit()
#if calculate is clicked
def total_calc():
    #gloablize variables
    global hst,grand_total
    #if the phone price is 0
    if price_==0:
        #disable the checkout button
        checkout_btn.config(state=DISABLED)
    #if it is not
    if price_!=0:
        #set the state to normal
        checkout_btn.config(state=NORMAL)
    #total of the apps, monthly cost, and phone
    total="{:.2f}".format(data_price+price_mins+price_canada+price_inter+price_app+price_)
    #output the subtotal
    subtotal_borderlbl.config(text="{:^25s}".format("$"+total))
    #take monthly cost and multiply by 24 
    discount_total="{:.2f}".format((data_price+price_mins+price_canada+price_inter)*24)
    #if discount is equalor larger than the phone price
    if float(discount_total)>=float(price_):
        #set the discount to the phone price
        discount_total=price_
        #hst is total - discount *0.13
        hst=(float(total)-float(discount_total))*0.13
        #grand total is total-discount+hst
        grand_total=float(float(total)-float(discount_total)+float(hst))    
        #output hst
        hst_borderlabel.config(text="{:^25s}".format("$"+"{:^.2f}".format(hst)))
        #if there is no discount
        if discount_total=="0.00":
            #output the $0.00
            discount_borderlbl.config(text="{:^25s}".format("$"+"{:^s}".format(discount_total)))
        #if there is a discount
        if discount_total>0.00:
            #output the discount and set properties
            discount_borderlbl.config(text="{:^25s}".format("-($"+"{:^.2f}".format(discount_total)+")"),bg="green",fg="white")
        #output and format the grand total
        grand_total_borderlabel.config(text="{:^25s}".format("$"+"{:^.2f}".format(grand_total)))
    #if discount is leass the phone price
    if float(discount_total)<float(price_):
        #find the hst
        hst=(float(total)-float(discount_total))*0.13
        #get the grand total
        grand_total=float(float(total)-float(discount_total)+float(hst))    
        #output the hst
        hst_borderlabel.config(text="{:^25s}".format("$"+"{:^.2f}".format(hst)))
        #if there is no discount
        if discount_total=="0.00":
            #output the $0.00
            discount_borderlbl.config(text="{:^25s}".format("$"+"{:^s}".format(discount_total)))
        #if there is a discount
        if discount_total>"0.00":
            #output the discount and set properties
            discount_borderlbl.config(text="{:^25s}".format("-($"+"{:^s}".format(discount_total)+")"),bg="green",fg="white")
        #output rhe grand total
        grand_total_borderlabel.config(text="{:^25s}".format("$"+"{:^.2f}".format(grand_total)))


#if user clicks checkout
def checkout_():
    #globalize variables
    global phone_colour,amount_gb,name_app,numclick,grand_total
    global lmins_recipt,cmins_recipt,imins_recipt,data_plan_recipt
    #create variables
    #apps list
    apps=[]
    #phone recipt output
    response_phone="---------------------------------------"+"\n"+"PHONE:"+"\n"+"iphone, "+phone_colour+", "+amount_gb+"\n"
    #apps output
    respone_apps="\n"+"APPS:"+"\n"
    #recipt variable for monthly plan
    month_plan="---------------------------------------"+"\n"+"MONTHLY PLAN:"+"\n"
    #recipt variable for data plan
    data_plan="Data:"+"\t\t\t\t\t"+str(data_plan_recipt)+"\n"
    #recipt variable for local mins
    local_recipt="Local (mins):"+"\t\t\t\t"+str(lmins_recipt)+"\n"
    #recipt variable for canada mins
    canada_recipt="Canada (mins):"+"\t\t\t"+str(cmins_recipt)+"\n"
    #recipt variable for international mins
    inter_recipt="International (mins):"+"\t\t"+str(imins_recipt)+"\n"
    #recipt variable for total
    total_recipt="---------------------------------------"+"\n"+"TOTAL:"+"\t\t\t\t\t"+"$"+"{:.2f}".format(grand_total)
    line_="---------------------------------------"
    #add apps to the variable
    for x in name_app:
        if x!="": 
            apps.append(x)
    output=""
    #add the apps to the strong
    for index in apps:
        output+=index+"\n"
    
    #if no apps are selected
    if numclick<1: 
        #and no data is selected 
        if data_plan_recipt=='0 GB':
            #and no local mins are selected 
            if lmins_recipt=="0":
                #and no canada mins are selected 
                if cmins_recipt=="0":
                    #and no international mins are selected 
                    if imins_recipt=="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+total_recipt)
                        #if user hit yes
                        if message_var==True:
                            #output message
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")
                            #exit
                            exit()
                    #if international mins are selected 
                    if imins_recipt!="0":
                        #output this message
                        message_var=messagebox.askyesno("Order Summary",response_phone+month_plan+inter_recipt+total_recipt)
                        #if user hits yes
                        if message_var==True:
                            #output message
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")
                            #exit
                            exit()
                #if canada mins are selected 
                if cmins_recipt!="0":
                    #if international mins are not selected 
                    if imins_recipt=="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+month_plan+canada_recipt+total_recipt)
                        #if user hits yes
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")
                            exit()
                    #if international mins are selected 
                    if imins_recipt!="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+month_plan+canada_recipt+inter_recipt+total_recipt)
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")
                            #EXIT
                            exit()
            #if local mins are selected    
            if lmins_recipt!="0":
                #if canada mins are not selected 
                if cmins_recipt=="0":
                    #if international mins are not selected 
                    if imins_recipt=="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+month_plan+local_recipt+total_recipt)
                        #if user hits yes
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")
                            exit()
                    #if international mins are selected                             
                    if imins_recipt!="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+month_plan+local_recipt+inter_recipt+total_recipt)
                        #if user hits yes
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")
                            exit()
                #if canada mins are selected 
                if cmins_recipt!="0":
                    #if international mins are not selected 
                    if imins_recipt=="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+month_plan+local_recipt+canada_recipt+total_recipt)
                        #if user hits yes
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")
                            exit()
                    #if international mins are selected 
                    if imins_recipt!="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+month_plan+local_recipt+canada_recipt+inter_recipt+total_recipt)
                        #if user hits yes
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")
                            exit()
        #if data is selected  
        if data_plan_recipt!='0 GB':
            #if local mins are not selected 
            if lmins_recipt=="0":
                #if canada mins are not selected 
                if cmins_recipt=="0":
                    #if international mins are not selected 
                    if imins_recipt=="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+month_plan+data_plan+total_recipt)
                        #if user hits yes
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")
                            exit()
                    #if local mins are selected 
                    if imins_recipt!="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+month_plan+data_plan+inter_recipt+total_recipt)
                        #if user hits yes
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")    
                            exit()
                #if canada mins are selected 
                if cmins_recipt!="0":
                    #if international mins are not selected 
                    if imins_recipt=="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+month_plan+data_plan+canada_recipt+total_recipt)
                        #if user hits yes
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")  
                            exit()
                    #if international mins are selected 
                    if imins_recipt!="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+month_plan+data_plan+canada_recipt+inter_recipt+total_recipt)
                        #if user hits yes
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")
                            exit()
            #if local mins are selected 
            if lmins_recipt!="0":
                #if canada mins are not selected 
                if cmins_recipt=="0":
                    #if international mins are not selected 
                    if imins_recipt=="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+month_plan+data_plan+local_recipt+total_recipt)
                        #if user hits yes
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")
                            exit()
                    #if international mins are selected 
                    if imins_recipt!="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+month_plan+data_plan+local_recipt+inter_recipt+total_recipt)
                        #if user hits yes
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")
                            exit()
                #if canada mins are selected 
                if cmins_recipt!="0":
                    #if international mins are not selected 
                    if imins_recipt=="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+month_plan+data_plan+local_recipt+canada_recipt+total_recipt)
                        #if user hits yes
                        if message_var==True:
                        #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")  
                            exit()
                    #if international mins are selected 
                    if imins_recipt!="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+month_plan+data_plan+local_recipt+canada_recipt+inter_recipt+total_recipt)
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")     
                            exit()
    #if apps are selected
    if numclick>=1:
        #if data plan is selected
        if data_plan_recipt=='0 GB':
            #if local mins are not selected 
            if lmins_recipt=="0":
                #if canada mins are not selected 
                if cmins_recipt=="0":
                    #if international mins are not selected 
                    if imins_recipt=="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+line_+respone_apps+output+total_recipt)
                        #if user hits yes
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")
                            exit()
                    #if international mins are selected 
                    if imins_recipt!="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+line_+respone_apps+output+month_plan+inter_recipt+total_recipt)
                        #if user hits yes
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")
                            exit()
                #if canada mins are selected 
                if cmins_recipt!="0":
                    if imins_recipt=="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+line_+respone_apps+output+month_plan+canada_recipt+total_recipt)
                        #if user hits yes
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")            
                            exit()
                    #if international mins are selected 
                    if imins_recipt!="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+line_+respone_apps+output+month_plan+canada_recipt+inter_recipt+total_recipt)
                        #if user hits yes
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")
                            exit()
            #if local mins are selected 
            if lmins_recipt!="0":
                #if canada mins are not selected 
                if cmins_recipt=="0":
                    #if international mins are not selected 
                    if imins_recipt=="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+line_+respone_apps+output+month_plan+local_recipt+total_recipt)
                        #if user hits yes
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")
                            exit()
                    #if international mins are selected 
                    if imins_recipt!="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+line_+respone_apps+output+month_plan+local_recipt+inter_recipt+total_recipt)
                        #if user hits yes
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")
                            exit()
                #if canada mins are not selected 
                if cmins_recipt!="0":
                    if imins_recipt=="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+line_+respone_apps+output+month_plan+local_recipt+canada_recipt+total_recipt)
                        #if user hits yes
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")
                            exit()
                    #if international mins are not selected 
                    if imins_recipt!="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+line_+respone_apps+output+month_plan+local_recipt+canada_recipt+inter_recipt+total_recipt)
                        #if user hits yes
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")
                            exit()
        #if data is selected
        if data_plan_recipt!='0 GB':
            #if local mins are not selected 
            if lmins_recipt=="0":
                #if canada mins are not selected 
                if cmins_recipt=="0":
                    #if international mins are not selected 
                    if imins_recipt=="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+line_+respone_apps+output+month_plan+data_plan+total_recipt)
                        #if user hits yes
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")
                            exit()
                    #if international mins are selected 
                    if imins_recipt!="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+line_+respone_apps+output+month_plan+data_plan+inter_recipt+total_recipt)
                        #if user hits yes
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")
                            exit()
                #if canada mins are selected 
                if cmins_recipt!="0":
                    #if international mins are not selected 
                    if imins_recipt=="0": 
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+line_+respone_apps+output+month_plan+data_plan+canada_recipt+total_recipt)
                        #if user hits yes
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")
                            exit()
                    #if international mins are selected 
                    if imins_recipt!="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+line_+respone_apps+output+month_plan+data_plan+canada_recipt+inter_recipt+total_recipt)
                        #if user hits yes
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")
                            exit()
            #if local mins are selected 
            if lmins_recipt!="0":
                #if canada mins are not selected 
                if cmins_recipt=="0":
                    #if international mins are not selected 
                    if imins_recipt=="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+line_+respone_apps+output+month_plan+data_plan+local_recipt+total_recipt)
                        #if user hits yes
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")
                            exit()
                    #if international mins are selected 
                    if imins_recipt!="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+line_+respone_apps+output+month_plan+data_plan+local_recipt+inter_recipt+total_recipt)
                        #if user hits yes
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")
                            exit()
                #if canada mins are selected 
                if cmins_recipt!="0":
                    if imins_recipt=="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+line_+respone_apps+output+month_plan+data_plan+local_recipt+canada_recipt+total_recipt)
                        #if user hits yes
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")
                            exit()
                    #if international mins are not selected 
                    if imins_recipt!="0":
                        #create and output message box
                        message_var=messagebox.askyesno("Order Summary",response_phone+line_+respone_apps+output+month_plan+data_plan+local_recipt+canada_recipt+inter_recipt+total_recipt)
                        #if user hits yes
                        if message_var==True:
                            #create and output message box
                            messagebox.showinfo("Rogers Wireless", "Thank you for choosing Rogers! Enjoy the purchase of your new phone.")
                            #exit
                            exit()
#if clear button is hit                       
def clear_button():
    #globalize variables
    global price_app,numclick,grand_total,discount_total,total,data_price,price_mins,price_canada,price_inter,price_,hst,name_app,phone_colour,amount_gb,lmins_recipt,cmins_recipt,imins_recipt
    #make first 11 variables ==0 
    price_=0
    numclick=0
    price_app=0
    data_price=0
    price_mins=0
    price_canada=0
    price_inter=0
    total=0
    discount_total=0
    hst=0
    grand_total=0
    #make phone red 
    phone_colour="Red"
    #set to ""
    amount_gb=""
    #reset the list 
    name_app=[""]*12
    #reset the data 
    data_plan_recipt="0 GB"
    #reset the local mins
    lmins_recipt="0"
    #reset the canada mins
    cmins_recipt="0"
    #reset the international mins
    imins_recipt="0"
    #output 0.00 for the mins labels
    i_min.config(text="0.00")
    c_min.config(text="0.00")
    monthly_price.config(text="$0.00")
    l_min.config(text="0.00")
    d_plan.config(text="0.00")
    #make the checkbuttuns false
    check_btn1.set(value=False)
    check_btn2.set(value=False)
    check_btn3.set(value=False)
    check_btn4.set(value=False)
    check_btn5.set(value=False)
    check_btn6.set(value=False)
    check_btn7.set(value=False)
    check_btn8.set(value=False)
    check_btn9.set(value=False)
    check_btn10.set(value=False)
    check_btn11.set(value=False)
    check_btn12.set(value=False)
    #set price to 0 and ouptut $0.00
    app_price.config(text="$0.00")
    #first phone is selected
    var_phone.set(value=0)
    #config price
    phone_price.config(text="$0.00")
    subtotal_borderlbl.config(text="{:^25s}".format("$0.00"))
    discount_borderlbl.config(text="{:^25s}".format("$0.00"),bg="white",fg="black")
    hst_borderlabel.config(text="{:^25s}".format("$0.00"))
    grand_total_borderlabel.config(text="{:^25s}".format("$0.00"))
    #set state to normal
    btn_64.config(state=NORMAL)
    btn_256.config(state=NORMAL)
    btn_512.config(state=NORMAL)
    btn_128.config(state=NORMAL)
    #set comboboxes to 0
    cbo.set(value=0)
    cbo1.set(value=0)
    cbo2.set(value=0)
    cbo3.set(value=0)

#-------------------------------------- 
#create window
window=Tk()
#make window title
window.title("Rogers Wireless")
#exit button when x is hit on the window
window.protocol('WM_DELETE_WINDOW', close_button)
#variable holding rogers logo
imgLogo=PhotoImage(file="rogers_logo.png")
#resize the logo
imgLogo=imgLogo.subsample(3)
#create label with image
img_lbl=Label(window,image=imgLogo,borderwidth=0)
#output the image
img_lbl.grid(row=0,columnspan=3)
#Create and set the properties of the label frame
frame=LabelFrame(window,fg="red",text="SELECT A PHONE",padx=5)
#place on grid
frame.grid(row=1,column=0,padx=10)

#--------------------------------------  Variables
#phone images
img_file=["iphone_red.png","iphone_blue.png","iphone_white.png","iphone_black.png"]
#price of phone
price_=0
numclick=0
#price of the apps
price_app=0
#data price
data_price=0
#price of mins
price_mins=0
price_canada=0
price_inter=0
total=0
discount_total=0
hst=0
grand_total=0
phone_colour="Red"
amount_gb=""
#list that will hold the apps
name_app=[""]*12
data_plan_recipt="0 GB"
lmins_recipt="0"
cmins_recipt="0"
imins_recipt="0"
#-------------------------------------- 
#variable that hold the phone image
phone_img=PhotoImage(file=img_file[0])
#resize the image
phone_img=phone_img.subsample(6)
#put on the label
phone_lbl=Label(frame,image=phone_img)
#put on the grid
phone_lbl.grid(row=0,rowspan=4)

#-------------------------------------- Radiobuttons
#holds value 
var_phone=IntVar()
#Create and set the properties of the red button
red_radbtn=Radiobutton(frame,text="Red",width=7,anchor="w",variable=var_phone,value=0,command=show_phone)
#place the red button on the grid
red_radbtn.grid(row=0,column=1,padx=10)
#Create and set the properties of the blue button
blue_radbtn=Radiobutton(frame,text="Blue",width=7,anchor="w",variable=var_phone,value=1,command=show_phone)
#place the blue button on the grid
blue_radbtn.grid(row=1,column=1,padx=10)
#Create and set the properties of the white button
white_radbtn=Radiobutton(frame,text="White",width=7,anchor="w",variable=var_phone,value=2,command=show_phone)
#place the white button on the grid
white_radbtn.grid(row=2,column=1,padx=10)
#Create and set the properties of the black button
black_radbtn=Radiobutton(frame,text="Black",width=7,anchor="w",variable=var_phone,value=3,command=show_phone)
#place the black button on the grid
black_radbtn.grid(row=3,column=1,padx=10)

#-------------------------------------- buttons
#Create and set the properties of the 64gb button
btn_64=Button(frame,text="64 GB",width=10,command=_64gb)
#place the 64gb button on the grid
btn_64.grid(row=0,column=2,padx=10)

#Create and set the properties of the 128gb button
btn_128=Button(frame,text="128 GB",width=10,command=_128gb)
#place the 128gb button on the grid
btn_128.grid(row=1,column=2,padx=10)

#Create and set the properties of the 256gb button
btn_256=Button(frame,text="256 GB",width=10,command=_256gb)
#place the 256gb button on the grid
btn_256.grid(row=2,column=2,padx=10)
#Create and set the properties of the 512gb button
btn_512=Button(frame,text="512 GB",width=10,command=_512gb)
#place the 512gb button on the grid
btn_512.grid(row=3,column=2,padx=10)
#-------------------------------------- 
#Create and set the properties of the 2nd frame
frame2=LabelFrame(window,fg="red",text="SELECT APPLICATIONS",pady=13,padx=5)
#place the frame on the grid
frame2.grid(row=1,column=1,padx=10)

#-------------------------------------- App 1
#hold app image
app1=PhotoImage(file="app0.png")
#resize app
app1=app1.subsample(2)
#variable that tells which checkbutton was selected
check_btn1=BooleanVar()
#Create and set the properties of the checkbutton
chkbtn_1=Checkbutton(frame2,variable=check_btn1,onvalue=True,offvalue=False,command=check_app1,image=app1,padx=5)
#place the checkbutton on the grid
chkbtn_1.grid(row=0,column=0)
#-------------------------------------- App 2
#hold app image
app2=PhotoImage(file="app1.png")
#resize app
app2=app2.subsample(2)
#variable that tells which checkbutton was selected
check_btn2=BooleanVar()
#Create and set the properties of the checkbutton
chkbtn_2=Checkbutton(frame2,variable=check_btn2,onvalue=True,offvalue=False,command=check_app2,image=app2,padx=5)
#place the checkbutton on the grid
chkbtn_2.grid(row=0,column=2)
#-------------------------------------- App 3
#hold app image
app3=PhotoImage(file="app2.png")
#resize app
app3=app3.subsample(2)
#variable that tells which checkbutton was selected
check_btn3=BooleanVar()
#Create and set the properties of the checkbutton
chkbtn_3=Checkbutton(frame2,variable=check_btn3,onvalue=True,offvalue=False,command=check_app3,image=app3,padx=5)
#place the checkbutton on the grid
chkbtn_3.grid(row=0,column=4)
#-------------------------------------- App 4
#hold app image
app4=PhotoImage(file="app3.png")
#resize app
app4=app4.subsample(2)
#variable that tells which checkbutton was selected
check_btn4=BooleanVar()
#Create and set the properties of the checkbutton
chkbtn_4=Checkbutton(frame2,variable=check_btn4,onvalue=True,offvalue=False,command=check_app4,image=app4,padx=5)
#place the checkbutton on the grid
chkbtn_4.grid(row=0,column=6)
#-------------------------------------- App 5
#hold app image
app5=PhotoImage(file="app4.png")
#resize app
app5=app5.subsample(2)
#variable that tells which checkbutton was selected
check_btn5=BooleanVar()
#Create and set the properties of the checkbutton
chkbtn_5=Checkbutton(frame2,variable=check_btn5,onvalue=True,offvalue=False,command=check_app5,image=app5,padx=5)
#place the checkbutton on the grid
chkbtn_5.grid(row=1,column=0)
#-------------------------------------- App 6
#hold app image
app6=PhotoImage(file="app5.png")
#resize app
app6=app6.subsample(2)
#variable that tells which checkbutton was selected
check_btn6=BooleanVar()
#Create and set the properties of the checkbutton
chkbtn_6=Checkbutton(frame2,variable=check_btn6,onvalue=True,offvalue=False,command=check_app6,image=app6,padx=5)
#place the checkbutton on the grid
chkbtn_6.grid(row=1,column=2)
#-------------------------------------- App 7
#hold app image
app7=PhotoImage(file="app6.png")
#resize app
app7=app7.subsample(2)
#variable that tells which checkbutton was selected
check_btn7=BooleanVar()
#Create and set the properties of the checkbutton
chkbtn_7=Checkbutton(frame2,variable=check_btn7,onvalue=True,offvalue=False,command=check_app7,image=app7,padx=5)
#place the checkbutton on the grid
chkbtn_7.grid(row=1,column=4)
#-------------------------------------- App 8
#hold app image
app8=PhotoImage(file="app7.png")
#resize app
app8=app8.subsample(2)
#variable that tells which checkbutton was selected
check_btn8=BooleanVar()
#Create and set the properties of the checkbutton
chkbtn_8=Checkbutton(frame2,variable=check_btn8,onvalue=True,offvalue=False,command=check_app8,image=app8,padx=5)
#place the checkbutton on the grid
chkbtn_8.grid(row=1,column=6)
#-------------------------------------- App 9
#hold app image
app9=PhotoImage(file="app8.png")
#resize app
app9=app9.subsample(2)
#variable that tells which checkbutton was selected
check_btn9=BooleanVar()
#Create and set the properties of the checkbutton
chkbtn_9=Checkbutton(frame2,variable=check_btn9,onvalue=True,offvalue=False,command=check_app9,image=app9,padx=5)
#place the checkbutton on the grid
chkbtn_9.grid(row=2,column=0)
#-------------------------------------- App 10
#hold app image
app10=PhotoImage(file="app9.png")
#resize app
app10=app10.subsample(2)
#variable that tells which checkbutton was selected
check_btn10=BooleanVar()
#Create and set the properties of the checkbutton
chkbtn_10=Checkbutton(frame2,variable=check_btn10,onvalue=True,offvalue=False,command=check_app10,image=app10,padx=5)
#place the checkbutton on the grid
chkbtn_10.grid(row=2,column=2)
#-------------------------------------- App 11
#hold app image
app11=PhotoImage(file="app10.png")
#resize app
app11=app11.subsample(2)
#variable that tells which checkbutton was selected
check_btn11=BooleanVar()
#Create and set the properties of the checkbutton
chkbtn_11=Checkbutton(frame2,variable=check_btn11,onvalue=True,offvalue=False,command=check_app11,image=app11,padx=5)
#place the checkbutton on the grid
chkbtn_11.grid(row=2,column=4)
#-------------------------------------- App 12
#hold app image
app12=PhotoImage(file="app11.png")
#resize app
app12=app12.subsample(2)
#variable that tells which checkbutton was selected
check_btn12=BooleanVar()
#Create and set the properties of the checkbutton
chkbtn_12=Checkbutton(frame2,variable=check_btn12,onvalue=True,offvalue=False,command=check_app12,image=app12,padx=5)
#place the checkbutton on the grid
chkbtn_12.grid(row=2,column=6)
#-------------------------------------- Frame
#create and set properties of the 3rd frame
frame3=LabelFrame(window,fg="red",text="SELECT A MONTHLY PLAN",pady=11,padx=5)
#place the frame on the grid
frame3.grid(row=1,column=2,padx=10)

#-------------------------------------- Label
#create and set properties of the label
gb_lbl=Label(frame3,text="Data Plan (GB):",anchor="w",width=15)
#place the label on the grid
gb_lbl.grid(row=0,column=0,padx=5,pady=10)
#create and set properties of the label
l_min_lbl=Label(frame3,text="Local (mins):",anchor="w",width=15)
#place the label on the grid
l_min_lbl.grid(row=1,column=0,pady=10)
#create and set properties of the label
c_min_lbl=Label(frame3,text="Canada (mins):",anchor="w",width=15)
#place the label on the grid
c_min_lbl.grid(row=2,column=0,pady=10)
#create and set properties of the label
i_min_lbl=Label(frame3,text="U.S (mins):",anchor="w",width=15)
#place the label on the grid
i_min_lbl.grid(row=3,column=0,pady=10)

#-------------------------------------- Border labels
#create and set properties of the label
d_plan=Label(frame3,text="0.00",borderwidth=2,relief="solid", width=10)
#place the label on the grid
d_plan.grid(row=0,column=2)
#create and set properties of the label
l_min=Label(frame3,text="0.00",borderwidth=2,relief="solid", width=10)
#place the label on the grid
l_min.grid(row=1,column=2)
#create and set properties of the label
c_min=Label(frame3,text="0.00",borderwidth=2,relief="solid", width=10)
#place the label on the grid
c_min.grid(row=2,column=2)
#create and set properties of the label
i_min=Label(frame3,text="0.00",borderwidth=2,relief="solid", width=10)
#place the label on the grid
i_min.grid(row=3,column=2)

#-------------------------------------- Combobox
#list of the choices in the combobox
dataplan=["0 GB","1 GB","2 GB","5 GB","10 GB","UNLIMITED"]
#create and set properties of the combobox
cbo=ttk.Combobox(frame3,state="readonly",values=dataplan,width=10)
#select an option from the combobox
cbo.bind("<<ComboboxSelected>>",price_data)
#keep the combobox selected at 0
cbo.current(0)
#place combobox on the grid
cbo.grid(row=0,column=1)
#list of the choices in the combobox
localmins=["0","250","1000","UNLIMITED"]
#create and set properties of the combobox
cbo1=ttk.Combobox(frame3,state="readonly",values=localmins,width=10)
#select an option from the combobox
cbo1.bind("<<ComboboxSelected>>",price_mins_local)
#keep the combobox selected at 0
cbo1.current(0)
#place combobox on the grid
cbo1.grid(row=1,column=1)
#list of the choices in the combobox
canadamins=["0","250","1000","UNLIMITED"]
#create and set properties of the combobox
cbo2=ttk.Combobox(frame3,state="readonly",values=canadamins,width=10)
#select an option from the combobox
cbo2.bind("<<ComboboxSelected>>",price_mins_canada)
#keep the combobox selected at 0
cbo2.current(0)
#place combobox on the grid
cbo2.grid(row=2,column=1)
#list of the choices in the combobox
inter_mins=["0","250","1000","UNLIMITED"]
#create and set properties of the combobox
cbo3=ttk.Combobox(frame3,state="readonly",values=inter_mins,width=10)
#select an option from the combobox
cbo3.bind("<<ComboboxSelected>>",price_inter_mins)
#keep the combobox selected at 0
cbo3.current(0)
#place combobox on the grid
cbo3.grid(row=3,column=1)
#-------------------------------------- 
#create and set properties of first two apps are free label
lbl_2apps=Label(window,text="First two (2) apps are free!",pady=10,fg="red",font=("arial 15 bold"))
#place the first two apps are free label on the grid
lbl_2apps.grid(row=3,columnspan=3)

#-------------------------------------- 
#create and set properties of the label
phone_price=Label(window,text="$0.00",borderwidth=2,relief="solid", width=15)
#place label on the grid
phone_price.grid(row=4,column=0)
#create and set properties of the label
app_price=Label(window,text="$0.00",borderwidth=2,relief="solid", width=15)
#place label on the grid
app_price.grid(row=4,column=1)
#create and set properties of the label
monthly_price=Label(window,text="$0.00",borderwidth=2,relief="solid", width=15)
#place label on the grid
monthly_price.grid(row=4,column=2)
#-------------------------------------- 
#hold visa image
visa_img=PhotoImage(file="paymentoptions.png")
#resize the image
visa_img=visa_img.subsample(10)
#put the image in a label 
visaimg_output=Label(window,image=visa_img,pady=50)
#output the label on the grid
visaimg_output.grid(row=5,column=0)
#-------------------------------------- Calculate Labels
#create 4th frame
frame4=Frame(window)
#place 4th frame on the grid
frame4.grid(row=5,column=1)
#create and set properties of the label
subtotal_lbl=Label(frame4,text="SUBTOTAL:",anchor="w", width=15,pady=5)
#place label on the grid
subtotal_lbl.grid(row=0,column=0)
#create and set properties of the label
discount_lbl=Label(frame4,text="DISCOUNT:",anchor="w",width=15,pady=5)
#place label on the grid
discount_lbl.grid(row=1,column=0)
#create and set properties of the label
hst_label=Label(frame4,text="HST:",anchor="w",width=15,pady=5)
#place label on the grid
hst_label.grid(row=2,column=0)
#create and set properties of the label
grand_total_label=Label(frame4,text="GRAND TOTAL:",anchor="w",width=15,pady=5)
#place label on the grid
grand_total_label.grid(row=3,column=0)

#--------------------------------------
#create and set properties of the label 
subtotal_borderlbl=Label(frame4,text=" ",anchor="w",borderwidth=2,relief="solid", width=15)
#place label on the grid
subtotal_borderlbl.grid(row=0,column=1)
#create and set properties of the label
discount_borderlbl=Label(frame4,text=" ",anchor="w",borderwidth=2,relief="solid",width=15)
#place label on the grid
discount_borderlbl.grid(row=1,column=1)
#create and set properties of the label
hst_borderlabel=Label(frame4,text=" ",anchor="w",borderwidth=2,relief="solid",width=15)
#place label on the grid
hst_borderlabel.grid(row=2,column=1)
#create and set properties of the label
grand_total_borderlabel=Label(frame4,text=" ",anchor="w",borderwidth=2,relief="solid",width=15)
#place label on the grid
grand_total_borderlabel.grid(row=3,column=1)
#-------------------------------------- 
#create 5th frame
frame5=Frame(window)
#place 5th frame on the grid
frame5.grid(column=2,row=5)

#-------------------------------------- Calculate Buttons
#create and set properties of the button
calculate_btn=Button(frame5,text="CALCULATE",width=15,command=total_calc)
#place button on the grid
calculate_btn.grid(row=0,column=2,padx=10,pady=10)
#create and set properties of the button
checkout_btn=Button(frame5,text="CHECKOUT",width=15,state=DISABLED,command=checkout_)
#place button on the grid
checkout_btn.grid(row=1,column=2,padx=10,pady=5)
#create and set properties of the button
clear_btn=Button(frame5,text="CLEAR",width=15,command=clear_button)
#place button on the grid
clear_btn.grid(row=2,column=2,padx=10,pady=5)
#create and set properties of the button
exit_btn=Button(frame5,text="EXIT",width=15,command=close_button)
#place button on the grid
exit_btn.grid(row=3,column=2,padx=10,pady=5)
#-------------------------------------- 
#run the window
window.mainloop()