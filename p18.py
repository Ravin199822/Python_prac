# Read text file

# open function
# read method
# seek method
# tell method
# readline method
# readlines method
# close method

path=(r'F:\Courses\python hindi\harshit vashisth\file1.txt)

f=open('file1.txt')                   # here i have to put txt's file path if .py file and .txt file are not in same folder.
                                      # f=open('file1.txt','r') ---for read file, f=open('file1.txt','w') ---for write file, f=open('file1.txt')----bydefault is reading mode
print(f.read())                # f.read() will return me file data in string form
f.close()

# o/p: 
#      -------------- Important things to remember -----------------
#      -- never do something to impress someone.
#      -- never live your life on someone else opinions.
#      -- Just find whatever you love and then hustle untill you don't need to introduce yourself.




f1=open('file1.txt')                      # o/p: -------------- Important things to remember -----------------
print(f1.read())                          #      -- never do something to impress someone.
print(f1.read())                          #      -- never live your life on someone else opinions.
f1.close()                                #      -- Just find whatever you love and then hustle untill you don't need to introduce yourself.
# python will return file data only one time even though we wrote print(f1.read()) two times. 
# this is happen because python read text file according to cursor, hemce when second time print(f1.read()) executed, our cursor was on last position in file, therefore we got data only one time




f2=open('file1.txt')                      # o/p: cursor position - 0
print(f"cursor position - {f2.tell()}")   #      -------------- Important things to remember -----------------
print(f2.read())                          #      -- never do something to impress someone.
print(f"cursor position - {f2.tell()}")   #      -- never live your life on someone else opinions.
print(f2.read())                          #      -- Just find whatever you love and then hustle untill you don't need to introduce yourself.
f2.close()                                #      cursor position - 250

# tell() method is used for getting position of cursor






seeh() method----> it is used for changing the position of cursor
f3=open('file1.txt') 
print(f"cursor position - {f3.tell()}")                    
print(f3.read())   
print(f"cursor position - {f3.tell()}") 
print("Before seek method")
f3.seek(0)     
print("After seek method")
print(f"cursor position - {f3.tell()}")    
print(f3.read())                          
f3.close()                              

# o/p: cursor position - 0
#      -------------- Important things to remember -----------------
#      -- never do something to impress someone.
#      -- never live your life on someone else opinions.
#      -- Just find whatever you love and then hustle untill you don't need to introduce yourself.
#      cursor position - 248
#      Before seek method
#      After seek method
#      cursor position - 0
#      -------------- Important things to remember -----------------
#      -- never do something to impress someone.
#      -- never live your life on someone else opinions.
#      -- Just find whatever you love and then hustle untill you don't need to introduce yourself.






readline() method  ----> read one line at a time

f4=open('file1.txt')     
print(f4.readline())                          
f4.close()                          # o/p: -------------- Important things to remember -----------------


f4=open('file1.txt')     
print(f4.readline())        
print(f4.readline())                          
print(f4.readline())                          
f4.close()

# o/p: -------------- Important things to remember -----------------

#      -- never do something to impress someone.

#      -- never live your life on someone else opinions.


f4=open('file1.txt')     
print(f4.readline(),end='')         # to remove space between two line
print(f4.readline())                          
print(f4.readline())                          
f4.close()

# o/p: -------------- Important things to remember -----------------
#      -- never do something to impress someone.

#      -- never live your life on someone else opinions.





readlines() method ----> it will make list of lines which are in file
f4=open('file1.txt')     
lines=f4.readlines()
print(lines)                      
print(len(lines))        # o/p: 4
f4.close()               # o/p: ['-------------- Important things to remember -----------------\n', '-- never do something to impress someone.\n', '-- never live your life on someone else opinions.\n', "-- Just find whatever you love and then hustle untill you don't need to introduce yourself."]


f4=open('file1.txt')                 # o/p: -------------- Important things to remember -----------------
lines=f4.readlines()                 #      -- never do something to impress someone.
for line in lines:                   #      -- never live your life on someone else opinions.
    print(line,end='')               #      -- Just find whatever you love and then hustle untill you don't need to introduce yourself.
f4.close()




# name, closed  ----> data descripter
f4=open('file1.txt')     
print(f4.name)                  # o/p: file1.txt
print(f4.closed)                # o/p: False
f4.close()
print(f4.closed)                # o/p: True





# without using read function, f4 is iterable
f4=open('file1.txt')                 # o/p: -------------- Important things to remember -----------------
for line in f4:                      #      -- never do something to impress someone.
    print(line,end='')               #      -- never live your life on someone else opinions.
f4.close()                           #      -- Just find whatever you love and then hustle untill you don't need to introduce yourself.



# i can make slicing with the help of readlines() method
f4=open('file1.txt')                 # o/p: -------------- Important things to remember -----------------
for line in f4.readlines()[:2]:      #      -- never do something to impress someone.
    print(line,end='')               
f4.close()