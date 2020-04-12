# Object Oriented Programming

# common topic in almost all popular programming languages (PYTHON, C++, JAVA) with common idea but with different syntax

# oop is just a style/way to write a code

# very helpful in creating real world programs

# we will see other advantages when we will start learning loop



# class, object(instance), method



# list class
# list object
# method


l=[1,2,3]
l2=[4,5,6]
l3=['Ravin',' Rakholiya']
l.append(8)









# create your first class

# OBJECTIVES
# WHAT IS CLASS
# WHAT IS INIT METHOD --or-- constructor
# WHAT ARE INIT METHOD, INSTANCE VARIABLES
# HOW TO CREATE OUR OBJECT




class Person:
    def __init__(self, first_name, last_name, age):                      # it is called as init method or constructor
        # instance variable                                              # self represents object like p1 and p2
        self.first_name=first_name                                       # whenever we call init method, self should be first argument. and self represents our object.
        self.last_name=last_name
        self.age=age

p1=Person("Ravinkumar","Rakholiya",22)
p2=Person("Rupenkumar","Rakholiya1",19)

print(p1.first_name)                           # o/p: Ravinkumar
print(p2.first_name)                           # o/p: Rupenkumar







class Person11:
    def __init__(self, first_name, last_name, age):
        # instance variables
        print("init method // constructor get called")  
        self.first_name=first_name                                       
        self.last_name=last_name
        self.age=age

p1=Person11("Ravinkumar","Rakholiya",22)                          # o/p: init method // constructor get called


p1=Person11("Ravinkumar","Rakholiya",22)                      # init method called when we create object.   
p2=Person11("Rupenkumar","Rakholiya1",19)
# o/p: init method // constructor get called
#      init method // constructor get called








# class Person111:
#     def __init__(person_obj, first_name, last_name, age):
#         # instance variables
#         person_obj.person_first_name=first_name                       # person_first_name----> instance variable                                     
#         person_obj.last_name=last_name
#         person_obj.age=age

# p1=Person111("Ravinkumar","Rakholiya",22) 
# print(p1.person_first_name)                                 # o/p: Ravinkumar














# Excercise 1

# create class laptop with attributes like brand name, model name, price
# create two objects/instance of your laptop class


class Laptop:
    def __init__(self, brand_name, model_name, price):
        # instance variable
        self.brand_name=brand_name
        self.name=model_name
        self.price=price                                        # we can create more instance variable
        self.laptop1=brand_name+" "+model_name
    
lp1=Laptop("Dell","inspire 5558",52500)
lp2=Laptop("HP","micro 1355",48000) 

print(lp1.name)                                                 # o/p: inspire 5558
print(lp1.laptop1)                                              # o/p: Dell inspire 5558












# in python, the all functions which are inside the class called as function.




# Instance method
l1=[1,2,3]                               # here, l1 is instance of List class, means l1 is object of our List class


class Person1:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def is_above_18(self):
        return True if self.age>18 else False
        # or return self.age>18
    

p1=Person1("Ravin","Rakholiya",22)
p2=Person1("Rupen","Rakholiya",17)
print(p1.full_name())                             # o/p: Ravin Rakholiya
print(p2.full_name())                             # o/p: Rupen Rakholiya
print(Person1.full_name(p2))                      # o/p: Rupen Rakholiya

# p2.full_name()=Person1.full_name(p2)




print(p1.is_above_18())                      # o/p: True
print(Person1.is_above_18(p1))               # o/p: True

print(p2.is_above_18())                      # o/p: False
print(Person1.is_above_18(p2))               # o/p: False





l4=[1,2,3]
l5=[1,2,3]
# clear, pop
l4.clear()
print(l4)                                     # o/p: []
list.clear(l5)
print(l5)                                     # o/p: []

# append
l4.append(10)
print(l4)                                     # o/p: [10]
list.append(l4,20)
print(l4)                                     # o/p: [10, 20]














