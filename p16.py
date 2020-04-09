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