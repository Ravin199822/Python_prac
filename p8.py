# SET

# set data type
# unordered collection of unique items
# not indexing




s={1,2,3,2}
print(s)        # o/p: {1, 2, 3}
# print(s[1])     # o/p: Error




# remove duplicates.....and.....convert list in sets
l=[1,2,2,3,4,4,4,4,4,5,5,5,6,7,7,7,8,8,8,8,8,9,0,0,0]
s1=set(l)
print(s1)                # o/p: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}


# convert set to list
l1=list(s1)
print(l1)               # o/p: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# add item in set
s.add(4)
print(s)                # o/p: {1, 2, 3, 4}
s.add(5)
s.add(4)
print(s)                # o/p: {1, 2, 3, 4, 5}



# remove item from set  ( here, when we will face error in remove method, where we can use discard() method to ignore error. Aside from that, when we discard the value which is not in set we will not face error)
s.remove(3)
print(s)                # o/p: {1, 2, 4, 5}

s.discard(4)
print(s)                # o/p: {1, 2, 5}
s.discard(8)            
print(s)                # o/p: {1, 2, 5}




# # clear() method    (Remove all elements from the set)
# s.clear()
# print(s)      # o/p: set()



# copy method
sc=s.copy()
print(sc)       # o/p: {1, 2, 5}




s3={1,1.0,2.0,3.5,"Ravin"}
print(s3)       # o/p: {1, 2.0, 3.5, 'Ravin'}





# # we can not store list and dictionary inside the set
# s4={1,2,2,3,[4,3,5]}
# print(s4)                     # o/p: Error
# s5={1,2,2,3,{'name':'Ravin','age':22}}
# print(s5)                     # o/p: Error








# In keyword in sets and for loop
s6={'a','b','c','d'}


if 'a' in s6:
    print('present')
else:                                         # o/p: present
    print('not present')




if 's' in s6:
    print('present')
else:                                         # o/p: not present
    print('not present')



# for loop
for item in s6:
    print(item)                          
# o/p: c                 (order of the output's item always change)
#      d
#      a
#      b









# set maths
a1={1,2,3,4}
a2={3,4,5,6}


# Union of sets              ( here we have to use pipe '|' )
union_set=a1|a2
print(union_set)                 # o/p: {1, 2, 3, 4, 5, 6}


# intersection of sets       ( here we have to use and '&' )
intesection_set=a1&a2
print(intesection_set)           # o/p: {3, 4}





