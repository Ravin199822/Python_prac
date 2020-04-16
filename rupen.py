import random
def print1(i,s):
    s=str(s)
    i=i+s
    print(f"al.add('{i}');")

def random1(i,l):
    if l==2:
        s=random.randrange(100,999)
        print1(i,s)
    if l==3:
        s=random.randrange(10,99)
        print1(i,s)
    if l==4:
        s=random.randrange(0,99)
        print1(i,s)
    if  l==5 or l==6:
        print(f"al.add('{i}');")

f6=open('file6.txt')
triplets=f6.read().split()
for i in triplets:
    l=len(i)
    random1(i,l)
f6.close()











