import sqlite3
import random
from datetime import datetime
from flask_login import current_user

DB_PATH = "user_time.db"

class Lg_update:
    def __init__(self, columns, db_path=DB_PATH):
        """
        Initialize with column name(s) and database path.
        Accepts either a single string or a list of strings.
        """
        if isinstance(columns, str):
            self.columns = [columns]
        elif isinstance(columns, list):
            self.columns = columns
        else:
            raise ValueError("columns must be a string or a list of strings")
        self.db_path = db_path

    def fetch_columns(self):
        """
        Build and execute a query to fetch the specified columns from EMPLOYEE_TIME.
        """
        columns_str = ", ".join(self.columns)
        query = f"SELECT {columns_str} FROM EMPLOYEE_TIME"
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return result

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

def main():
    now = datetime.now()
    today = now.strftime('%Y/%d/%m') 
    current_time = now.strftime("%H:%M")
    empty_marker = 'empty'
    
    if current_user.is_authenticated:
        print(f"Logged-in user: {current_user.username}")
    else:
        print("no user is logged in.")
    
    return current_user.username
    
    emp_id = current_user.username
    
    record = get_employee_record(emp_id)
    
    if record is None:
        # er ikke i database
        print(f"Employee with ID {emp_id} not found. Inserting a new record for today.")
        insert_values(emp_id, today, current_time, empty_marker)
    else:
        # Since we assume one record per employee, get the stored date.
        record_date = record[1]  # Assuming the DATE column is at index 1.
        if record_date != today:
            # The employee is logging in on a new day: update the record to reflect today.
            print(f"Employee ID {emp_id} is logging in on a new day. Updating DATE, LOGIN and resetting LOGOUT.")
            update_record_new_day(emp_id, today, current_time)
        else:
            # The record is for today. Update according to current state of LOGIN and LOGOUT.
            current_login = record[2]  # LOGIN column
            current_logout = record[3] # LOGOUT column
            if current_login == empty_marker and current_logout == empty_marker:
                print(f"Employee ID {emp_id} has no LOGIN for today. Setting LOGIN time.")
                update_login(emp_id, current_time)
            elif current_login != empty_marker and current_logout == empty_marker:
                print(f"Employee ID {emp_id} is already logged in today. Setting LOGOUT time.")
                update_logout(emp_id, current_time)
            else:
                print(f"Employee ID {emp_id} already has both LOGIN and LOGOUT times filled for today.")
    
    # For demonstration: fetch and print all employee IDs.
    selector = Lg_update("ID")
    print("Employee IDs in the table:", selector.fetch_columns())

if __name__ == "__main__":
    main()