# Excercise 2
class Laptop1:
    def __init__(self, brand_name, model_name, price):
        # instance variable
        self.brand_name=brand_name
        self.name=model_name
        self.price=price                                       
        
    def laptop_discount(self,disc):
        a=(self.price*disc)/100
        return self.price-a

lp1=Laptop1("Dell","inspire 5558",52500)
n=int(input("Enter percentage for discount\n"))
print(lp1.laptop_discount(n))















# Class Variable


# class---->circle
# method---> area, circum

class Circle:
    def __init__(self, radius, pi):
        self.radius=radius
        self.pi=pi
    
    def circum_cir(self):
        return 2*self.pi*self.radius
    
    def area_cir(self):
        return self.pi*(self.radius**2)

c=Circle(4,3.14)
c1=Circle(6,3.14)
print(c.circum_cir())                                  # o/p: 25.12
print(c1.area_cir())                                   # o/p: 113.04

# here are two problems
# 1). we write pi value 3.14 when we create object, like in above case we made two object, hence we have to write 3.14 two times.....2). as a result 3.14 store in memory for each objects, so it will take more space, which is reason of memory wastage.






class Circle1:
    pi = 3.14                                 # class variable
    def __init__(self, radius):
        self.radius=radius
    
    def circum_cir(self):
        return 2*Circle1.pi*self.radius        # we can use class variable like class_name.class_variable_name
    
    def area_cir(self):
        return Circle1.pi*(self.radius**2)

c2=Circle1(4)
c3=Circle1(6)
print(c2.circum_cir())                                  # o/p: 25.12
print(c3.area_cir())                                    # o/p: 113.04









class Laptop2:
    lap_disc=10
    def __init__(self, brand_name, model_name, price):
        # instance variable
        self.brand_name=brand_name
        self.name=model_name
        self.price=price                                       
        
    def laptop_discount(self):
        a=(self.price*Laptop2.lap_disc)/100
        return self.price-a

lp3=Laptop2("Dell","inspire 5558",52500)
lp4=Laptop2("Hp","inspire 5558",50000)
print(lp3.laptop_discount())                            # o/p: 47250.0
print(lp4.laptop_discount())                            # o/p: 45000.0








class Laptop3:
    lap_disc1=10
    def __init__(self, brand_name, model_name, price):
        # instance variable
        self.brand_name=brand_name
        self.name=model_name
        self.price=price                                       
        
    def laptop_discount(self):
        a=(self.price*Laptop3.lap_disc1)/100
        return self.price-a


Laptop3.lap_disc1=0
lp5=Laptop3("Dell","inspire 5558",52500)
lp6=Laptop3("Hp","inspire 5558",50000)
print(lp5.laptop_discount())                            # o/p: 52500.0
print(lp6.laptop_discount())                            # o/p: 50000.0


# how can we see, object has which variables
print(lp5.__dict__)                              # o/p: {'brand_name': 'Dell', 'name': 'inspire 5558', 'price': 52500}
print(lp6.__dict__)                              # o/p: {'brand_name': 'Hp', 'name': 'inspire 5558', 'price': 50000}


# here, if we want to apply discount 30 for only Hp's laptop so....
lp6.lap_disc1=30
print(lp6.laptop_discount())                     # o/p: 45000.0              the output took disc=10 , so we can not get right answer using this method




class Laptop4:
    lap_disc2=10
    def __init__(self, brand_name, model_name, price):
        # instance variable
        self.brand_name=brand_name
        self.name=model_name
        self.price=price                                       
        
    def laptop_discount(self):
        a=(self.price*self.lap_disc2)/100
        return self.price-a


lp7=Laptop4("Dell","inspire 5558",52500)
lp8=Laptop4("Hp","inspire 5558",50000)
lp8.lap_disc2=30
print(lp8.laptop_discount())                                    # o/p: 35000.0            this is right answer   dic=30 for hp
print(lp7.laptop_discount())                                    # o/p: 47250.0            this is right answer   dic=10 for dell















