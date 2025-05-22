import sqlite3
from datetime import datetime

now = datetime.now()


class SelClm:
    def __init__(self, columns, db_path="user_time.db"):
        """
        Initialize with column name(s) and database path.
        Accepts either a single string or a list of strings.
        """
        if isinstance(columns, str):
            # Convert a single column to a list for consistency
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
        # Create a comma-separated string of column names.
        # Ensure that the column names are valid; if they come from an untrusted source,
        # you may want to validate them against a known list of columns.
        columns_str = ", ".join(self.columns)
        query1 = f"SELECT {columns_str} FROM EMPLOYEE_TIME"

        # Connect to the database and fetch the data.
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(query1)
        result = cursor.fetchall()
        conn.close()
        return result

# You can choose a single column:
selector_single = SelClm("EID")
print("Single column (EID):", selector_single.fetch_columns())

# Or multiple columns:
selector_multiple = SelClm(["ID", "EID", "DATE", "LOGIN", "LOGOUT"])
print("Multiple columns (ID, EID, DATE, LOGIN, LOGOUT):", selector_multiple.fetch_columns())

class Lg_update:
    def __init__(self, columns, db_path="user_time.db"):
        """
        Initialize with column name(s) and database path.
        Accepts either a single string or a list of strings.
        """
        if isinstance(columns, str):
            # Convert a single column to a list for consistency
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
        # Create a comma-separated string of column names.
        # Ensure that the column names are valid; if they come from an untrusted source,
        # you may want to validate them against a known list of columns.
        columns_str = ", ".join(self.columns)
        query2 = f"SELECT {columns_str} FROM EMPLOYEE_TIME"

        # Connect to the database and fetch the data.
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(query2)
        result = cursor.fetchall()
        conn.close()
        return result
    

single_selector = Lg_update("ID")
if id != ("ID"): 
    def Insert_values(ID, DATE, LOGIN, LOGOUT):
        cursor.execute(''' INSERT INTO EMPLOYEE_TIME (ID, DATE, LOGIN, LOGOUT) VALUES (?, ?, ?, ?)''', (ID, DATE, LOGIN, LOGOUT))
elif id == "ID" and LOGIN == 'None' and LOGOUT == 'None':
    """
    Update EMPLOYEE_TIME
    SET LOGIN = now.strftime("%H:%m")
    WHERE id=ID
    """
elif LOGOUT == 'None' and LOGIN != 'None':
    """
    Update EMPLOYEE_TIME
    SET LOGOUT = now.strftime("%H:%m")
    WHERE id=ID
    """


