# Decorators

# you have to have complete understanding of functions,
# first class function/closures
# then finally we will learn about decorators


def square(a):
    return a**2

print(square(4))                       # o/p: 16
s=square
print(s(7))                            # o/p: 49
print(s.__name__)                      # o/p: square
print(square.__name__)                 # o/p: square
print(s)                               # o/p: <function square at 0x02C2F2B0>
print(square)                          # o/p: <function square at 0x02C2F2B0>





# pass function as argument
l=[1,2,3,4]
print(list(map(square,l)))             # o/p: [1, 4, 9, 16]
print(list(map(lambda a:a**2,l)))      # o/p: [1, 4, 9, 16]


def my_map(func, l):
    new_list=[]
    for i in l:
        new_list.append(func(i))
    return new_list

print(my_map(square,l))                # o/p: [1, 4, 9, 16]
print(my_map(lambda a:a**2, l))        # o/p: [1, 4, 9, 16]


def my_map2(func,l):
    return[func(i) for i in l]

print(my_map(lambda a:a**2,l))         # o/p: [1, 4, 9, 16]