# Excercise 3

class Person2:
    count_instance=0
    def __init__(self, first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        # self.count_instance+=1                               # here we will get 0 as out put because we have to take class variables by class name
        Person2.count_instance+=1
    
p21=Person2("Ravin","Rakholiya")
p22=Person2("Ravin1","Rakholiya1")

print(Person2.count_instance)                             # o/p: 2















# class Methods

# difference between class method and instance method

# class variable = class attribute




class Person3:
    count_instance=0             # class variable --or-- class attribute              ------> same for all objects of the class, we can call class variable by using class name with . operator
    def __init__(self, first_name, last_name, age):                 # instance method
        Person3.count_instance+=1
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

    @classmethod                              # declaring class method
    def instance_count(cls):
        return f"you have created {cls.count_instance} instances in {cls.__name__} class"              # here we can write Person3.count_instance  and Person3.__name__   insted of cls.count_instance and cls.__name__

    def full_name(self):                                            # instance method   
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):                                          # insatnce method      -------i can use instance method with instance(p31,p32) of the class
        return self.age>18

p31=Person3("Ravin","Rakholiya",10)
p32=Person3("Rupen","Rakholiya1",19)
print(Person3.instance_count())          # calling class method     # o/p: you have created 2 instances in Person3 class       # this thing, we can access by using instance name.
print(p31.instance_count())                                         # o/p: you have created 2 instances in Person3 class       # but we should not do this

# in instance method first argument is object(self), while in class method the first argument is class














# class methods as a constructors

# when we create out instance(object), its call init method which is counstructor
# but here, we want to create object in different way, which calls class method and would be constructor for that instance

class Person4:
    count_instance=0             
    def __init__(self, first_name, last_name, age):                 
        Person3.count_instance+=1
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

    @classmethod                             
    def instance_count(cls):
        return f"you have created {cls.count_instance} instances in {cls.__name__} class" 

    @classmethod
    def from_string(cls,string):
        first,last,age=string.split(',')    
        return cls(first,last,int(age))         

    def full_name(self):                                               
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):                                          
        return self.age>18

p41=Person4("Ravin","Rakholiya",10)
p42=Person4("Rupen","Rakholiya1",19)

p43=Person4.from_string('Yash,Rakholiya2,20')
print(p43.full_name())                  # o/p: Yash Rakholiya2
print(p43.is_above_18())                # o/p: True















# Static Method

# class method related with our class
# instance method related with our instance
# but static method is not related with our class and instance
# static method is like our normal function 
# static method has logical relation with our class
# we can create static method by using static method decorator


class Person5:
    count_instance=0             
    def __init__(self, first_name, last_name, age):                 
        Person3.count_instance+=1
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

    @classmethod                             
    def instance_count(cls):
        return f"you have created {cls.count_instance} instances in {cls.__name__} class" 

    @classmethod
    def from_string(cls,string):               # cls represents our class
        first,last,age=string.split(',')    
        return cls(first,last,int(age))       

    @staticmethod                                # creating static method
    def hello():
        print('hello, static method called')  

    def full_name(self):                       # self represents out instance                            
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):                                          
        return self.age>18

p51=Person5("Ravin","Rakholiya",10) 
p52=Person5("Rupen","Rakholiya1",19)
Person5.hello()          # calling static method                # o/p: hello, static method called















# Encapsulation                   ----encapulate data in class (encaptulate methodas data in a class)
# Abstraction                     ----hide the complexity   (method hide main logic)
# Some special Naming Conventions ----show as private for developer, but not private
# Name Mangling                   ---- __name  (not a convention)
 

class Phone:
    def __init__(self, brand, model_name, price):
        self.brand=brand
        self.model_name=model_name
        # self._price=price
        self.__price=price

    def make_a_call(self, phone_number):
        print(f"calling {phone_number}.......")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def send_message(self):
        pass    #twilio



