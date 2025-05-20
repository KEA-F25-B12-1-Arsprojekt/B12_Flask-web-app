from datetime import datetime
import sqlite3
import random
import sqlite.py



class sel_e:
    def __init__(self, EID):
        self.EID = E_ID
            """ SELECT self.EID FROM EMPLOYEE """

class sel_id:
    def __init__(self, ID):
        self.ID = R_ID
            """ SELECT self.ID FROM EMPLOYEE """
    
class sel_login:
    def __init__(self, LOGIN):
        self.LOGIN = E_LOGIN
            """ SELECT self.LOGIN FROM EMPLOYEE """

class sel_logout:
    def __init__(self, LOGOUT):
        self.LOGOUT = E_LOGOUT
            """ SELECT self.LOGOUT FROM EMPLOYEE """


class sel_date:
    def __init__(self, DATE):
        self.DATE = E_DATE
            """ SELECT self.DATE FROM EMPLOYEE """


logi = sel_login

print(logi)