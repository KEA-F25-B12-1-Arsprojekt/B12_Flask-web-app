# Import module
from datetime import datetime
import sqlite3
import random
# datetime object containing current date and time
now = datetime.now()
 
# dd/mm/YY H:M:S
dt_string = now.strftime("%Y/%d/%m/%H:%M")
print(dt_string)

# Connecting to sqlite
conn = sqlite3.connect('user_time.db')

# Creating a cursor object using the 
# cursor() method
cursor = conn.cursor()

# Queries to INSERT records.
def Insert_values(ID, EID, DATE, LOGIN, LOGOUT):
    cursor.execute(''' INSERT INTO EMPLOYEE_TIME (ID, EID, DATE, LOGIN, LOGOUT) VALUES (?, ?, ?,?,?)''', (ID, EID, DATE, LOGIN, LOGOUT))

# Display data inserted
print("Data Inserted in the table: ")
data=cursor.execute('''SELECT * FROM EMPLOYEE_TIME''')
for row in data:
    print(row)

R_ID = random.randint(1000, 8000)
E_ID = 'SDSDSDSDS'
E_DATE = now.strftime('%Y/%m/%d')
E_LOGIN = now.strftime('%H:%M')
E_LOGOUT = 0

Insert_values(R_ID, E_ID, E_DATE, E_LOGIN, E_LOGOUT)

# Commit your changes in 
# the database    
conn.commit()

conn.close()