l=[4,2,7,1,5]
l.sort()            # python use tim sort for sorting, hide complexity
print(l)                 # o/p: [1, 2, 4, 5, 7]

# with out encapsulation, abstraction is not possible.


# convention
# in python, everything is public.

# '_' (underscore) is convention------> we use this because, i can say to other developer that don't make changes in it and treat as private method because it is private. but you know it is not private, anyone can make changes in it

# _name  ---> convention of private name
# __name__   ----> it is called by double underscorw method, or  dunder, or  magic method


phone1=Phone('nokia','1100',1000)
# print(phone1._price)                    # o/p: 1000
# phone1._price=-1000
# print(phone1._price)                    # o/p: -1000


# Name mangling ----> _classname__attributename
# print(phone1.__price)                   # o/p: AttributeError: 'Phone' object has no attribute '__price'
print(phone1.__dict__)                  # o/p: {'brand': 'nokia', 'model_name': '1100', '_Phone__price': 1000}      # here, python changed __price as _Phone__price
print(phone1._Phone__price)             # o/p: 1000
phone1._Phone__price=-1000
print(phone1._Phone__price)             # o/p: -1000

print(phone1.brand)                     # o/p: nokia















# Property, Setter decorator

# will discuss three prblems in existing
# then we will solve them using getter, setter decorator

class Phone1:
    def __init__(self, brand, model_name, price):
        self.brand=brand
        self.model_name=model_name
        self._price=price
        self.complete_specification=f"{self.brand} {self.model_name} and price is {self._price}"


    def make_a_call(self, phone_number):
        print(f"calling {phone_number}.......")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

phone11=Phone1('nokia','1100',1000)                                       # problem 1) here i can enter negative price, which is practically not possible in life, because phone has not negative price
print(phone11.brand)                                     # o/p: nokia
print(phone11.model_name)                                # o/p: 1100
print(phone11._price)                                    # o/p: 1000
print(phone11.complete_specification)                    # o/p: nokia   1100 and price is 1000





print(phone11.brand)                                     # o/p: nokia
print(phone11.model_name)                                # o/p: 1100
phone11._price=500                                                                # problem 3) here we can also set negative price which is not possible for phone in real life
print(phone11._price)                                    # o/p: 500               #  problem 2) price of the phone is updated here but not updated in belove line(complete_specification)
print(phone11.complete_specification)                    # o/p: nokia   1100 and price is 1000


# how can we solve this problems
# we can set price 0 when user add negative price
phone11=Phone1('nokia','1100',1000)          



class Phone2:
    def __init__(self, brand, model_name, price):
        self.brand=brand
        self.model_name=model_name
        # if price>0:
        #     self._price=price
        # else:                                    # solution 1
        #     self._price= 0       ----OR----
        self._price=max(price,0)
        # self.complete_specification=f"{self.brand} {self.model_name} and price is {self._price}"    # solution 2-----> this should not be written here, and make function which return this 

    @property                        # if i use property decorator here, i don;t need to call it as a function
    def complete_specification(self):             # soln 2
        return f"{self.brand} {self.model_name} and price is {self._price}"



    # getter(), setter()      # solution 3
    @property                              # it will return price
    def price1(self):                        # getter method
        return self._price

    @price1.setter
    def price1(self,new_price):              # setter method
        self._price=max(new_price,0)




    def make_a_call(self, phone_number):
        print(f"calling {phone_number}.......")

    def full_name(self):
        return f"{self.brand} {self.model_name}"



#soln 1
phone21=Phone2('nokia','1100',1000) 
phone22=Phone2('nokia','1100',-1000) 
print(phone21._price)                       # o/p: 1000
print(phone22._price)                       # o/p: 0



# soln 2
phone21._price=500
print(phone21._price)                       # o/p: 500         
# print(phone21.complete_specification())     # o/p: nokia 1100 and price is 500              # soln 2   (without property decorator)

