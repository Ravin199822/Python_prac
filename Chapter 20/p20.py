# Python Modules


# Os Module
# we can do file move, delet, check extension using this module


# import os
# print(os.getcwd())                # o/p: F:\Python_prac\Chapter 20

# create folder

# path=(r'F:\Python_prac\Chapter 20\movies'
# os.mkdir("movies")                # when i ran first time, folder created, but when i ran second time i got error(FileExistsError: [WinError 183] Cannot create a folder when that folder already exists: 'movies')
# print(os.path.exists('movies'))   # o/p: True              # it will check file exists or not and we have to enter path of the folder instead of folder name only.
# if os.path.exists('movies'):
#     print("already exists")
# else:                                     # o/p: already exists
#     os.mkdir('movies')


# path=(r'F:\Python_prac\Chapter 20\movies')
# --OR---
# os.chdir(r'F:\Python_prac\Chapter 20')         and then use mkdir('movies') method

# create file
# open('file.txt','a').close()                           # it will create file, and it will not give error in case of file existing



# print(os.listdir())                         # o/p: ['file.txt', 'movies', 'p20.py']                  # it will return the list of files and folders of current working directory
# print(os.listdir(r'F:\Courses\python hindi'))        # o/p: ['harshit vashisth', 'test.py']



# # if we want file path                                # o/p: F:\Python_prac\Chapter 20\file.txt
# for item in os.listdir():                             #      F:\Python_prac\Chapter 20\movies
#     # print(os.getcwd()+'\\'+item)                      #      F:\Python_prac\Chapter 20\p20.py
#     # or
#     path=os.path.join(os.getcwd(),item)
#     print(path)




# for item in os.listdir(r'F:\Courses\python hindi'):                             
#     # print(r'F:\Courses\python hindi'+'\\'+item)                      
#     # or                                                                      # o/p: F:\Courses\python hindi\harshit vashisth
#     path=os.path.join(r'F:\Courses\python hindi',item)                        #      F:\Courses\python hindi\test.py
#     print(path)





# os.chdir(r'F:\Courses')
# print(os.listdir())

# # o/p: ['AWS', 'python 2', 'python hindi', '[FreeCourseLab.com] Udemy - Build Responsive Website Using HTML5, CSS3, JS And Bootstrap', '[FreeCourseLab.com] Udemy - Git for Windows Step-By-Step Mastery using Commands and GUI', '[FreeCourseLab.com] Udemy - Python 3 Complete Masterclass - Make Your Job Tasks Easier!', '[FreeCourseSite.com] Udemy - Docker Mastery The Complete Toolset From a Docker Captain', '[FreeTutorials.Eu] data-structures-algorithms-in-python', '[FreeTutorials.Eu] Udemy - Adobe Photoshop CC – Essentials Training Course', '[FreeTutorials.Eu] Udemy - sql-mysql-for-data-analytics-and-business-intelligence']






# os.chdir(r'F:\Python_prac\Chapter 20')
# # print(os.walk(r'F:\Python_prac\Chapter 20'))                   # o/p: <generator object walk at 0x00A0EED0>
# file_iter=os.walk(r'F:\Python_prac\Chapter 20')
# for current_path, folder_names, file_names in file_iter:
#     print(f"current_path : {current_path}")
#     print(f"folder_names : {folder_names}")
#     print(f"file_names   : {file_names}")

# #  o/p: current_path : F:\Python_prac\Chapter 20
# #       folder_names : ['movies']
# #       file_names   : ['file.txt', 'p20.py']
# #       current_path : F:\Python_prac\Chapter 20\movies      
# #       folder_names : ['Ravin']
# #       file_names   : ['New Microsoft Excel Worksheet.xlsx']
# #       current_path : F:\Python_prac\Chapter 20\movies\Ravin
# #       folder_names : []
# #       file_names   : ['New Bitmap Image.bmp']



# create folder inside folder
# os.makedirs('new/Ravin')                       # it will create Ravin folder inside new folder(here new and Ravin both are new folder)

# i want to delete folder

# os.rmdir('new')                  # o/p: OSError: [WinError 145] The directory is not empty: 'new'             this function delete only empty folder
# we can delete not empty folder using shutil module
# import shutil

# delete not empty folder
# shutil.rmtree('new')                               # rmtree function delete not empty folder permenantly, means folder will not move to the recycle bin
   
# copy not empty folder in another folder
# shutil.copytree('new','movies/new123')                 # copy new folder in movies and where new folder copied with new name like new123. we have to give path insted of folder name

