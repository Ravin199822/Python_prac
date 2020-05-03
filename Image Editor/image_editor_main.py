import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont



win=tk.Tk()
win.title("Image Editor")       # set title
win.geometry("1200x800")       # set window geometry




style = ttk.Style()
fontStyle = tkFont.Font(family="Lucida Grande", size=20)
fontStyle1 = tkFont.Font(family="Helvetica", size=10)











# Set notebook widget on main window
nb=ttk.Notebook(win) 

# Set three pages on Notebook using main
page1=ttk.Frame(nb)
page2=ttk.Frame(nb)
page3=ttk.Frame(nb)

# Set title of Pages
nb.add(page1, text=" Instructions ")
nb.add(page2, text=" Image Editor ")
nb.add(page3, text=" File Collector ")


# Set location of Notebook
# nb.grid(row=0, column=0, padx=3, pady=2)
nb.pack(expand=True,fill='both')




# ========================================== FOR Instruction Page =========================================================  

# Open Image                    # sharpness
# Image Viewer                  # Brightness
                                # Color
                                # resize
                                # extensin change





# Bydefault button              # According to user







# ========================================== FOR Image Editor Page =========================================================











# ========================================== FOR File Collector Page =========================================================  






# Extension
extension_tuple=('.aif','.cda','.mid','.midi','.mp3','.mpa','.ogg','.wav','.wma','.wpl','.7z','.arj','.deb','.pkg','.rar','.rpm','.gz','.z','.zip','.bin','.dmg','.iso','.toast','.vcd','.csv','.dat','.db','.dbf','.log','.mdb','.sav','.sql','.tar','.xml','.email','.eml','.emlx','.msg','.oft','.ost','.pst','.vcf','.apk','.bat','.cgi','.com','.exe','.gadget','.jar','.wsf','.fnt','.fon','.otf','.ttf','.ai','.bmp','.gif','.ico','.jpeg','.jpg','.png','.ps','.psd','.svg','.tif','.tiff','.asp','.aspx','.cer','.cfm','.css','.htm','.html','.js','.jsp','.part','.php','.py','.rss','.xhtml','.key','.odp','.pps','.ppt','.pptx','.c','.class','.cpp','.cs','.h','.java','.pl','.sh','.swift','.vb','.ods','.xls','.xlsm','.xlsx','.bak','.cab','.cfg','.cpl','.cur','.dll','.dmp','.drv','.icns','.ini','.lnk','.msi','.sys','.tmp','.3g2','.3gp','.avi','.flv','.h264','.m4v','.mkv','.mov','.mp4','.mpg','.mpeg','.rm','.swf','.vob','.wmv','.doc','.docx','.odt','.rtf','.tex','.txt','.wpd','.wps','.pdf')
extension_name=('audio_extensions','compressed_file_extensions','disc_and_media_extensions','database_file_extensions','email_extensions','executable_extensions','font_file_extensions','image_extensions','web_extensions','presentation_extensions','programming_extensions','spreadsheet_extensions','system_realated_extensions','video_extensions','file_extensions')