print(phone21.complete_specification)       # o/p: nokia 1100 and price is 500




# soln 3
phone21._price=-500
print(phone21._price)                         # o/p: -500
print(phone21.complete_specification)         # o/p: nokia 1100 and price is -500

phone21.price1=-500
print(phone21.price1)                         # o/p: 0
print(phone21.complete_specification)         # o/p: nokia 1100 and price is 0














# Inheritance

class Phone3:                      # base clss/Parent class
    def __init__(self, brand, model_name, price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)


    def make_a_call(self, phone_number):
        print(f"calling {phone_number}.......")

    def full_name(self):
        return f"{self.brand} {self.model_name}"



class Smartphone(Phone3):                      # derived clss/child class
    def __init__(self,  brand, model_name, price, ram, internal_memory, rear_camera):
        #two ways to get parant class varibles

        # Phone3.__init__(self, brand, model_name, price)         # 1) uncommon way
        super().__init__(brand, model_name, price)              # 2) common way ----> here we don't need to pass self as argument in super
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera

phone31=Phone3('nokia','1100',1000) 
smartphone=Smartphone("Redmi","Y2",9000,"3 GB","32 GB","16 mpx")
print(phone31.full_name())                         # o/p: nokia 1100
print(smartphone.full_name())                      # o/p: Redmi Y2
print(smartphone.full_name()+f" and price is : {smartphone._price}")             # o/p: Redmi Y2 and price is : 9000































# Can we derive more than one class from base class
# Multilevel inheritane
# Method resolution order  (MRO)
# Method Overriding
# isinstance(), issubclass()



