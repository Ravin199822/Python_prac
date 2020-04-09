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

print(my_map2(lambda a:a**2,l))         # o/p: [1, 4, 9, 16]










# Function returning function ---or---   Closures ---or--- first class function


def outer_func():
    def inner_func():
        print("inside inner func")
    return inner_func

print(outer_func())                          # o/p: <function outer_func.<locals>.inner_func at 0x0115F3D0>

var=outer_func()
var()                                        # o/p: inside inner func




def outer_func1(msg):
    def inner_func1():
        print(f"message is : {msg}")
    return inner_func1

var1 = outer_func1("Hi there !")
var1()                                       # o/p: message is : Hi there !




# Function returning function ---or---   Closures ---or--- first class function practice

def to_power(x):
    def cal_power(n):
        return n**x
    return cal_power


squ=to_power(2)                                          # o/p: enter number you want to square:
n=int(input("enter number you want to square:\n"))       #      4
print(squ(n))                                            #      16


cube=to_power(3)                                         # o/p: enter number you want to square:
n1=int(input("enter number you want to cube:\n"))        #      2
print(cube(n1))                                          #      8
















# Decorators------> enhance the functionality of other functions
# decorator is function which enhance the functionality of other functions

# i want to print "this is awesome" when i call func1 or func2 and i don't want to change the code of func1 and func2 

def decorator_function(any_function):
    def wrapper_function():
        print("this is awesome")
        any_function()
    return wrapper_function

def func1():
    print("this is function 1")

def func2():
    print("this is function 2")

func1()                                        # o/p: this is function 1
func2()                                        # o/p: this is function 2

# here we can write func1 instead of var2 and var2()
var2=decorator_function(func1)
var2()                                         # o/p: this is awesome
                                               #      this is function 1
                
func1=decorator_function(func1)
func1()                                         # o/p: this is awesome
                                               #      this is function 1


# here we can write func2 instead of var3 and var3()
var3=decorator_function(func2)                 # o/p: this is awesome
var3()                                         #      this is function 2

func2=decorator_function(func2)                 # o/p: this is awesome
func2()                                         #      this is function 2




# @ -----> use for decorator
def decorator_function1(any_function):
    def wrapper_function():
        print("this is awesome")
        any_function()
    return wrapper_function

@decorator_function1           # shortcut                             
def func11():                                              
    print("this is function 11")                           

@decorator_function1 
def func22():                                              
    print("this is function 22")                           


func11()                                                   # o/p: this is awesome
                                                           #      this is function 11



func22()                                                   # o/p: this is awesome
                                                           #      this is function 22






        # def decorator_function2(any_function):
        #     def wrapper_function():
        #         print("this is awesome")
        #         any_function()                                ## in this function i will get error because func3(4) will call wrapper function which has no parameters, as a result i have to face type error.
        #     return wrapper_function                           ## we can solve this proble using *args and **kwarg

        # @decorator_function2                             
        # def func3(a):                                              
        #     print(f"this is function {a}")  

        # func3(4)                                       # o/p: type error               





def decorator_function3(any_function):
    def wrapper_function(*arg,**kwarg):
        print("this is awesome")
        any_function(*arg,**kwarg)
    return wrapper_function

@decorator_function3          # shortcut                             
def func3(a):                                              
    print(f"this is function {a}") 

func3(7)                                        # o/p: this is awesome
                                                #      this is function 7


@decorator_function3
def add(a,b):
    return a+b

add(3,4)                                        # o/p: this is awesome

print(add(3,4))                                 # o/p: None               ------ here, we are getting none as output because in decorator_function3 we simply call any_function(*args,**kwarg), so we have to return any_function to get real output(sum of a and b).

        






# I think this is complete decorator function
def decorator_function4(any_function):
    def wrapper_function(*arg,**kwarg):
        print("this is awesome")
        return any_function(*arg,**kwarg)
    return wrapper_function


@decorator_function4
def add1(a,b):
    return a+b

add1(3,4)                                        # o/p: this is awesome

print(add1(3,4))                                 # o/p: 7




@decorator_function4                                     
def func4(a):                                              
    print(f"this is function {a}") 

func4(10)                                        # o/p: this is awesome
                                                 #      this is function 10



                                        
                                    








def decorator_function5(any_function):
    def wrapper_function(*arg,**kwarg):
        """ This is wrapper function """
        print("this is awesome")
        return any_function(*arg,**kwarg)
    return wrapper_function