dict_extensions={
            'audio_extensions'          :   ('.aif','.cda','.mid','.midi','.mp3','.mpa','.ogg','.wav','.wma','.wpl'),
            'compressed_file_extensions':   ('.7z','.arj','.deb','.pkg','.rar','.rpm','.gz','.z','.zip'),
            'disc_and_media_extensions' :   ('.bin','.dmg','.iso','.toast','.vcd'),
            'database_file_extensions'  :   ('.csv','.dat','.db','.dbf','.log','.mdb','.sav','.sql','.tar','.xml'),
            'email_extensions'          :   ('.email','.eml','.emlx','.msg','.oft','.ost','.pst','.vcf'),
            'executable_extensions'     :   ('.apk','.bat','.cgi','.com','.exe','.gadget','.jar','.wsf'),
            'font_file_extensions'      :   ('.fnt','.fon','.otf','.ttf'),
            'image_extensions'          :   ('.ai','.bmp','.gif','.ico','.jpeg','.jpg','.png','.ps','.psd','.svg','.tif','.tiff'),
            'web_extensions'            :   ('.asp','.aspx','.cer','.cfm','.css','.htm','.html','.js','.jsp','.part','.php','.py','.rss','.xhtml'),
            'presentation_extensions'   :   ('.key','.odp','.pps','.ppt','.pptx'),
            'programming_extensions'    :   ('.c','.class','.cpp','.cs','.h','.java','.pl','.sh','.swift','.vb'),
            'spreadsheet_extensions'    :   ('.ods','.xls','.xlsm','.xlsx'),
            'system_realated_extensions':   ('.bak','.cab','.cfg','.cpl','.cur','.dll','.dmp','.drv','.icns','.ini','.lnk','.msi','.sys','.tmp'),
            'video_extensions'          :   ('.3g2','.3gp','.avi','.flv','.h264','.m4v','.mkv','.mov','.mp4','.mpg','.mpeg','.rm','.swf','.vob','.wmv'),
            'file_extensions'           :   ('.doc','.docx','.odt','.rtf','.tex','.txt','.wpd','.wps','.pdf')
}












# global variable
a=3

# Variables
page3_radio_var=tk.StringVar()
choose_location=tk.StringVar()
add_page3_loc_var=tk.StringVar()
acc_add_page3_loc_var=tk.StringVar()
acc_choose_no_ext_var=tk.IntVar()
acc_choose_location=tk.StringVar()





# Bydefault button              # According to user




# make lableframe
style.configure('BLUE.TLabelframe.Label', foreground='blue', font='bold')
style.configure('BLACK.TLabelframe.Label', foreground='black', font='bold')





# Widgets
# make lab;e for choose any option like by default or according to me
lable3=ttk.LabelFrame(page3,text="Choose any One Option : ",style='BLUE.TLabelframe')
lable3.grid(row=0,column=0,padx=60, pady=80,sticky=tk.E)



# Make radio button
# page3_checked=1
# def check_page3_radio(event=None):
#     a=page3_radio_var.get()
#     global page3_checked
#     if a==1:
#         page3_checked=1
#     if a==2:
#         page3_checked=2




# Making two radio button for by deafault and according to me
default_radio=ttk.Radiobutton(lable3, text= ' Bydefault ', value='bydefault', variable=page3_radio_var)
default_radio.grid(row=1,column=0,padx=20, pady=20, sticky=tk.W)

choosen_by_user_radio=ttk.Radiobutton(lable3, text= 'According to me', value='user', variable=page3_radio_var)
choosen_by_user_radio.grid(row=1,column=1,ipadx=20, ipady=30, sticky=tk.W)




# creater button
# ttk.Style().configure("TButton", padding=6, relief="flat",
#    background="#ccc")



error_pag3_lable=ttk.Label(page3,text="Please, choose option....", foreground='red',font=fontStyle)    # fo error on page3 (user not checked any radio button)

# making lable frame on page3 for bydefault and according to user
page3_bydefault_lableframe=ttk.LabelFrame(page3,text=" Bydefault : ",style='BLACK.TLabelframe')
page3_acc_user_lableframe=ttk.LabelFrame(page3,text=" According to me : ",style='BLACK.TLabelframe')


# Combobox of extensions and entry for folder name and lables also


# 1) add button for open location

add_page3_location=ttk.Entry(page3_bydefault_lableframe,width=60,textvariable=add_page3_loc_var)
ex_file_dest_loc=ttk.Label(page3_bydefault_lableframe,text="Enter path where you want to store your folders.....\n       e.g. F:/Downloads/New_Folder   ",foreground='blue',font=fontStyle1)
acc_add_page3_location=ttk.Entry(page3_acc_user_lableframe,width=60,textvariable=acc_add_page3_loc_var)
acc_ex_file_dest_loc=ttk.Label(page3_acc_user_lableframe,text="Enter path where you want to store your folders.....\n       e.g. F:/Downloads/New_Folder   ",foreground='blue',font=fontStyle1)
submit_btn_click_lable=ttk.Label(page3_bydefault_lableframe,text="Your task completed successfully......",foreground='black')
thank_bydefault_lable=ttk.Label(page3_bydefault_lableframe,text="Thank you for use....",foreground='blue',font=fontStyle)
acc_submit_btn_click_lable=ttk.Label(page3_acc_user_lableframe,text="Your task completed successfully......",foreground='blue')