# Can we derive more than one class from base class ----> YES
class Phone4:                # parent class / base class
    def __init__(self, brand, model_name, price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def make_a_call(self,number):
        return f"calling {number}......"

class Smartphone1(Phone4):           # child class / derived class
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        super().__init__(brand, model_name, price)
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera

class Smartphone2(Phone4):           # child class / derived class
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        super().__init__(brand, model_name, price)
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera

smartphone1=Smartphone2("Samsung","s10",50000,"8 GB","64 GB","32 mpx")
print(smartphone1.full_name())                        # o/p: Samsung s10





# Multilevel inheritane
class Phone5:                # parent class / base class
    def __init__(self, brand, model_name, price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def make_a_call(self,number):
        return f"calling {number}......"

class Smartphone3(Phone5):           # child class / derived class
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        super().__init__(brand, model_name, price)
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera

    def my_storage(self):
        return f"Ram is : {self.ram} and Internal storage is : {self.internal_memory}"

class FlagshipPhone(Smartphone3):           
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera, front_camera):
        super().__init__(brand, model_name, price, ram, internal_memory, rear_camera)
        self.front_camera=front_camera
    
p=FlagshipPhone("One+","o1",65000,"12 GB","128 GB","64 mpx","32 mpx")
print(p.full_name())                    # o/p: One+ o1
print(p.my_storage())                   # o/p: Ram is : 12 GB and Internal storage is : 128 GB







# MRO (Metjhod resolution Order)

# every class has method resolution order

# How we can see (print) method resolution order
# print(help(Smartphone3))            
                                        # o/p:  Help on class Smartphone3 in module __main__:

                                        #       class Smartphone3(Phone5)
                                        #       |  Smartphone3(brand, model_name, price, ram, internal_memory, rear_camera)
                                        #       |
                                        #       |  Method resolution order:
                                            #   |      Smartphone3                          .# this is order of python is searching for
                                        #       |      Phone5                                # firstly, python checks in SmartPhone3, then in Phone5 and then object
                                        #       |      builtins.object    # this is master class in python, all classes are inherited from it in Python
                                        #       |
                                        #       |  Methods defined here:
                                        #       |
                                        #       |  __init__(self, brand, model_name, price, ram, internal_memory, rear_camera)
                                        #       |      Initialize self.  See help(type(self)) for accurate signature.
                                        #       |
                                        #       |  my_storage(self)
                                        #       |
                                        #       |  ----------------------------------------------------------------------
                                        #       |  Methods inherited from Phone5:
                                        #       |
                                        #       |  full_name(self)
                                        #       |
                                        #       |  make_a_call(self, number)
                                        #       |
                                        #       |  ----------------------------------------------------------------------
                                        #       |  Data descriptors inherited from Phone5:
                                        #       |
                                        #       |  __dict__
                                        #       |      dictionary for instance variables (if defined)
                                        #       |
                                        #       |  __weakref__
                                        #       |      list of weak references to the object (if defined)




# print(help(FlagshipPhone)) 
                                        #  o/p:  Help on class FlagshipPhone in module __main__:

                                        #       class FlagshipPhone(Smartphone3)
                                        #       |  FlagshipPhone(brand, model_name, price, ram, internal_memory, rear_camera, front_camera)
                                        #       |
                                        #       |  Method resolution order:
                                        #       |      FlagshipPhone
                                        #       |      Smartphone3
                                        #       |      Phone5
                                        #       |      builtins.object
                                        #       |
                                        #       |  Methods defined here:
                                        #       |
                                        #       |  __init__(self, brand, model_name, price, ram, internal_memory, rear_camera, front_camera)
                                        #       |      Initialize self.  See help(type(self)) for accurate signature.
                                        #       |
                                        #       |  ----------------------------------------------------------------------
                                        #       |  Methods inherited from Smartphone3:
                                        #       |
                                        #       |  my_storage(self)
                                        #       |
                                        #       |  ----------------------------------------------------------------------
                                        #       |  Methods inherited from Phone5:
                                        #       |
                                        #       |  full_name(self)
                                        #       |
                                        #       |  make_a_call(self, number)
                                        #       |
                                        #       |  ----------------------------------------------------------------------
                                        #       |  Data descriptors inherited from Phone5:
                                        #       |
                                        #       |  __dict__
                                        #       |      dictionary for instance variables (if defined)
                                        #       |
                                        #       |  __weakref__
                                        #       |      list of weak references to the object (if defined)












# Method Overriding      -----> ethod has same name in different classes with different arguments

class Phone6:                # parent class / base class
    def __init__(self, brand, model_name, price):
        self.brand=brand
        self.model_name=model_name
        self._price=max(price,0)

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def make_a_call(self,number):
        return f"calling {number}......"

class Smartphone4(Phone6):           # child class / derived class
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        super().__init__(brand, model_name, price)
        self.ram=ram
        self.internal_memory=internal_memory
        self.rear_camera=rear_camera

    def my_storage(self):
        return f"Ram is : {self.ram} and Internal storage is : {self.internal_memory}"

    def full_name(self):
        return f"{self.brand} {self.model_name} {self.ram} {self.internal_memory}"

class FlagshipPhone1(Smartphone4):           
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera, front_camera):
        super().__init__(brand, model_name, price, ram, internal_memory, rear_camera)
        self.front_camera=front_camera



s=Smartphone4("abc","dfg",20000,"3 gb","12 gb","10mpx")
print(s.full_name())               # o/p: abc dfg 3 gb 12 gb

f=FlagshipPhone1("One+","o1",65000,"12 GB","128 GB","64 mpx","32 mpx")
print(f.full_name())               # o/p: One+ o1 12 GB 128 GB               # this is happening because python firstly checks in flagshipPhone class, if there is no method of full_name then it will check in smartphone class and there python got full_name method so python did not check in phone class, as a result smartphone's full_name method executed










# isinstance(), issubclass() -----> built-in function




# isinstance()     ----> we can use this function when we want to check this object is class or not like 's' is object of 'Smartphone4' class or not?

print(isinstance(s,Smartphone4))           # o/p: True
print(isinstance(s,Phone6))                # o/p: True
print(isinstance(s,FlagshipPhone1))        # o/p: False