@decorator_function5
def add2(a,b):
    ''' this is add function '''
    return a+b

print(add2.__doc__)                             # o/p:  This is wrapper function
print(add2.__name__)                            # o/p: wrapper_function
# here we call add2 function, even though we are getting output of wrapper function
# we can overcome this problem by importing wraps module




# complete decorator function
from functools import wraps
def decorator_function6(any_function):
    @wraps(any_function)
    def wrapper_function(*arg,**kwarg):
        """ This is wrapper function """
        print("this is awesome")
        return any_function(*arg,**kwarg)
    return wrapper_function


@decorator_function6
def add3(a,b):
    ''' this is add function '''
    return a+b

print(add3.__doc__)                             # o/p:  This is add function
print(add3.__name__)                            # o/p: add3













# Decorators practice


from functools import wraps
def print_function_data(function):
    @wraps(function)
    def wrapper_function(*args,**kwarg):
         print(f"you are calling {function.__name__} function")
         print(f"{function.__doc__}")
         return function(*args,**kwarg)
    return wrapper_function


@print_function_data
def add4(a,b):
    ''' This function takes two numbers as argument and return their sum '''
    return a+b

print(add4(4,5))                                       # o/p: you are calling add4 function
                                                       #       This function takes two numbers as argument and return their sum
                                                       #      9









# How to find time which has taken by executing function
import time
t1=time.time()
print("this is line 1")                              # o/p: this is line 1
x=5
if x==5:
    print("x is equal to 5")                         # o/p: x is equal to 5
print("this is line 2")                              # o/p: this is line 2
print("this is line 2")                              # o/p: this is line 2 
print("this is line 2")                              # o/p: this is line 2 
print("this is line 2")                              # o/p: this is line 2 
print("this is line 2")                              # o/p: this is line 2 
print("this is line 2")                              # o/p: this is line 2 
print("this is line 2")                              # o/p: this is line 2 
t2=time.time()
print(t2-t1)                                         # o/p: 0.004003047943115234










# Excercise 1
import time

from functools import wraps
def calculate_time(function1):
    @wraps(function1)
    def wrapper_function1(*args,**kwarg):
        print(f"executing.....{function1.__name__}")
        t11=time.time()
        returned_value=function1(*args,**kwarg)
        t22=time.time()
        ta=t22-t11
        print (f"this function took {ta} to run")
        return returned_value
    return wrapper_function1


@calculate_time
def funct():
    print(f"this is {funct.__name__} function")

funct()                                   # o/p: executing.....funct
                                          #      this is funct function
                                          #      this function took 0.003991842269897461 to run




@calculate_time
def check_square1(n1):
    return [i**2 for i in range(1,n1+1)]

check_square1(1000)                      # o/p: executing.....check_square
                                         #      this function took 0.003998756408691406 to run














# Decorator practice 2
def add_all(*args):
    total=0
    for i in args:
        total+=i
    return total

print(add_all(1,2,3,4,5))                       # o/p: 15
# print(add_all(1,2,3,4,5,[1,2,3]))               # o/p: Error -------> we can dismiss this error by using decorator


from functools import wraps
def only_int_allow(funct1):
    @wraps(funct1)
    def inner_funct(*args,**kwarg):
        # data_list=[]
        # for i in args:
        #     data_list.append(type(i)==int)
        # if all(data_list):
        #     return (funct1(*args,**kwarg))
        # else:
        #     return "Invalid arguments"
        if all([type(i)==int for i in args]):
            return (funct1(*args,**kwarg))
        return "Invalid arguments"
    return inner_funct


@only_int_allow
def add_all1(*args):
    total=0
    for i in args:
        total+=i
    return total

print(add_all1(1,2,3,4,5))                       # o/p: 15
print(add_all1(1,2,3,4,5,[1,2,3]))               # o/p: Invalid arguments














# Decorator with arguments

from functools import wraps
def only_data_type_allow(data_type):
    def decorator1(function11):
        @wraps(function11)
        def wrapper1(*args,**kwarg):
            if all([type(i)==data_type for i in args]):
                return function11(*args,**kwarg)
            return "Invalid input"
        return wrapper1
    return decorator1


@only_data_type_allow(str)
def string_join(*args):
    s=""
    for i in args:
        s+=i
    return s


print(string_join('Ravin ','Rakholiya'))                # o/p: Ravin Rakholiya        
print(string_join('Ravin ','Rakholiya',8))              # o/p: Invalid input     