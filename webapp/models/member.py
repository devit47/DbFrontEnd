from webapp.dbconnect import Connection
import cx_Oracle


def check_for_premium():
    try:
        connection = Connection()
        connection.connect()
        cur = connection.cursor
        cur.callproc('SP_Premium_Update_Check')
        connection.close()
    except cx_Oracle.DatabaseError:
        print('Failed to call SP_Premium_Update_Check')


def set_temp_to_standard():
    try:
        connection = Connection()
        connection.connect()
        cur = connection.cursor
        cur.callproc('SP_Set_TempPremium_To_Std')
        connection.close()
    except cx_Oracle.DatabaseError:
        print('Failed to call SP_Set_TempPremium_To_Std')


def add_new_member():
    try:
        connection = Connection()
        connection.connect()
        cur = connection.cursor
        cur.callproc('SP_Validate_Member')
        connection.close()
    except cx_Oracle.DatabaseError:
        print('Failed to call SP_Validate_Member')


def get_all_members():
    members = []
    try:
        connection = Connection()
        connection.connect()
        cur = connection.cursor
        cur.execute('select * from members')
        for line in cur:
            members.append(line)
        connection.close()

        return members
    except cx_Oracle.DatabaseError:
        print('Failed to call get members')
