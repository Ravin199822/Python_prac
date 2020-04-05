# *args or *operator




def sum_num(a,b):
    return a+b

print(sum_num(3,4))                      # o/p: 7
# print(sum_num(2,3,4))                   # o/p: Type Error            -----> we can not pass more than two argument in sum_num function. we can overcome this problem by using *args (here we can use * with anyone like *abd, *asd anything)




def num_sum(*args):
    print(args)                         # o/p: (1, 2, 3, 4, 5)
    print(type(args))                   # o/p: <class 'tuple'>


num_sum(1,2,3,4,5)









def num_sum1(*args):
    total=0
    for num in args:
        total+=num
    return total

print(num_sum1(1,2,3,4,5))               # o/p: 15 













# *args with normal parameter
def mul_args(*args):
    mul=1
    for i in args:
        mul*=i
    return mul

print(mul_args(2,3,4,5))             # o/p: 120









def mul_args1(num, *args):
    mul=1
    for i in args:
        mul*=i
    return mul

print(mul_args1(2,3,4,5))                         # o/p: 60








# def mul_args2(num, *args):
#     mul=1
#     for i in args:
#         mul*=i
#     return mul

# print(mul_args2())                         # o/p: type Error










def mul_args3(num, *args):
    mul=1
    print(num)                                    # o/p: 2
    print(args)                                   # o/p: (3, 4, 5)
    for i in args:
        mul*=i
    return mul

print(mul_args3(2,3,4,5))                         # o/p: 60













def mul_args4(num, *args):
    mul=1
    print(num)                                    # o/p: 2
    print(args)                                   # o/p: ()
    for i in args:
        mul*=i
    return mul

print(mul_args4(2))                               #o/p: 1








# def mul_args5(*args, num):
#     mul=1
#     print(num)                                    # o/p: 2
#     print(args)                                   # o/p: (3, 4, 5)
#     for i in args:
#         mul*=i
#     return mul

# print(mul_args5(2,3,4,5))                         # o/p: type error











def mul_args6(*args):
    mul=1
    print(args)                                   # o/p: ([2, 3, 4, 5],)
    for i in args:
        mul*=i
    return mul

l1=[2,3,4,5]
print(mul_args6(l1))                              # o/p: [2, 3, 4, 5]





def mul_args8(*args):
    mul=1
    print(args)                                   # o/p: ((2, 3, 4, 5),)
    for i in args:
        mul*=i
    return mul

l1=(2,3,4,5)
print(mul_args8(l1))                              # o/p: (2, 3, 4, 5)












def mul_args7(*args):
    mul=1
    print(args)                                   # o/p: (2, 3, 4, 5)
    for i in args:
        mul*=i
    return mul

l1=[2,3,4,5]      # or l1=(2,3,4,5)
print(mul_args7(*l1))                             # o/p: 120

















# Excercise 1
def to_power(num, *args):
    if args:
        return [i**num for i in args]
    else:
        return "hey! you didn't pass"

l2=[1,2,3,4,5]
print(to_power(3,*l2))                 # o/p: [1, 8, 27, 64, 125]


















# kwarg----------> keyword arguments
# **kwarg--------> double star operator
# it will gather as a dictionary


# kwarg as a argument
def fun(**kwarg):
    print(type(kwarg))                                           # o/p: <class 'dict'>
    return kwarg

print(fun(first_name='Ravin',last_name='Rakholiya'))             # o/p: {'first_name': 'Ravin', 'last_name': 'Rakholiya'}














def fun1(**kwarg):
    for k,v in kwarg.items():                               # o/p: first_name:Ravin
        print(f"{k}:{v}")                                   # o/p: last_name:Rakholiya
print(fun1(first_name='Ravin',last_name='Rakholiya'))       # o/p: None







# def func(name, **kwarg):
#     print(type(kwarg))                                          
#     return kwarg

# print(func(first_name='Ravin',last_name='Rakholiya'))       # o/p: type error










def func1(name, **kwarg):
    print(type(kwarg))  
    print(name)                                    # o/p: rupen                      
    return kwarg

print(func1('rupen',first_name='Ravin',last_name='Rakholiya'))




def func2(**kwarg):
    return kwarg

d1={'first_name':'Ravin1','last_name':'Rakholiya1'}
print(func2(**d1))                           # o/p: {'first_name': 'Ravin1', 'last_name': 'Rakholiya1'}










# Function with all type of parameters 
# PADK----> parameters, *args, default parameters, **kwargs

# Default parameter
def func3(name="unknown",age=24):     #parameters
    print(f"name : {name} and age : {age}")
    

func3()    #args           # o/p: name : unknown and age : 24
func3("Ravin")             # o/p: name : Ravin and age : 24
func3(22)                  # o/p: name : 22 and age : 24
func3("Rebel",22)          # o/p: name : Rebel and age : 22




# padk
def func4(name,*args,last_name="Rakholiya",**kwargs):
    print(name)                         # o/p: Ravin
    print(args)                         # o/p: (1, 2, 3)
    print(last_name)                    # o/p: Rakholiya
    print(kwargs)                       # o/p: {'a': 'c', 'b': 'd'}  

func4("Ravin", 1,2,3,a='c',b='d')











# Excercise 2
def names(args,**kwargs):
    if kwargs.get('reverse_str')==True:
        return [i[::-1].title() for i in args]
    else:
        return [i.title() for i in args]

name=["ravin",'rupen','yash']
print(names(name))                       # o/p: ['Ravin', 'Rupen', 'Yash']
print(names(name,reverse_str=True))      # o/p: ['Nivar', 'Nepur', 'Hsay'] 