# issubclass()
print(issubclass(Smartphone4,Phone6))              # o/p: True
print(issubclass(Smartphone4,FlagshipPhone1))      # o/p: False
print(issubclass(FlagshipPhone1,Phone6))           # o/p: True































# Multiple Inheritance


class A:
    def class_a_method(self):
        return 'I\'m Just class A method'
    
    def hello(self):
        return "hello! fro class A"

instance_a=A()
print(instance_a.class_a_method())                      # o/p: I'm Just class A method





class A1:
    def class_a_method(self):
        return 'I\'m Just class A1 method'
    
    def hello(self):
        return "hello! from class A1"

class B1:
    def class_b_method(self):
        return 'I\'m Just class B1 method'
    
    def hello(self):
        return "hello! from class B1"

class C1(A1,B1):
# class C1(B1,A1):
    pass                            # here i don't want to write anythong inside class so I wrote pass


instance_c=C1()
print(instance_c.class_a_method())               # o/p: I'm Just class A1 method
print(instance_c.class_b_method())               # o/p: I'm Just class B1 method
print(instance_c.hello())                        # o/p: hello! from class A1               # i got to called class A1's hello method because C1(A1,B1) so method resolution order is C1 then A1 then B1               (resolution order means python checks method available in class or not)
print(instance_c.hello())                        # o/p: hello! from class B1               # # i got to called class A1's hello method because C1(B1,A1) so method resolution order is C1 then B1 then A1              (we can check resolution order using help function)



# there are two ways in python to check method resolution order

# 1) using help function
# print(help(C1))                         # o/p: class C1(A1, B1)
                                        #      |  Method resolution order:
                                        #      |      C1
                                        #      |      A1
                                        #      |      B1
                                        #      |  Methods inherited from A1:
                                        #      |
                                        #      |  class_a_method(self)

# 2) mro function
print(C1.mro())                         # o/p: [<class '__main__.C1'>, <class '__main__.A1'>, <class '__main__.B1'>, <class 'object'>]
# or
print(C1.__mro__)                       # o/p: (<class '__main__.C1'>, <class '__main__.A1'>, <class '__main__.B1'>, <class 'object'>)































# Special Magic methods/Dunder methods
# Operator overloading
# Ploymorphism





# Special Magic methods/Dunder methods     ------> which hass double underscore at front and rear like '__init__ method'.

class Phone7:
    def __init__(self, brand, model_name, price):
        self.brand=brand
        self.model_name=model_name
        self._price=price
        self.complete_specification=f"{self.brand} {self.model_name} and price is {self._price}"


    def make_a_call(self, phone_number):
        print(f"calling {phone_number}.......")


l6=[1,2,3]
print(l6)                                           # o/p: [1, 2, 3] 
instance_phone7=Phone7("Nokia","s10",2000)
print(instance_phone7)                              # o/p: <__main__.Phone7 object at 0x03912FA0>
# when i call list's object by its name i got data of list but it is not happened with instance_phone7 object where i got location as output
# we can overcome this problem using dunder methods (str, repr)   (repr means representation)




class Phone8:
    def __init__(self, brand, model_name, price):
        self.brand=brand
        self.model_name=model_name
        self._price=price
        self.complete_specification=f"{self.brand} {self.model_name} and price is {self._price}"


    def make_a_call(self, phone_number):
        print(f"calling {phone_number}.......")

    # str, repr
    def __repr__(self):
        return f"{self.brand} {self._price}"


instance_phone8=Phone8("Nokia","s10",2000)
print(instance_phone8)                       # o/p: Nokia 2000







class Phone9:
    def __init__(self, brand, model_name, price):
        self.brand=brand
        self.model_name=model_name
        self._price=price
        self.complete_specification=f"{self.brand} {self.model_name} and price is {self._price}"


    def make_a_call(self, phone_number):
        print(f"calling {phone_number}.......")

    # str, repr
    def __str__(self):
        return f"{self.brand} {self._price}"


