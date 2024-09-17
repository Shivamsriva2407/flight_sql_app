import mysql.connector as c


try:
    conn  = c.connect(

         host='127.0.0.1',
         user = 'root',
         password ='',
        database = 'indigo'
    )
    cursor = conn.cursor()
    print('connection establised')
except Exception as e:
    print('connection error')

#     Create a database on the db server

# cursor.execute('create database indigo')
# conn.commit()

#  create a table
#  airport id, code , name
# cursor.execute('''
# create table airport (
# airport_id INTEGER PRIMARY KEY ,
# code VARCHAR(10) not null,
# city VARCHAR(50) not null,
# name VARCHAR(255)not null
# )
# ''')
# conn.commit()



#  INSERT DATA INTO THE TABLE

# cursor.execute('''
# Insert into airport values
# (1,'DEL','New delhi','IGIA'),
# (2,'MUM','Mumbai','MA'),
# (3,'BAN','Bangalore','BA'),
# (4,'CAL','Kolkatta','CA'),
# (5,'UPA','Uttar pradesh','UA'),
# (6,'JAM','Jammu','JA')
# ''')
# conn.commit()



#  Search

cursor.execute('''
select * from airport where airport_id>3
''')
data = cursor.fetchall()
print(data)

for i in data:
    print(i[3])