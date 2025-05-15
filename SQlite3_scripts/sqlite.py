# Import module
import sqlite3

set  

# Connecting to sqlite
conn = sqlite3.connect('Sqlite3test.db')

# Creating a cursor object using the 
# cursor() method
cursor = conn.cursor()

# Queries to INSERT records.
def Insert_values(ID, PASSWORD, NAME):
    cursor.execute(''' INSERT INTO EMPLOYEEID (ID, PASSWORD, NAME) VALUES (?, ?, ?)''', (ID, PASSWORD, NAME))

# Display data inserted
print("Data Inserted in the table: ")
data=cursor.execute('''SELECT * FROM EMPLOYEEID''')
for row in data:
    print(row)

E_ID = 'bomb'
E_PASSWORD = 'sky0001'
E_NAME = 'dumbo'

Insert_values(E_ID, E_PASSWORD , E_NAME)

# Commit your changes in 
# the database    
conn.commit()



# Closing the connection
conn.close()

