# Import module
from datetime import datetime
import sqlite3

# datetime object containing current date and time
now = datetime.now()
 
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%H:%M")
print(dt_string)

table = """ CREATE TABLE IF NOT EXISTS EMPLOYEE_TIME """
cursor.execute(table)
# Connecting to sqlite
conn = sqlite3.connect('user_time.db')

# Creating a cursor object using the 
# cursor() method
cursor = conn.cursor()

# Queries to INSERT records.
def Insert_values(ID, TIME, NAME):
    cursor.execute(''' INSERT INTO EMPLOYEE_TIME (ID, TIME, NAME) VALUES (?, ?, ?)''', (ID, TIME, NAME))

# Display data inserted
print("Data Inserted in the table: ")
data=cursor.execute('''SELECT * FROM EMPLOYEE_TIME''')
for row in data:
    print(row)

E_ID = 'bomb'
E_TIME = dt_string 
E_NAME = 'dumbo'

Insert_values(E_ID, E_TIME , E_NAME)

# Commit your changes in 
# the database    
conn.commit()