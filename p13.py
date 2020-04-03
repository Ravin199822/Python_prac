# Enumerate() Function


# We use enumerate function with for loop to track position of our item in iterable




# How we can do without enumerate function
names=['Ravin','Rupen','Yash','Chirag','Dhara','Trupti']            # o/p: 0------>Ravin
pos=0                                                               #      1------>Rupen 
for name in names:                                                  #      2------>Yash  
    print(f"{pos}------>{name}")                                    #      3------>Chirag
    pos+=1                                                          #      4------>Dhara
                                                                    #      5------>Trupti 
                                        




# With Enumerate Function                                       # o/p: 0------>Ravin
                                                                #      1------>Rupen
for pos1,name1 in enumerate(names):                             #      2------>Yash
    print(f"{pos1}------>{name1}")                              #      3------>Chirag
                                                                #      4------>Dhara
                                                                #      5------>Trupti                                            






# Define a function that two arguments
# 1.) list containing string
# 2.) string that want to find in your list
# and this function will return the index of String in your list and 
# if String is not present then return -1


def fun_enum(list1,string1):
    for pos,name in enumerate(list1):
        if name==string1:
            return pos
    return -1                                         # o/p: Enter name:
                                                      #      Yash
s=input("Enter name:\n")                              #      2
print(fun_enum(names,s))





















# MAP function  
numbers=[1,2,3,4,5]

def square1(a):
    return a**2


# simple method
l1=[]
for i in numbers:
    l1.append(square1(i))
print(l1)                                 # o/p: [1, 4, 9, 16, 25]


# OR  ( using map function)              map(method_name,list_name)

print(map(square1,numbers))               # o/p: <map object at 0x00DE9238>
print(list(map(square1,numbers)))         # o/p: [1, 4, 9, 16, 25]

# OR ( using map and lambda function)           lambda parameters:operation

print(list(map(lambda s:s**2, numbers)))  # o/p: [1, 4, 9, 16, 25]

# OR  ( using list comprehension)          [append_with_list loop]

print([i**2 for i in numbers])            # o/p: [1, 4, 9, 16, 25]






l2=['abc','abcd','abcde']
length=map(len,l2)                        # o/p: 3
for i in length:                          #      4
    print(i)                              #      5


length1=list(map(len,l2))
print(length1)                            # o/p: [3, 4, 5]