# copy file in anoter folder
# shutil.copy(r'F:\Python_prac\Chapter 20\movies\a.xlsx',r'F:/Python_prac/Chapter 20/movies/new123/a1.xlsx')

# move one folder in another folder
# shutil.move(r'F:\Python_prac\Chapter 20\movies\new123',r'F:/Python_prac/Chapter 20/movies/Ravin/new1234')

# move file in another folder
# shutil.move(r'F:\Python_prac\Chapter 20\movies\a.xlsx',r'F:/Python_prac/Chapter 20/movies/new123/a2.xlsx')















# Edit Imagies using python  ---> we can do that using pillow library of python, but it is not standard library of python

# Installation of pillow library
#
# pip install Pillow


# how to change the extension
# resize image files
# resize multiple images using for loop 
# Sharpness
# Brightness
# Color
# Contrast
# Image blur, Gaussianblur



from PIL import Image
import os




# # how to change the extension
img1=Image.open(r'C:\Users\Rupen Rakholiya\Desktop\compress\x1.png')
# # if img1.mode == 'RGBA':
# #     img1 = img1.convert('RGB')
# # img1.save(r'F:\Python_prac\Chapter 20\Ravin\r.jpg')
# # img1.show()





# # resize image files
# max_size=(500,250)
# img1.thumbnail(max_size)
# img1.save(r'C:\Users\Rupen Rakholiya\Desktop\compress\z1.png')


# resize multiple images using for loop 

# How to deal with all files

# for item in os.listdir(r'F:\Python_prac\Chapter 20\Ravin'):
#     if item.endswith('.jpg'):
#         img1=Image.open(r'F:\Python_prac\Chapter 20\Ravin'+'\\'+item)
#         file_name, extension=os.path.splitext(item)
#         img1.save(r'F:\Python_prac\Chapter 20\Ravin'+'\\'+f'{file_name}.png')


# for item in os.listdir(r'F:\Python_prac\Chapter 20\Ravin'):
#     if item.endswith('.jpg'):
#         img1=Image.open(r'F:\Python_prac\Chapter 20\Ravin'+'\\'+item)
#         max_size=(250,250)
#         img1.thumbnail(max_size)
#         file_name, extension=os.path.splitext(item)
#         img1.save(r'F:\Python_prac\Chapter 20\Ravin'+'\\'+f'{file_name}r.png')






# sharpness, brightnessm color, contrast we have to import ImageEnhance module

# Sharpness 
from PIL import ImageEnhance


# img1=Image.open(r'F:\Python_prac\Chapter 20\Ravin\r2.jpg')
enhancer=ImageEnhance.Sharpness(img1)                                 # Sharpness is a class, ImageEnhance is a module
enhancer.enhance(5).save(r'C:\Users\Rupen Rakholiya\Desktop\compress\x2.png')
# # 0 ---> blurry image
# # 1 ---> original image
# # 2 ---> image with increased sharpness
# # 3,4,5... ---> sharpness will incress





# # # Color

# img1=Image.open(r'F:\Python_prac\Chapter 20\Ravin\r2edited1.jpg')
# enhancer=ImageEnhance.Color(img1)                                 # Color is a class, ImageEnhance is a module
# enhancer.enhance(2).save(r'F:\Python_prac\Chapter 20\Ravin\r2editedc.png')

# # 0 ---> black and white image
# # 1 ---> original image
# # 2,3,4...----> increase colour







# # # Brightness

# img1=Image.open(r'F:\Python_prac\Chapter 20\Ravin\r2edited1.jpg')
# enhancer=ImageEnhance.Brightness(img1)                                 # Brightness is a class, ImageEnhance is a module
# enhancer.enhance(1.5).save(r'F:\Python_prac\Chapter 20\Ravin\r2editedb.png')

# # 0 ---> black image
# # 1 ---> original image
# # 2,3,4...----> increase brightness





# # # Contrast

# img1=Image.open(r'F:\Python_prac\Chapter 20\Ravin\r2edited1.jpg')
# enhancer=ImageEnhance.Contrast(img1)                                 # Contrast is a class, ImageEnhance is a module
# enhancer.enhance(1.5).save(r'F:\Python_prac\Chapter 20\Ravin\r2editedco.png')

# # 0 ---> black and white image
# # 1 ---> original image
# # 2,3,4...----> increase contrast







# # Image blur  ----> for it we have to import filter
# from PIL import ImageFilter

# img1=Image.open(r'F:\Python_prac\Chapter 20\Ravin\r2edited1.jpg')
# img1.filter(ImageFilter.Gaussianblur(radius=4)).save(r'F:\Python_prac\Chapter 20\Ravin\r2blur.png')

# bydefault radius is 2
