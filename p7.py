# #Dictionaries intro
# #Q - why we use dictionaries?
# #A - Because of limitation of lists, lists are not enough to represent
# #real data
# #secondly, dictinaries are unordered collection of data-----> means not indexing and data in kay:value pair


# #create dictionary
# # 1) first method
# user={'name':'Ravin','age':22}
# print(user)                        #o/p:{'name': 'Ravin', 'age': 22}
   
# # 2) second method
# user1=dict(name='Ravin',age=22)
# print(user1)                         #o/p:{'name': 'Ravin', 'age': 22}




# #access data in dictionary
# #unorderd collection of data, so we can't access by indexing
# #as a result, we can access data by using key
# print(user1['name'])                               #o/p:Ravin
# print(user1['age'])                                #o/p:22

# # we can store anything inside dictionary....



# # add data in deictionary
# user_in={}
# user_in['name']='Ravin'
# user_in['age']=22
# print(user_in)



# #create the dictionaries
# user_info={
#     'name':'Ravin',
#     'age':22,
#     'fav_movie':['3 iditos','gangajal'],
#     'fav_song':['kal ho na ho','kata laga'],
#     'fav_sub':{'science':'drawing'}
# }
# print(user_info)               #o/p:{'name': 'Ravin', 'age': 22, 'fav_movie': ['3 iditos', 'gangajal'], 'fav_song': ['kal ho na ho', 'kata laga'], 'fav_sub': {'science': 'drawing'}}
# print(user_info['fav_movie'])  #o/p:['3 iditos', 'gangajal']
# print(user_info['fav_sub'])    #o/p:{'science': 'drawing'}   


# users={
#     'user1':{
#         'name':'Ravin',
#         'age':22,
#         'l_name':'Rakholiya',
#     },
#     'user2':{
#         'name':'Ravin1',
#         'age':21,
#         'l_name':'Rakholiya1',
#     },
#     'user3':{
#         'name':'Ravin3',
#         'age':24,
#         'l_name':'Rakholiya3',
#     }
# }
# print(users)     #o/p:{'user1': {'name': 'Ravin', 'age': 22, 'l_name': 'Rakholiya'}, 'user2': {'name': 'Ravin1', 'age': 21, 'l_name': 'Rakholiya1'}, 'user3': {'name': 'Ravin3', 'age': 24, 'l_name': 'Rakholiya3'}}
# print(users['user2'])   #o/p:{'name': 'Ravin1', 'age': 21, 'l_name': 'Rakholiya1'}





# #add data in empty dictionary
# user_in={}
# user_in['name']="Rebel"
# print(user_in)                #o/p:{'name': 'Rebel'}
# user_in['age']=23
# print(user_in)                #o/p:{'name': 'Rebel', 'age': 23}




# # In keyword and iteration in dictionary

user_info={
    'name':'Ravin',
    'age':22,
    'fav_movie':['3 iditos','gangajal'],
    'fav_song':['kal ho na ho','kata laga'],
    'fav_sub':{'science':'drawing'}
}


# # check if key exist in dictionary  (only use in for checking by keys)
# if 'name' in user_info:
#     print("present")
# else:
#     print("not present")

# # o/p: present




# # check if value exist in dictionary  (here we have to use in keyword + dictionary name with values())
# if 22 in user_info.values():
#     print("present")
# else:
#     print("Not present")

# # o/p: present


# if ['kal ho na ho','kata laga'] in user_info.values():
#     print("present")
# else:
#     print("Not present")

# # o/p: present





# # looping in dictionary
# for i in user_info:
#     print(i)

# # o/p:  name
# #       age
# #       fav_movie
# #       fav_song
# #       fav_sub





# for i in user_info.values():
#     print(i)

# # o/p: Ravin
# #      22
# #      ['3 iditos', 'gangajal']
# #      ['kal ho na ho', 'kata laga']
# #      {'science': 'drawing'}






# for i in user_info:
#     print(user_info[i])

# # o/p: Ravin
# #      22
# #      ['3 iditos', 'gangajal']
# #      ['kal ho na ho', 'kata laga']
# #      {'science': 'drawing'}






# # Values method
# user_info_dict_value=user_info.values()
# print(user_info_dict_value)        # o/p: dict_values(['Ravin', 22, ['3 iditos', 'gangajal'], ['kal ho na ho', 'kata laga'], {'science': 'drawing'}])
# print(type(user_info_dict_value))  # o/p: <class 'dict_values'>





# # Keys method
# user_info_dict_keys=user_info.keys()
# print(user_info_dict_keys)        # o/p: dict_keys(['name', 'age', 'fav_movie', 'fav_song', 'fav_sub'])
# print(type(user_info_dict_keys))  # o/p: <class 'dict_keys'>








