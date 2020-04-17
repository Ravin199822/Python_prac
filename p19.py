# File3.csv
# name,email,phone_no
# Ravin,ravinrakholiya559@gmail.com,+918732904392
# Rupen,rupenrakholiya559@gmail.com,+917433089863






# Work with CSV File
# csv file ---> used for storing data in tabula form




# Read to CSV
# we can read csv file using reader function or DictReader class from csv module


# Read csv file using reader
from csv import reader
with open('file3.csv','r') as rf:
    csv_reader=reader(rf)
    # csv_reader is iterator
    print(csv_reader)                   # o/p: <_csv.reader object at 0x0125D8E8>
    print(type(csv_reader))             # o/p: <class '_csv.reader'>
    for i in csv_reader:                # csv_reader is iterator so we can print it only one time, if we want to use more than one time then we can convert it into list.
        print(i)

# o/p: ['name', 'email', 'phone_no']                 # but here column name also printed, we can overcome this problem using next() methos
#      ['Ravin', 'ravinrakholiya559@gmail.com', '+918732904392']
#      ['Rupen', 'rupenrakholiya559@gmail.com', '+917433089863']





# from csv import reader
# with open(r'file3.csv','r',encoding='utf=8') as rf:
#     csv_reader=reader(rf)
#     # csv_reader is iterator
#     print(csv_reader)                   # o/p: <_csv.reader object at 0x0125D8E8>
#     print(type(csv_reader))             # o/p: <class '_csv.reader'>
#     next(csv_reader)
#     for i in csv_reader:                # o/p: ['Ravin', 'ravinrakholiya559@gmail.com', '+918732904392']
#         print(i)                        #      ['Rupen', 'rupenrakholiya559@gmail.com', '+917433089863']








# Read csv file using DictReader
from csv import DictReader                          # we read csv file as ordered dictionary using DictReader
with open('file3.csv','r') as rf:
    csv_reader1=DictReader(rf)
    print(type(csv_reader1))                         # o/p: <class 'csv.DictReader'>
    for line in csv_reader1:
        print(line)

# o/p: {'name': 'Ravin', 'email': 'ravinrakholiya559@gmail.com', 'phone_no': '+918732904392'}
#      {'name': 'Rupen', 'email': 'rupenrakholiya559@gmail.com', 'phone_no': '+917433089863'}







from csv import DictReader                          
with open('file3.csv','r') as rf:                    # o/p: Ravin
    csv_reader1=DictReader(rf)                       # o/p: Rupen
    for line in csv_reader1:
        print(line['name'])






    

# File3.csv
# name|email|phone_no
# Ravin|ravinrakholiya559@gmail.com|+918732904392
# Rupen|rupenrakholiya559@gmail.com|+917433089863

from csv import DictReader                          
with open('file3.csv','r') as rf:                    # o/p: {'name|email|phone_no': 'Ravin|ravinrakholiya559@gmail.com|+918732904392'}
    csv_reader1=DictReader(rf)                       #      {'name|email|phone_no': 'Rupen|rupenrakholiya559@gmail.com|+917433089863'}
    for line in csv_reader1:
        print(line)



# sometimes we get error just because of | instead of , so we can address this issue by using delimiter
from csv import DictReader                          
with open('file3.csv','r') as rf:                    # o/p: {'name': 'Ravin', 'email': 'ravinrakholiya559@gmail.com', 'phone_no': '+918732904392'}
    csv_reader1=DictReader(rf,delimiter='|')         #      {'name': 'Rupen', 'email': 'rupenrakholiya559@gmail.com', 'phone_no': '+917433089863'}
    for line in csv_reader1:
        print(line)




# DictReader is better than reader





# Write to CSV
# writer, DictWriter  -----> for write into csv file


# write into csv using writer
from csv import writer
with open('file3.csv','w') as wf:                    # now file3.csv is empty
    csv_write=writer(wf)                  # there are two methods in writer for writing 1)writerow, 2)writerows
    csv_write.writerow(['name','country'])
    csv_write.writerow(['Rupen','Germany'])
    csv_write.writerow(['Ravin','India'])
    csv_write.writerow(['Yash','Austrelia'])

