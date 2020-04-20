# Create GUI app with Python, Tkinter

# python tkinter tutorial

# python's standard library
# we can make GUI application using this library
# pronunciation: tee-kinter, tk-inter, kinter


# starter code
# import tkinter
# window=tkinter.Tk()                     # Tk is constructor(it will create the window)
# window.mainloop()                       # mainloop is method
# these three line will return window when we will run
# we must write these above three line when we want to make GUI application using Tkinter.




# import tkinter
# window=tkinter.Tk()                    
# window.title("GUI")                        # this will change the name of window
# window.mainloop()





# from tkinter import *                      # importing tkinter libray in other way
# window=Tk()                    
# window.title("GUI")                        
# window.mainloop()





# starter code
import tkinter as tk
from  tkinter import ttk
window=tk.Tk()                    
window.title("GUI")


# create lables ---->lables can be a text, or lable of any thing(stuff)

# widgets(label, button, radio buttons) ---> available in tk and ttk library
# we can use tk or ttk for widgets but ttk widgets are more attractive in terms of design

# name_label=tk.Label(window,text="Enter Your name : ")
name_lable=ttk.Label(window,text="Enter Your name : ")
name_lable.grid(row=0,column=0,sticky=tk.W)                             # # there are two methos for set location of widget 1)pack (name_label.pack()), 2)grid(name_lable.grid(row=0,column=0))

email_lable=ttk.Label(window,text="Enter your E-mail : ")
email_lable.grid(row=1,column=0,sticky=tk.W)

age_label=ttk.Label(window,text="Enter your age : ")
age_label.grid(row=2,column=0,sticky=tk.W)                               # stiky=tk.W  is used for start line from lest side window(stick leble on WEST side)

gender_label=ttk.Label(window,text="Gender : ")
gender_label.grid(row=3,column=0,sticky=tk.W) 

radio_lable=ttk.Label(window,text='Your occuptionption : ')
radio_lable.grid(row=4,column=0,sticky=tk.W)




# Create Entry box
# name_entry=ttk.Entry(window,width=18)
# name_entry.grid(row=0,column=1)
name_var=tk.StringVar()
name_entry=ttk.Entry(window,width=18,textvariable=name_var)                           # what ever we will write in entry box, it will be stored in name_var
name_entry.grid(row=0,column=1)
name_entry.focus()

email_var=tk.StringVar()
email_entry=ttk.Entry(window,width=18,textvariable=email_var)                           
email_entry.grid(row=1,column=1)

age_var=tk.IntVar()
age_entry=ttk.Entry(window,width=18,textvariable=age_var)                           
age_entry.grid(row=2,column=1)




# Create Combo box
gender_var=tk.StringVar()
gender_combo=ttk.Combobox(window,width=15, textvariable=gender_var,state='readonly')               # state is for make comobo box read only, it means we can not write inside combo box
gender_combo['values']=('Male','Female','Other')
gender_combo.current(0)                                          # it is for set the value in comobo box
gender_combo.grid(row=3,column=1)




# create radio button
occuption_var=tk.StringVar()
radio_student=ttk.Radiobutton(window,text='Student', value='Student', variable=occuption_var)
radio_student.grid(row=4,column=1)

radio_teacher=ttk.Radiobutton(window,text='Teacher', value='Teacher', variable=occuption_var)
radio_teacher.grid(row=4,column=2)





# Create Checck Button
check_var=tk.IntVar()
check_button=ttk.Checkbutton(window,text="check if you want to subscribe to our newsletter",variable=check_var)
check_button.grid(row=5,columnspan=3)                         # columnspan is used for taking column without affecting other one. If we write only column we got affected GUI in terms of space.





# create button
# def action():
#     user_name=name_var.get()              # here, get() method is used for getting value of variable
#     user_mail=email_var.get()
#     user_age=age_var.get()
#     user_gender=gender_var.get()
#     user_occuption=occuption_var.get()
#     # for check box, beccause check box will return 0 or 1.
#     if check_var.get()==0:
#         user_checked='NO'
#     else:
#         user_checked="YES"
#     print(f'name:{user_name}, mail-id:{user_mail}, age:{user_age}, gender:{user_gender}, occuption:{user_occuption},Subscribed:{user_checked}')
#     with open("data.txt","a") as data:                    # this code for stotre value in file
#         data.write(f'{user_name},{user_mail},{user_age},{user_gender},{user_occuption},{user_checked}  \n' )
    
#     # these three lines for deleteing values from edit box after clicking on submit button
#     name_entry.delete(0,tk.END)
#     email_entry.delete(0,tk.END)
#     age_entry.delete(0,tk.END)

#     # when we want to change color of name lable after clicking on submit button
#     name_lable.configure(foreground="Blue")             # here we can use color code instead of color name              
#     # name_lable.configure(background="Blue")
#     # window.configure(background="Pink")                # change background color of window
#     # submit_button.configure(foreground="Blue")         # in this we will get error, for doing this we have to use stylish, otherwise use tk insted of ttk in submit_button=tk.Button(.....)



# write into CSV
from csv import DictWriter
import os
def action():
    user_name=name_var.get()              # here, get() method is used for getting value of variable
    user_mail=email_var.get()
    user_age=age_var.get()
    user_gender=gender_var.get()
    user_occuption=occuption_var.get()
    # for check box, beccause check box will return 0 or 1.
    if check_var.get()==0:
        user_checked='NO'
    else:
        user_checked="YES"
    print(f'name:{user_name}, mail-id:{user_mail}, age:{user_age}, gender:{user_gender}, occuption:{user_occuption},Subscribed:{user_checked}')
    

    # write to csv
    with open("data.csv","a",newline='') as data:                    # this code for stotre value in file
        dict_write=DictWriter(data, fieldnames=['User_name','E_mail',"Age",'Gender','Occuption','Subscribed'])
        if os.stat('data.csv').st_size==0:
            dict_write.writeheader()
        dict_write.writerow({
            "User_name" : user_name,
            "E_mail"    : user_mail,
            "Age"       : user_age,
            "Gender"    : user_gender,
            "Occuption" : user_occuption,
            "Subscribed": user_checked
        })
    
    # these three lines for deleteing values from edit box after clicking on submit button
    name_entry.delete(0,tk.END)
    email_entry.delete(0,tk.END)
    age_entry.delete(0,tk.END)

    # when we want to change color of name lable after clicking on submit button
    name_lable.configure(foreground="Blue")




submit_button=ttk.Button(window,text="Submit",command=action)              # command is for calling method
submit_button.grid(row=6,column=0)



window.mainloop()