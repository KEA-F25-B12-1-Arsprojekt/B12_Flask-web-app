# Import module
import sqlite3
import random
# Connecting to sqlite
conn = sqlite3.connect('users.db')

# Creating a cursor object using the 
# cursor() method
cursor = conn.cursor()

# Queries to INSERT records.
def Insert_values(ID, PASSWORD, NAME):
    cursor.execute(''' INSERT INTO EMPLOYEE (ID, PASSWORD, NAME) VALUES (?, ?, ?)''', (ID, PASSWORD, NAME))

# Display data inserted
print("Data Inserted in the table: ")
data=cursor.execute('''SELECT * FROM EMPLOYEE''')
for row in data:
    print(row)

E_ID = random.randint(1000, 8000)
E_PASSWORD = '?'
E_NAME = '?'

Insert_values(E_ID, E_PASSWORD , E_NAME)

data2 = cursor.execute(''' SELECT * FROM EMPLOYEE''')
print(data2)

# Commit your changes in 
# the database   
conn.commit()

# Closing the connection
conn.close()

