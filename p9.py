# List Comprehension         (uniq and important topic in python)


# with thw help of list comprehension we can create of list in one line


# ex--> create a list of squares from 1 tp 10
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

