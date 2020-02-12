# Tuple

#it is also data structure
#it can store any data type
#but it is immutable, that means we can not update tuple
#data inside tuple
#tuple are faster than lists

example=("one","two","three")
#no-append   no-insert    no-pop   no-remove

#methods
#count, index
#len function
#Slicing


print(example[:2])    #o/p:('one', 'two')

# example[0]=1
# print(example)#Error


#looping in tuple                    #o/p:
mixed=(1,2,3,4.0)                    #      1
for i in mixed:                      #      2
    print(i)                         #      3 
   #we can also use while loop       #      4.0

i=0
while i<len(mixed):
    print(mixed[i])
    i+=1



#tuple with one element
mixed=(1,2,3,4.0) 
print(type(mixed))                   #o/p:<class 'tuple'>
mix1=(3)                   #this is not tuple
print(type(mix1))                    #o/p:<class 'int'>
mix2=(3,)                  #if we want to make sinle element tuple, we have to use column after element
print(type(mix2))                    #o/p:<class 'tuple'>
s=("Word")                 #this is not tuple
print(type(s))                       #o/p:<class 'str'>
s1=("words",)
print(type(s1))                      #o/p:<class 'tuple'>






#tuple with out parenthesis
guiter='honda',"hero",'passion'      #we can create tuple without parethesis
print(type(guiter))                       #o/p:<class 'tuple'>



#tuple unpcking
tuple_1='12',"23",'34','45','56'
a,b,c,d,e=tuple_1                     #here we have to take number variables same as a number of elements in tuple
print(a)              #o/p:12
print(b)              #o/p:23
print(c)              #o/p:34
print(d)              #o/p:45
print(e)              #o/p:56






#list inside tuples
tuple_1=("Ravin",["rupen","yash"])
#here we can add remove items from list
tuple_1[1].pop()
print(tuple_1)             #o/p:('Ravin', ['rupen'])
tuple_1[1].append("Me also")
print(tuple_1)             #o/p:('Ravin', ['rupen', 'Me also'])





# some other function
# min(),max(),sum








#function returning two values
def func(a,b):
    add=a+b
    mul=a*b
    return add,mul

print(func(3,4))    #o/p:(7, 12)
#or
add1,multi=func(3,4)
print(add1)          #o/p:7
print(multi)         #o/p:12






#something more about tuple, list, string
nums=tuple(range(1,11))
print(nums)                          #o/p:(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
nu_list=list(range(1,11))
print(nu_list)                       #o/p:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nu_string=str((1,2,3,4,5,6,7,8,9,10))
print(nu_string)                     #o/p:(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(type(nu_string))               #o/p:<class 'str'>

