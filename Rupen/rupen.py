import random
from csv import DictReader, DictWriter, writer


def print1(i,s):
    s=str(s)
    i=i+s
    writing(i)

def random1(name,l):
    if l==2:
        s=random.randrange(100,999)
        print1(name,s)
    if l==3:
        s=random.randrange(10,99)
        print1(name,s)
    if l==4:
        s=random.randrange(0,99)
        print1(name,s)
    if  l==5 or l==6:
        writing(name)





# count=0
# with open('male.csv',"r") as rf:
#     with open('male1.csv','a',newline="") as wf:
#         csv_reader=DictReader(rf)
#         csv_writer=DictWriter(wf,fieldnames=['names'])
#         csv_writer.writeheader()
#         for names11 in csv_reader:
#             csv_writer.writerow({
#                 'names':f"{names11['name']}"
#             })
#             # count+=1
#             # if(count==9500):
#             #     break








count1=0
def writing(name):
    with open('indianf2.txt','a') as wf:
        wf.write(f'al.add("{name}");\n')
        
with open('set4.csv',"r") as rf:
    csv_reader=DictReader(rf)
    for name in csv_reader:  
        l=len(name['name'])
        random1(name['name'],l)   





# triplets=f6.read().split()
# for i in triplets:
#     l=len(i)
#     random1(i,l)
# f6.close()