# o/p: name,country
                                            # here we are getting line spce between two row data
#      Rupen,Germany

#      Ravin,India

#      Yash,Austrelia






from csv import writer
with open('file3.csv','w',newline='') as wf:                    # now file3.csv is empty
    csv_write=writer(wf)                  # there are two methods in writer for writing 1)writerow, 2)writerows

    # # 1)writerow   ----> inside list
    # csv_write.writerow(['name','country'])                                             # o/p: name,country
    # csv_write.writerow(['Rupen','Germany'])                                            #      Rupen,Germany
    # csv_write.writerow(['Ravin','India'])                                              #      Ravin,India
    # csv_write.writerow(['Yash','Austrelia'])                                           #      Yash,Austrelia


    # 2)writerows    ----> inside list inside list
    csv_write.writerows([['name','country'],['Rupen','Germany'],['Ravin','India'],['Yash','Austrelia']])



# here we are using from csv import dict....., we can do this by using only import csv, but we don't import csv because if we import csv then python searching for dict... and it may take more time





# write into csv using DictWriter
from csv import DictWriter                            # when we use dictwrite we have to show header(colum_name) in code
with open("file3.csv",'w') as wf:                     # file3.csv is empty
    csv_write=DictWriter(wf,fieldnames=['first_name','last_name','age'])
    csv_write.writeheader()                                # this method will write header in csv file
                 # here, also two methos for writing in csv 1) writerow    2) wrterows
    csv_write.writerow({
        'first_name':'Ravin',
        'last_name':'Rakholiya',
        'age':22
    })                                                      # o/p: first_name,last_name,age
    csv_write.writerow({                                    #
        'first_name':'Rupen',                               #      Ravin,Rakholiya,22
        'last_name':'Rakholiya1',                           #
        'age':19                                            #      Rupen,Rakholiya1,19
    })





# we are getting space between two line in output, and we can address this issue using newline=''

from csv import DictWriter                            # when we use dictwrite we have to show header(colum_name) in code
with open("file3.csv",'w',newline='') as wf:                     # file3.csv is empty
    csv_write=DictWriter(wf,fieldnames=['first_name','last_name','age'])
    csv_write.writeheader()                                # this method will write header in csv file
                 # here, also two methos for writing in csv 1) writerow    2) wrterows


    # #  1) writerow ----> inside dict
    # csv_write.writerow({
    #     'first_name':'Ravin',
    #     'last_name':'Rakholiya',
    #     'age':22
    # })                                                      # o/p: first_name,last_name,age
    # csv_write.writerow({                                    #      Ravin,Rakholiya,22
    #     'first_name':'Rupen',                               #      Rupen,Rakholiya1,19
    #     'last_name':'Rakholiya1',                           
    #     'age':19                                            
    # })
    
    # 2) writerows -----> inside list inside dict
    csv_write.writerows([{'first_name':'Ravin', 'last_name':'Rakholiya','age':22},
                        {'first_name':'Rupen', 'last_name':'Rakholiya1','age':19}])



# DictWriter is betterthan Writer





# read csv  ---> reader, DictReader
# write csv ---> writer, DictWriter











# Read and Write CSV file simulteneously   -----> read data from one csv and write that data into another csv file

from csv import DictReader,DictWriter
with open('file3.csv','r') as rf:
    with open('file4.csv','w',newline='') as wf:                       # here file3.csv has data and file4.csv was empty
        csv_read=DictReader(rf)
        csv_write=DictWriter(wf,fieldnames=['first_name','last_name','age'])
        csv_write.writeheader()
        for line in csv_read:                                           # o/p: first_name,last_name,age              (in file4.csv for csv.writerow(line))
            # csv_write.writerow(line)                                  #      Ravin,Rakholiya,22
            # ----OR-----                                               #      Rupen,Rakholiya1,19
            fname,lname,age=line['first_name'],line['last_name'],line['age']
            csv_write.writerow({
                'first_name':fname.upper(),                    # o/p: in file4.csv
                'last_name':lname.upper(),                     #      first_name,last_name,age
                'age':age                                      #      RAVIN,RAKHOLIYA,22
            })                                                 #      RUPEN,RAKHOLIYA1,19