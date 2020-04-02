# Lambda Expression (anonymous function)


def add(a,b):
    return a+b

print(add(2,3))                      # o/p: 5





print(add)                           # o/p: <function add at 0x009EF340>xxxxxx  



addition=lambda a,b:a+b
print(addition(4,5))                 # o/p: 9

print(addition)                      # o/p: <function <lambda> at 0x014DF2F8>

                 
multiplication=lambda a,b:a*b
print(multiplication(4,5))           # o/p: 20






# Lambda expression practice


# Even or not
def is_even(a):
    if a%2==0:
        return True
    return False

# OR
def is_even1(a):
    return a%2==0



# OR
is_even2=lambda a:a%2==0                     # o/p: Enter number:
n=input('Enter number:\n')                   #      12
print(is_even2(int(n)))                      #      True












# Last character
def last_char(s):
    return s[-1]

print(last_char("Ravin"))                  # o/p: n

# OR

last_char1=lambda s:s[-1]                  # o/p: Enter String:
s1=input("Enter String:\n")                #      Yash      
print(last_char1(s1))                      #      h









# Lambda function with if-else statement
def len_check(s):
    if len(s)>5:
        return True
    return False

print(len_check("Ravin"))                     # o/p: False

# OR

len_check1=lambda s:len(s)>5                  # o/p: Enter String:
n1=input("Enter String:\n")                   #      wq
print(len_check1(n1))                         #      False

# OR 

len_check2=lambda s1:True if len(s1)>5 else False        # o/p: Enter String:
n1=input("Enter String:\n")                              #      Ravinr
print(len_check1(n1))                                    #      True