# Generators

# generators are iterators

# Iterator and iterable

# iterable
l=[1,2,3] # iterable---->list, tuple, string

# for i in l:
#     print(i)

i=iter(l)           # when for loop run first time, it convert list in iterator by using iter function, and then we have to use next function
print(next(i))      # o/p: 1
print(next(i))      # o/p: 2
print(next(i))      # o/p: 3

# we can change iterable in iterator and qw can do work as for loop.

# iterator
s=map(lambda s:s**2,l)  # it is iterator
print(s)             # o/p: <map object at 0x01639268>           # here, we are getting location as output because map is not converted in list.
# map function is also iterator so we don't need to convert in iterator using iter() function. hence, we can directly apply next() function.
print(next(s))       # o/p: 1
print(next(s))       # o/p: 4
print(next(s))       # o/p: 9

for num in map(lambda s:s**2,l):           # we can apply for loop in iterator and iterable both.
    print(num)

# o/p: 1
#      4
#      9








# generator

# generator is sequence as list but it is not iterable, in fact it is iterator.



# why should we use generator?

# 1).  -----In List---
#      [.............many numbers........]-----> this huge list will be stored in my memory
#     this process will take time because, firstly list will create, and then it will be stored in memory. as a result this process will consume time and memory both.
# 
# 2). -----In generator-----
#       one number generate at a time in memory, and when second number will generate, first number will go outside(delete). (3) or (5), (9)......
#     As a result we can save our memory and time.


# when we have to use our sequence many times, we should use list, 
# while, we have to use our sequence only for one time, we can use generator. because in generator our sequence is not stred in memore while in list, the sequence stored in memory.








# create first generator with generator function
# we can create generator by using
# 1). generator function
# 2). generstor comprehension


# generator function

def nums(n):
    for i in range(1,n+1):
        print(i)
    
nums(10)
# o/p: 1
#      2
#      3
#      4
#      5
#      6
#      7
#      8
#      9
#      10



# we can create generator by using yield keyword
def nums1(n):
    for i in range(1,n+1):
        # yield(i)                          # yield is a keyword so you don't have to write i in parenthesis because it's not a function, I mean you can also write as 'yield i' instead of 'yiels(i)' 
        yield i
nums1(10)                    # o/p: 
print(nums1(10))             # o/p: <generator object nums1 at 0x03A10E98>


for i in nums1(10):
    print(i)

# o/p: 1
#      2
#      3
#      4
#      5
#      6
#      7
#      8
#      9
#      10
j=nums1(10)                                    # if i will convert this in list like j=list(nums1(10)) i will  get output in both below for loop., and j=list(nums1(10)) will also loss the featurs of generator because it has become list.
for i in j:              
    print(i)            # o/p: no 1 to 10

for i in j:
    print(i)            # o/p:                     here is no output because nums1() is generator, hence we can can use value only one time.
