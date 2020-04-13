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























# Raise Example 2

class Mobile:
    def __init__(self, name):
        self.name=name

class MobileStore:
    def __init__(self):
        self.mobiles=[]

    def add_mobile(self, new_mobile):
        self.mobiles.append(new_mobile)


oneplus=Mobile("oneplus")
samsung="Samsung Galaxy s10"
mobostore=MobileStore()
print(mobostore.mobiles)                             # o/p: []
mobostore.add_mobile(samsung)
print(mobostore.mobiles)                             # o/p: ['Samsung Galaxy s10']

# here, i don't want to store any other string which are not in Mobile's object store in mobiles list. I mean i want that the string which are present in Mobile's obj store in mobiles's list.








class Mobile1:
    def __init__(self, name):
        self.name=name

class MobileStore1:
    def __init__(self):
        self.mobiles1=[]

    def add_mobile(self, new_mobile):
        if isinstance(new_mobile,Mobile1):
            self.mobiles1.append(new_mobile)
        else:
            raise TypeError("new_mobile should be object of mobile class")

oneplus1=Mobile1("oneplus")
samsung1="Samsung Galaxy s10"
mobostore1=MobileStore1()
# mobostore1.add_mobile(samsung1)                       # o/p: TypeError: new_mobile should be object of mobile class
# print(mobostore1.mobiles1)                          
mobostore1.add_mobile(oneplus1)
print(mobostore1.mobiles1)                           # o/p: [<__main__.Mobile1 object at 0x034F9820>]
mobo_phones=mobostore1.mobiles1
print(mobo_phones[0].name)                           # o/p: oneplus
# or
print(mobostore1.mobiles1[0].name)                   # o/p: oneplus












# Exception Handling
# try except else finally



# Exception is the error which comes at time of execution


# try except
while True:
    try:
        age=int(input('Enter your age:\n'))
        break
    except ValueError:
        print("Maybe you entered string insted of number, try again")
    except:
        print("unexpected error......")
if age<18:
    print("you can't play this game")
else:
    print("you can play this game")










# else finally clause
while True:
    try:
        number=int(input('Enter your age:\n'))
        print(f"user input : {number}")                               
        break
    except ValueError:
        print("Please type integer !!!")
    except:
        print("unexpected error......")
                                                                              





while True:
    try:
        number=int(input('Enter your age:\n'))
    except ValueError:
        print("Please type integer !!!")
    except:
        print("unexpected error......")
    else:                                                    # this block will run when try block will run successfully, without exception
        print(f"user input : {number}")                      # else is used to increase the redability of code                     
        break
    finally:
        print("Finally block......")

# o/p:                                               # o/p:
# Enter your age:                                    # Enter your age:
# d                                                  # 2
# Please type integer !!!                            # user input : 2
# Finally block......                                # Finally block......                                                
                                                       
                                                        
                                                        












# Excercise 1

# make a function 'divide'
# divide(a,b)


def divide(a,b):
    try:
        c=0
        c=a/b
    except ZeroDivisionError:
        print("please don't divide by Zero")
    except TypeError:
        print("Please input numbers only")
    else:
        return c
    

print(divide(4,2))                          # o/p: 2.0
print(divide(4,0))                          # o/p: please don't divide by Zero
print(divide('4',2))                        # o/p: Please input numbers only
print(divide(4,'2'))                        # o/p: Please input numbers only

        













# Custom Exception

# Q - why custom exception?
# A - to increase the redability of code 




def validate(name):
    if len(name)<8:
        raise ValueError("name is too short")

user_name=input("Enter name:\n")
validate(user_name)
print(f"hello {user_name}")

# o/p:
# Enter name:
# sd
# ValueError: name is too short



#  make our own exception(custom exception)
class NameTooShortError(ValueError):
    pass

def validate1(name):
    if len(name)<8:
        raise NameTooShortError("name is too short")

user_name1=input("Enter name:\n")
validate1(user_name1)
print(f"hello {user_name1}")

# o/p:
# Enter name:
# as
# __main__.NameTooShortError: name is too short