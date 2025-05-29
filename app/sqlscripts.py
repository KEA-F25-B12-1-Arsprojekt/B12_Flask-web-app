import sqlite3
from datetime import datetime
from flask_login import current_user

DB_PATH = "user_time.db"

def get_employee_record(emp_id, db_path=DB_PATH):
    """
    Retrieve a record from EMPLOYEE_TIME for the given emp_id.
    Assumes that each employee appears only once in the table.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = "SELECT * FROM EMPLOYEE_TIME WHERE ID = ?"
    cursor.execute(query, (emp_id,))
    record = cursor.fetchone()
    conn.close()
    return record

def insert_values(emp_id, date, login, logout, db_path=DB_PATH):
    """
    Insert a new record into EMPLOYEE_TIME.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = "INSERT INTO EMPLOYEE_TIME (ID, DATE, LOGIN, LOGOUT) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (emp_id, date, login, logout))
    conn.commit()
    conn.close()

def update_login(emp_id, login_value, db_path=DB_PATH):
    """
    Update the LOGIN field for an existing employee.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = "UPDATE EMPLOYEE_TIME SET LOGIN = ? WHERE ID = ?"
    cursor.execute(query, (login_value, emp_id))
    conn.commit()
    conn.close()

def update_logout(emp_id, logout_value, db_path=DB_PATH):
    """
    Update the LOGOUT field for an existing employee.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = "UPDATE EMPLOYEE_TIME SET LOGOUT = ? WHERE ID = ?"
    cursor.execute(query, (logout_value, emp_id))
    conn.commit()
    conn.close()

def update_record_new_day(emp_id, date, login, db_path=DB_PATH):
    """
    For an existing employee logging in on a new day,
    update the DATE and LOGIN fields, and reset LOGOUT to 'empty'.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = "UPDATE EMPLOYEE_TIME SET DATE = ?, LOGIN = ?, LOGOUT = ? WHERE ID = ?"
    cursor.execute(query, (date, login, 'empty', emp_id))
    conn.commit()
    conn.close()


    now = datetime.now()
    today = now.strftime('%Y/%d/%m') 
    current_time = now.strftime("%H:%M")
    empty_marker = 'empty'
    
    emp_id = current_user.username
    
def handle_employee_check_in(emp_id):
    now = datetime.now()
    today = now.strftime('%Y/%d/%m') 
    current_time = now.strftime("%H:%M")
    empty_marker = 'empty'
    
    record = get_employee_record(emp_id)

    if record is None:
        # Check if employee exists in database
        print(f"Employee with ID {emp_id} not found. Inserting a new record for today.")
        insert_values(emp_id, today, current_time, empty_marker)
    else:
        # Get stored date
        record_date = record[1]
        if record_date != today:
            # New employee login
            print(f"Employee ID {emp_id} is logging in on a new day. Updating DATE, LOGIN and resetting LOGOUT.")
            update_record_new_day(emp_id, today, current_time)
        else:
            # Update based on current state (LOGIN and LOGOUT), give terminal updates
            current_login = record[2]  # LOGIN column
            current_logout = record[3]  # LOGOUT column
            if current_login == empty_marker and current_logout == empty_marker:
                print(f"Employee ID {emp_id} has no LOGIN for today. Setting LOGIN time.")
                update_login(emp_id, current_time)
            elif current_login != empty_marker and current_logout == empty_marker:
                print(f"Employee ID {emp_id} is already logged in today. Setting LOGOUT time.")
                update_logout(emp_id, current_time)
            else:
                print(f"Employee ID {emp_id} already has both LOGIN and LOGOUT times filled for today.")
