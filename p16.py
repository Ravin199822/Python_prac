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




# class Person:
#     def __init__(self, first_name, last_name, age):                      # it is called as init method or constructor
#         # instance variable                                              # self represents object like p1 and p2
#         self.first_name=first_name                                       # whenever we called init method, self is bydefault first argument. and self represents our object.
#         self.last_name=last_name
#         self.age=age

# p1=Person("Ravinkumar","Rakholiya",22)
# p2=Person("Rupenkumar","Rakholiya1",19)

# print(p1.first_name)                           # o/p: Ravinkumar
# print(p2.first_name)                           # o/p: Rupenkumar







# class Person:
#     def __init__(self, first_name, last_name, age):
#         # instance variables
#         print("init method // constructor get called")  
#         self.first_name=first_name                                       
#         self.last_name=last_name
#         self.age=age

# p1=Person("Ravinkumar","Rakholiya",22)                          # o/p: init method // constructor get called


# p1=Person("Ravinkumar","Rakholiya",22)                      # init method called when we create object.   
# p2=Person("Rupenkumar","Rakholiya1",19)
# # o/p: init method // constructor get called
# #      init method // constructor get called








# class Person:
#     def __init__(person_obj, first_name, last_name, age):
#         # instance variables
#         person_obj.person_first_name=first_name                       # person_first_name----> instance variable                                     
#         person_obj.last_name=last_name
#         person_obj.age=age

# p1=Person("Ravinkumar","Rakholiya",22) 
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












# in python, the all function which are inside the class called as function.




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
# 1). we write pi value 3.14 when we create object, like in above case we made two object, hence we have to write 3.14 two times.....2). as a result 3.14 store in memory for each objects, so it will take more space, which is result of memory wastage.






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


# Laptop3.lap_disc1=0
lp5=Laptop3("Dell","inspire 5558",52500)
lp6=Laptop3("Hp","inspire 5558",50000)
print(lp5.laptop_discount())                            # o/p: 52500.0
print(lp6.laptop_discount())                            # o/p: 50000.0


# how can we see, object has which variables
print(lp5.__dict__)                              # o/p: {'brand_name': 'Dell', 'name': 'inspire 5558', 'price': 52500}
print(lp6.__dict__)                              # o/p: {'brand_name': 'Hp', 'name': 'inspire 5558', 'price': 50000}


# here, if we want to apply discount 30 for only Hp's laptop so....
lp6.lap_disc1=30
print(lp6.laptop_discount())                     # o/p: 45000.0              the output is took disc=10 , so we can not get right answer using this method




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