def bydefault_ShowChoice():
    if choose_location.get()=='loc':
        submit_btn_click_lable.grid_remove()
        thank_bydefault_lable.grid_remove()
        add_page3_location.grid(row=2,columnspan=15,padx=20,pady=0)
        ex_file_dest_loc.grid(row=3,columnspan=15,padx=20,pady=0)

    if choose_location.get()=='custom':
        # remove grid when user choose custom loacton 
        submit_btn_click_lable.grid_remove()
        thank_bydefault_lable.grid_remove()
        add_page3_location.grid_remove()
        ex_file_dest_loc.grid_remove()

def acc_ShowChoice():
    if acc_choose_location.get()=='loc':
        acc_submit_btn_click_lable.grid_remove()
        acc_add_page3_location.grid(row=a,column=1,padx=0,pady=0)
        acc_ex_file_dest_loc.grid(row=a+1,column=1,padx=0,pady=0)

    if acc_choose_location.get()=='custom':
        acc_submit_btn_click_lable.grid_remove()
        acc_add_page3_location.grid_remove()
        acc_ex_file_dest_loc.grid_remove()

def createNewFolders():
    submit_btn_click_lable.grid(row=6,columnspan=2,padx=20,pady=20)
    thank_bydefault_lable.grid(row=7,columnspan=2,padx=20,pady=40)


def acc_createNewFolders():
    acc_submit_btn_click_lable.grid(row=a+3,columnspan=2,padx=20,pady=20)



def Scrollbar_creation():
    scroll_bar=tk.Scrollbar(page3_acc_user_lableframe)
    scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
    scroll_bar.config(command=win.yview)
    page3_acc_user_lableframe.config(yscrollcommand=scroll_bar.set)



def acc_choose_no_ext_func(event=None):
    print("acc_choose_no_ext_func is called")
    global a
    a=3
    ext=acc_choose_no_ext_var.get()
    if type(ext)==int:
        acc_extension_lable=ttk.Label(page3_acc_user_lableframe, text= " Choose Extension ",foreground='black')
        acc_extension_lable.grid(row=2,column=0,padx=100, pady=10, sticky=tk.W)
        acc_add_folder_name=ttk.Label(page3_acc_user_lableframe,text=" Enter Folder Name ", foreground='black' )
        acc_add_folder_name.grid(row=2,column=1,padx=100, pady=10, sticky=tk.W)

        
        count=0
        for i in range(ext+1):
            acc_choose_ext_forloop_combo=ttk.Combobox(page3_acc_user_lableframe,width=20, state='readonly')
            acc_folder_name_entry=ttk.Entry(page3_acc_user_lableframe, width=30)
            if a!=3 and count==0:
                acc_choose_ext_forloop_combo.forget()
                a=3
                count+=1
                print(i)
            acc_choose_ext_forloop_combo['values']=extension_tuple
            acc_choose_ext_forloop_combo.current(0)
            acc_choose_ext_forloop_combo.grid(row=a,column=0, padx=80, pady=10,sticky=tk.W)
            acc_folder_name_entry.grid(row=a,column=1, padx=80, pady=10,sticky=tk.W)
            a+=1  
        acc_combo_ext_btn.grid_remove()


        # Create radio Button 
        acc_custom_location_radio=ttk.Radiobutton(page3_acc_user_lableframe, text= 'Custom Location ', value='custom', variable=acc_choose_location,command =acc_ShowChoice)
        acc_custom_location_radio.grid(row=a,column=0,pady=30)

        acc_location_by_user_radio=ttk.Radiobutton(page3_acc_user_lableframe, text= 'At My Location', value='loc', variable=acc_choose_location,command =acc_ShowChoice)
        acc_location_by_user_radio.grid(row=a+1,column=0,pady=10)
        
        # Submit button
        page3_acc_submit_btn=ttk.Button(page3_acc_user_lableframe, text="Submit",style="C.TButton",command=acc_createNewFolders)
        page3_acc_submit_btn.grid(row=a+2, columnspan=3, pady=30)


 
    if type(ext)!=int:   # i have to make exception here
        print("Error")

