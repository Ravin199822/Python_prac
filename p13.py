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













# Filter() Function


def is_even(a):
    return a%2==0

numbers=[3,2,4,7,9,8,0,6,1]

evens=filter(is_even,numbers)
print(evens)                # o/p: <filter object at 0x032F92B0>

for i in evens:             # o/p: 2
    print(i)                #      4
                            #      8
                            #      0
                            #      6
                
for i in evens:
    print(i)            # o/p: no output

# Note: map and filter can be iterated one time only. iterator many times possible in list and tuple but only one time in map and filter.





                            
evens1=tuple(filter(is_even,numbers))
print(evens1)               # o/p: (2, 4, 8, 0, 6)

evens1=list(filter(is_even,numbers))
print(evens1)               # o/p: [2, 4, 8, 0, 6]


evens3=filter(lambda a:a%2==0,numbers)
print(evens3)               # o/p: <filter object at 0x035F9298>
print(tuple(filter(lambda a:a%2==0,numbers)))         # o/p: (2, 4, 8, 0, 6)


print([i for i in numbers if i%2==0])                 # o/p: [2, 4, 8, 0, 6]















# Iterator vs Iterables 
 
numbers1=[1,2,3,4,5]                 # iterables  (list, tuple, String)
square2=map(lambda a:a**2,numbers1)  # Iterator

print(square2)                       # o/p: <map object at 0x02B99310>

# for i in square2:                    # o/p: 1
#     print(i)                         #      4
#                                      #      9
#                                      #      16
#                                      #      25




# for i in numbers1:
#     print(i)

# How for loop works
# Steps
# call iter function
# iter(numbers)-----> iterator
# next(iter(numbers))


# here, we have to use iter func------> iterables
number_iter=iter(numbers1)
# print(number_iter)                         # o/p: <list_iterator object at 0x030D9328>
# print(next(number_iter))                   # o/p: 1
# print(next(number_iter))                   # o/p: 2
# print(next(number_iter))                   # o/p: 3
# print(next(number_iter))                   # o/p: 4
# print(next(number_iter))                   # o/p: 5
# print(next(number_iter))                   # o/p: Error (StopIteration)



# # Here we don't need to use iter func----->iterator
# print(next(square2))                         # o/p: 1
# print(next(square2))                         # o/p: 4
# print(next(square2))                         # o/p: 9
# print(next(square2))                         # o/p: 16
# print(next(square2))                         # o/p: 25
# print(next(square2))                         # o/p: Error (StopIteration)
















# Zip() function (we can use this function when we want to combine two different list together)
user_id=["user_1","User_2","user_3"]
names3=["Ravin","Rupen","Yash"]
print(zip(user_id,names3))                  # o/p: <zip object at 0x011C2F48>
print(list(zip(user_id,names3)))            # o/p: [('user_1', 'Ravin'), ('User_2', 'Rupen'), ('user_3', 'Yash')]
print(tuple(zip(user_id,names3)))           # o/p: (('user_1', 'Ravin'), ('User_2', 'Rupen'), ('user_3', 'Yash'))
print(dict(zip(user_id,names3)))            # o/p: {'user_1': 'Ravin', 'User_2': 'Rupen', 'user_3': 'Yash'}


user_id1=["user_1","User_2"]
names4=["Ravin","Rupen","Yash"]
print(list(zip(user_id1,names4)))          # o/p: [('user_1', 'Ravin'), ('User_2', 'Rupen')]
print(dict(zip(user_id1,names4)))          # o/p: {'user_1': 'Ravin', 'User_2': 'Rupen'}


Example=[('a',1),('b',2)]
print(dict(Example))                      # o/p: {'a': 1, 'b': 2}




l_name=["Rakholiya","Patel","Gami"]
print(list(zip(user_id,names3,l_name)))  # o/p: [('user_1', 'Ravin', 'Rakholiya'), ('User_2', 'Rupen', 'Patel'), ('user_3', 'Yash', 'Gami')]
print(dict(zip(user_id,names3,l_name)))  # o/p: Error