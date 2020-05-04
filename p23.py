import mysql.connector   



# Type Status in MySQL command line client   -----> we will get information about mySQL



# # Create connection
# conn=mysql.connector.connect(host='localhost', username='root', password='java')
# print(conn)                                                                        # o/p: <mysql.connector.connection.MySQLConnection object at 0x00F4C880>


# # my_cursor=conn.cursor()
# # query="CREATE DATABASE p_database"
# # my_cursor.execute(query)
# # conn.commit()
# # conn.close()




# my_cursor=conn.cursor()                                 # o/p: ('employees',)
# query="SHOW DATABASES"                                  #      ('information_schema',)
# my_cursor.execute(query)                                #      ('mysql',)
#                                                         #      ('new_database',)
# for database_name in my_cursor:                         #      ('p_database',)
#     print(database_name)                                #      ('performance_schema',)
# conn.commit()                                           #      ('sakila',)
# conn.close()                                            #      ('sales',) 
#                                                         #      ('sys',)
#                                                         #      ('world',)

# # This gives me tuple





# # To get output in list

# my_cursor=conn.cursor()
# query="SHOW DATABASES"
# my_cursor.execute(query)
# print(my_cursor.fetchall())                    # o/p: [('employees',), ('information_schema',), ('mysql',), ('new_database',), ('p_database',), ('performance_schema',), ('sakila',), ('sales',), ('sys',), ('world',)]
# conn.commit()
# conn.close()






# # If i want to use created database
# conn=mysql.connector.connect(host='localhost', username='root', password='java', database='p_database')
# my_cursor=conn.cursor()
# my_cursor.execute("CREATE TABLE student(name VARCHAR(255), age INT)")
# conn.commit()
# conn.close()



# conn=mysql.connector.connect(host='localhost', username='root', password='java', database='p_database')
# my_cursor=conn.cursor()
# query="INSERT INTO student(name, age) VALUES(%s,%s)"                   # in MYSQL---> %s   and in SQLITE---->?
# values=[
#     ('Ravin',22),
#     ('Rupen',29),
#     ('Renish',28),
#     ('Rockey',27),
#     ('Rock',26),
#     ('Rensom',25),
#     ('Ram',24),
#     ('Ronny',23)]

# # my_cursor.execute(query, values)           # only for one value

# my_cursor.executemany(query, values)         # for many values
# conn.commit()
# conn.close()











# conn=mysql.connector.connect(host='localhost', username='root', password='java', database='p_database')
# my_cursor=conn.cursor()
# query="select * from student"                   
# my_cursor.execute(query)           
# for columns in my_cursor:
#     print(columns)
# conn.commit()
# conn.close()


# # o/p: ('Ravin', 22)
# #      ('Ravin', 22)
# #      ('Rupen', 29)
# #      ('Renish', 28)
# #      ('Rockey', 27)
# #      ('Rock', 26)
# #      ('Rensom', 25)
# #      ('Ram', 24)
# #      ('Ronny', 23)










conn=mysql.connector.connect(host='localhost', username='root', password='java', database='p_database')
my_cursor=conn.cursor()
query="select * from student"                   
my_cursor.execute(query)           
print(my_cursor.fetchall())     # o/p: [('Ravin', 22), ('Ravin', 22), ('Rupen', 29), ('Renish', 28), ('Rockey', 27), ('Rock', 26), ('Rensom', 25), ('Ram', 24), ('Ronny', 23)]
conn.commit()
conn.close()