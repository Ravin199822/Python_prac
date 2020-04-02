# Dictionary comprehension



# square={1:1,2:4,3:9}

square={num:num**2 for num in range(1,11)}
print(square)                               # o/p: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}




square1={f"square of {num} is":num**2 for num in range(1,11)}
print(square1)                              # o/p: {'square of 1 is': 1, 'square of 2 is': 4, 'square of 3 is': 9, 'square of 4 is': 16, 'square of 5 is': 25, 'square of 6 is': 36, 'square of 7 is': 49, 'square of 8 is': 64, 'square of 9 is': 81, 'square of 10 is': 100}


for k,v in square1.items():
    print(f"{k}:{v}")

# o/p:  square of 1 is:1
#       square of 2 is:4
#       square of 3 is:9
#       square of 4 is:16
#       square of 5 is:25
#       square of 6 is:36
#       square of 7 is:49
#       square of 8 is:64
#       square of 9 is:81
#       square of 10 is:100





# word counter
String1="RavinsRi"
word_count={i:String1.count(i) for i in String1}
print(word_count)                              # o/p: {'R': 2, 'a': 1, 'v': 1, 'i': 2, 'n': 1, 's': 1}











# Dictionary comprehension with if-elase statement
dict_1={i:("even" if i%2==0 else "odd") for i in range(1,11)}
print(dict_1)                               # o/p: {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even', 7: 'odd', 8: 'even', 9: 'odd', 10: 'even'}















# SET Comprehension
square_set={i**2 for i in range(1,11)}
print(square_set)                   # o/p: {64, 1, 4, 36, 100, 9, 16, 49, 81, 25}




# 2)
names1=['Ravin','Rupen','Yash','Chirag']
name_set={names2[0] for names2 in names1}
print(name_set)                          # o/p: {'Y', 'R', 'C'}