# Built-in Errors
# Exception, How to handle them
# raise your own errors, debugging, etc etc






# Built-in Errors

# syntax error ---> made some kind of illegality in syntax
# Indentation Error ---> related to space after loop, function, class, collon
                        # def rav():
                        #     print("fd")
                        #    print("sf")     # indentation error
# name error ---> it happens when we use things(variable, method,....)  which is not defined
# type error ----> print(5+"af")
print(5*"af")                       # o/p: afafafafaf
# Index Error
                        # l=[1,2,3]
                        # print(l[3])        # index error
# Value Error
                        # s="abc"
                        # print(int(s))
# Attribute Error
                        # l=[1,2,3]
                        # l.push(4)          # here i am getting attribute error because list has not push method.
# Key Error
                        # d={'name':'Rakholiya'}
                        # print(d['age'])                  # key error










# Raise Errors
def add(a,b):
    return a+b

print(add(2,3))                      # o/p: 5
print(add('2','3'))                  # o/p: 23



def add1(a,b):
    if (type(a) is int) and (type(b) is int):
        return a+b
    return "OOPS you are passing wrong data type to function"

print(add1(2,3))                      # o/p: 5
print(add1('2','3'))                  # o/p: OOPS you are passing wrong data type to function





def add2(a,b):
    if (type(a) is int) and (type(b) is int):
        return a+b
    raise TypeError("OOPS you are passing wrong data type to function")                   # here,we can raise any error, like we can write valueError instead of typr error


print(add2(2,3))                      # o/p: 5
# print(add2('2','3'))                  # o/p: TypeError: OOPS you are passing wrong data type to function


# def add2(a,b):
#     if (type(a) is int) and (type(b) is int):
#         return a+b
#     raise ValueError("OOPS you are passing wrong data type to function")                   

# print(add2(2,3))                      # o/p: 5
# print(add2('2','3'))                  # o/p: ValueError: OOPS you are passing wrong data type to function









# Raise errors example 1
# NotImplementedError                   # we raise this error when we use inheritance in oop 
# abstract method



class Animal:
    def __init__(self,name):
        self.name=name
    
    def sound(self):
        return "this is animal sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed=breed

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed=breed
        

doggy=Dog("boony",'pug')
print(doggy.sound())                     # o/p: this is animal sound





class Animal1:
    def __init__(self,name):
        self.name=name
    
    def sound(self):
        return "meao meao"

class Dog1(Animal1):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed=breed

class Cat1(Animal1):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed=breed

doggy=Dog1("boony",'pug')
print(doggy.sound())                       # o/p: meao meao              # this sound comes on dog object that i don't want,
# but i want that class which inherit animal class define sound method, otherwise i should be got raise Error----> it is called NotImplementedError










# class Animal2:
#     def __init__(self,name):
#         self.name=name
    
#     def sound(self):
#         raise NotImplementedError('you have to define this method in subclasses')

# class Dog2(Animal2):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed=breed

# class Cat2(Animal2):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed=breed

# doggy=Dog2("boony",'pug')
# print(doggy.sound())                        # o/p: NotImplementedError: you have to define this method in subclasses












class Animal3:
    def __init__(self,name):
        self.name=name
    
    def sound(self):                                        # abstract method
        raise NotImplementedError('you have to define this method in subclasses')

class Dog3(Animal3):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed=breed

    def sound(self):
        return "bhow bhow"

class Cat3(Animal3):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed=breed

    def sound(self):
        return "meao meao"

doggy=Dog3("boony",'pug')
print(doggy.sound())                 # o/p: bhow bhow   



