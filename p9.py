# List Comprehension         (uniq and important topic in python)


# with the help of list comprehension we can create of list in one line


# ex--> create a list of squares from 1 to+nnnn 10
square1=[]
for i in range(1,11):
    square1.append(i**2)
    i=i+1
print(square1)                    # o/p: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# OR
square2=[j**2 for j in range(1,11)]
print(square2)                    # o/p: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# ex----> create list of negative number 1-10
neg_num=[-i for i in range(1,11)]
print(neg_num)                    # o/p: [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

# OR
neg1_num=[]
for i in range(1,11):
    neg1_num.append(-i)
print(neg1_num)                   # o/p: [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]






# Ex
names=['Ravin','Rupen','Yash','Chirag']
new_list=[]
for name in names:
    new_list.append(name[0])
print(new_list)                    # o/p: ['R', 'R', 'Y', 'C']

# oR
new_list=[name[0] for name in names]
print(new_list)                    # o/p: ['R', 'R', 'Y', 'C']








  

# Excercise 1
list1=['abc','def','klp','asd']
rev_list=[rev[::-1] for rev in list1]
print(rev_list)                    # o/p: ['cba', 'fed', 'plk', 'dsa']













# list comprehension with if statement
numbers=list(range(1,11))
print(numbers)                       # o/p: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


even_num=[]
for i in numbers:
    if i%2==0:
        even_num.append(i)
print(even_num)                      # o/p: [2, 4, 6, 8, 10]

# OR
eve_list=[i for i in numbers if i%2==0]
print(eve_list)                      # o/p: [2, 4, 6, 8, 10]
odd_list=[i for i in range(1,11) if i%2!=0]
print(odd_list)                      # o/p: [1, 3, 5, 7, 9]









# Exercise 2
def int_to_str(l1):
    return [str(i) for i in l1 if type(i)==int or type(i)==float]

print(int_to_str([True,False,'Str',[1,2,3],1,1.0,2]))              # o/p: ['1', '1.0', '2']












# list comprehension with if-else statement
num1_list=[]
for i in range(1,11):
    if i%2==0:
        num1_list.append(-i)
    else:
        num1_list.append(i**2)
print(num1_list)                             # o/p: [1, -2, 9, -4, 25, -6, 49, -8, 81, -10]



num_list=[-i if (i%2==0) else i**2 for i in range(1,11) ]
print(num_list)                             # o/p: [1, -2, 9, -4, 25, -6, 49, -8, 81, -10]













# Nested list comprehension

# Example---->[[1,2,3],[1,2,3],[1,2,3]]
nested_list=[[i for i in range(1,4)] for j in range(1,4)]
print(nested_list)                          # o/p: [[1, 2, 3], [1, 2, 3], [1, 2, 3]]