print(f"outside a:{a}")


# this is button for crating combo boxes 
acc_combo_ext_btn=ttk.Button(page3_acc_user_lableframe,text=' Click me ',style="C.TButton",command=acc_choose_no_ext_func)

def createNewWindow():
    # print(page3_radio_var)
    page3_radio_var1=page3_radio_var.get()
    if page3_radio_var1=='bydefault':              # user cliked on bydefault
        lable3.destroy()
        page3_submit_btn.destroy()
        error_pag3_lable.destroy()

        # set lable frame for bydefault
        page3_bydefault_lableframe.pack(expand=True,fill='both', padx=10, pady=10)

        # create button in lableframe bydefault
        open_bydefault_btn=ttk.Button(page3_bydefault_lableframe, text="    Open Files Location   ",style="C.TButton")
        open_bydefault_btn.grid(row=0, column=0, padx=20, pady=20)

        # create lable for location
        loc_lable3=ttk.Label(page3_bydefault_lableframe,text="location is :")
        loc_lable3.grid(row=0,column=1,padx=0,pady=20)

        # Create Radio Button
        custom_location_radio=ttk.Radiobutton(page3_bydefault_lableframe, text= ' Custom Location ', value='custom', variable=choose_location,command =bydefault_ShowChoice)
        custom_location_radio.grid(row=1,column=0,padx=20, pady=20, sticky=tk.W)

        location_by_user_radio=ttk.Radiobutton(page3_bydefault_lableframe, text= 'At My Location', value='loc', variable=choose_location,command =bydefault_ShowChoice)
        location_by_user_radio.grid(row=1,column=1,ipadx=20, ipady=30, sticky=tk.W)

        # Calling bydefault_ShowChoice

        # Create Submit Button
        page3_bydefault_submit_btn=ttk.Button(page3_bydefault_lableframe, text="Submit",style="C.TButton",command=createNewFolders)
        page3_bydefault_submit_btn.grid(row=4, columnspan=2, pady=30)



    elif page3_radio_var1=='user':              # user clicked on according to me
        lable3.destroy()
        page3_submit_btn.destroy()
        error_pag3_lable.destroy()


        # set lable frame for according to usr
        page3_acc_user_lableframe.pack(fill=tk.BOTH,expand=True, padx=10, pady=10)
        

        # Create lable of no extension
        acc_choose_ext_lable=ttk.Label(page3_acc_user_lableframe,text=" No of Extensions   : ")
        acc_choose_ext_lable.grid(row=0,column=0,padx=50,pady=50,sticky=tk.W)
        



        # Making combo box for choose number of extension
        acc_choose_no_ext_combo=ttk.Combobox(page3_acc_user_lableframe,width=10,textvariable=acc_choose_no_ext_var, state='readonly')
        acc_choose_no_ext_combo['values']=(1,2,3,4,5)
        acc_choose_no_ext_combo.current(0)
        acc_choose_no_ext_combo.grid(row=0,column=1, padx=0, pady=50, sticky=tk.W)

        

        # Create button to get combobox values
        acc_combo_ext_btn.grid(row=1,columnspan=3,padx=150,pady=0,sticky=tk.W)




    else:
        error_pag3_lable.grid(row=2,column=0, pady=10)

# def get_page3(event=None):
#     ttk.PanedWindow(page3)

    # l1=ttk.Label(page3,text="Clicked")
    # l1.grid(row=2,column=0)




style.map("C.TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')]
    )

# submit button of page3 which give as data user clicks on bydefault or c=according to me
page3_submit_btn=ttk.Button(page3, text="Submit",style="C.TButton",command=createNewWindow)
page3_submit_btn.grid(row=1, columnspan=2)







#----------------------------------- BYDEFAULT ------------------------------------------------




#----------------------------------- ACCORDING TO USER ----------------------------------------------










win.mainloop()