# # Items methos
# user_item=user_info.items()
# print(user_item)              # o/p: dict_items([('name', 'Ravin'), ('age', 22), ('fav_movie', ['3 iditos', 'gangajal']), ('fav_song', ['kal ho na ho', 'kata laga']), ('fav_sub', {'science': 'drawing'})])
# print(type(user_item))        # o/p: <class 'dict_items'>


# for key, value in user_info.items():
#     print(f'key is {key} and value is {value}')

# # o/p:   key is name and value is Ravin
# #        key is age and value is 22
# #        key is fav_movie and value is ['3 iditos', 'gangajal']
# #        key is fav_song and value is ['kal ho na ho', 'kata laga']
# #        key is fav_sub and value is {'science': 'drawing'}









# # Add and Delete data

# # ADD
# user_info['user_tune']=['tune 1','tune 2']
# print(user_info)                  # o/p: {'name': 'Ravin', 'age': 22, 'fav_movie': ['3 iditos', 'gangajal'], 'fav_song': ['kal ho na ho', 'kata laga'], 'fav_sub': {'science': 'drawing'}, 'user_tune': ['tune 1', 'tune 2']}





# #DELETE
# popped_item=user_info.pop('user_tune')
# print(f'pop item is{popped_item}') # o/p: pop item is['tune 1', 'tune 2']---------->list
# print(user_info)                   # o/p: {'name': 'Ravin', 'age': 22, 'fav_movie': ['3 iditos', 'gangajal'], 'fav_song': ['kal ho na ho', 'kata laga'], 'fav_sub': {'science': 'drawing'}}




# #  popped item rendomly pop)
# popped_item1=user_info.popitem()
# print(popped_item1)                  # o/p: ('user_tune', ['tune 1', 'tune 2'])-----------------> tuple
# print(user_info)                     # o/p: {'name': 'Ravin', 'age': 22, 'fav_movie': ['3 iditos', 'gangajal'], 'fav_song': ['kal ho na ho', 'kata laga'], 'fav_sub': {'science': 'drawing'}}
# print(type(popped_item1))            # o/p: <class 'tuple'>










# # update() mathod
# more_info={'State':['Gujarat','Maharashtra'],'Dist':['Junagadh','Surat']}
# user_info.update(more_info)
# print(user_info)                   # o/p: {'name': 'Ravin', 'age': 22, 'fav_movie': ['3 iditos', 'gangajal'], 'fav_song': ['kal ho na ho', 'kata laga'], 'fav_sub': {'science': 'drawing'}, 'State': ['Gujarat', 'Maharashtra'], 'Dist': ['Junagadh', 'Surat']}

# more_info1={'name':'Ravin Rakholiya'}
# user_info.update(more_info1)
# print(user_info)                   # o/p: {'name': 'Ravin Rakholiya', 'age': 22, 'fav_movie': ['3 iditos', 'gangajal'], 'fav_song': ['kal ho na ho', 'kata laga'], 'fav_sub': {'science': 'drawing'}, 'State': ['Gujarat', 'Maharashtra'], 'Dist': ['Junagadh', 'Surat']}

# user_info.update({})                # it will not be affected
# print(user_info)                     # o/p: {'name': 'Ravin', 'age': 22, 'fav_movie': ['3 iditos', 'gangajal'], 'fav_song': ['kal ho na ho', 'kata laga'], 'fav_sub': {'science': 'drawing'}}










# fromkeys, get, clear, copy method


# Fromkeys--------> used for creating dictionary

# d={'name':'unknown','age':'unknown'}

d=dict.fromkeys(['name','age','height'],'unknown')
print(d)                                   # o/p: {'name': 'unknown', 'age': 'unknown', 'height': 'unknown'}

d1=dict.fromkeys(('name','age','height'),'unknown')
print(d1)                                  # o/p: {'name': 'unknown', 'age': 'unknown', 'height': 'unknown'}


d2=dict.fromkeys("abc",'unknown')
print(d2)                                  # o/p: {'a': 'unknown', 'b': 'unknown', 'c': 'unknown'}

d3=dict.fromkeys(range(1,11),"unknown")
print(d3)                                  # o/p: {1: 'unknown', 2: 'unknown', 3: 'unknown', 4: 'unknown', 5: 'unknown', 6: 'unknown', 7: 'unknown', 8: 'unknown', 9: 'unknown', 10: 'unknown'}

d4=dict.fromkeys(('name','age'),['unknown','unknown'])
print(d4)                                  # o/p: {'name': ['unknown', 'unknown'], 'age': ['unknown', 'unknown']}





# Get() Methos (Useful)
print(d['name'])