instance_phone9=Phone9("Nokia","s10",2000)
print(instance_phone9)                       # o/p: Nokia 2000







class Phone91:
    def __init__(self, brand, model_name, price):
        self.brand=brand
        self.model_name=model_name
        self._price=price
        self.complete_specification=f"{self.brand} {self.model_name} and price is {self._price}"


    def make_a_call(self, phone_number):
        print(f"calling {phone_number}.......")

    # str, repr
    def __str__(self):
        return f"{self.brand} {self.model_name}"
    
    def __repr__(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"


instance_phone91=Phone91("Nokia","s10",2000)
print(instance_phone91)                       # o/p: Nokia s10






class Phone92:
    def __init__(self, brand, model_name, price):
        self.brand=brand
        self.model_name=model_name
        self._price=price
        self.complete_specification=f"{self.brand} {self.model_name} and price is {self._price}"


    def make_a_call(self, phone_number):
        print(f"calling {phone_number}.......")

    # str, repr  
    def __repr__(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"

    def __str__(self):
        return f"{self.brand} {self.model_name}"

instance_phone92=Phone92("Nokia","s10",2000)
print(instance_phone92)                       # o/p: Nokia s10
print(str(instance_phone92))                  # o/p: Nokia s10
print(repr(instance_phone92))                 # o/p: Nokia s10 and price is 2000







# professional use this way
class Phone93:
    def __init__(self, brand, model_name, price):
        self.brand=brand
        self.model_name=model_name
        self._price=price
        self.complete_specification=f"{self.brand} {self.model_name} and price is {self._price}"


    def make_a_call(self, phone_number):
        print(f"calling {phone_number}.......")

    # str, repr  
    def __str__(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"

    def __repr__(self):
        return f"Phone(\"{self.brand}\",\"{self.model_name}\",{self._price})"

instance_phone93=Phone93("Nokia","s10",2000)
print(instance_phone93)                      # o/p: Nokia s10 and price is 2000
print(repr(instance_phone93))                # o/p: Phone("Nokia","s10",2000)









d1=[1,2,3]
d2=(1,3,4)
d3="Ravin"
print(len(d1))               # o/p: 3
print(len(d2))               # o/p: 3
print(len(d3))               # o/p: 5

# i can also find the lenth of the phone object but i have to use duder method

class Phone94:
    def __init__(self, brand, model_name, price):
        self.brand=brand
        self.model_name=model_name
        self._price=price
        self.complete_specification=f"{self.brand} {self.model_name} and price is {self._price}"


    def my_phone(self):
        return f"{self.brand} {self.model_name}"
    
    def __len__(self):
            return len(self.my_phone())

instance_phone94=Phone94("Nokia","s10",2000)
print(len(instance_phone94))             # o/p: 9












# Operator Overloading

#  2+3=5
# 'abc'+'wer'='abcwer'

instance_phone941=Phone94("Nokia","s11",2200)
# print(instance_phone94+instance_phone941)                    # type error
# we can overcome by + operator overloading



class Phone95:
    def __init__(self, brand, model_name, price):
        self.brand=brand
        self.model_name=model_name
        self.price=price
        self.complete_specification=f"{self.brand} {self.model_name} and price is {self.price}"


    def my_phone(self):
        return f"{self.brand} {self.model_name}"
    
    def __len__(self):
            return len(self.my_phone())

    def __add__(self, other):
        return self.price + other.price                 # here we made + operator overloading


instance_phone95a=Phone95("Nokia","s10",2000)
instance_phone95b=Phone95("Nokia","s11",2200)
print(instance_phone95a+instance_phone95b)               # o/p: 4200








# Polymorphism        -----> many forms
#  2+3=5                                # here + is used as sum of two number
# 'abc'+'wer'='abcwer'                  # here + is used for concating two string                # here + used for many purpose do it is example of polymorphism
# method overriding is also example of polymorphism