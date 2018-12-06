from webapp.dbconnect import Connection
import cx_Oracle


def get_all_colleges():
    members = []
    test = []
    try:
        connection = Connection()
        connection.connect()
        cur = connection.cursor
        cur.execute('select * from colleges')
        for line in cur:
            for data in line:
                test.append(data)
            members.append(line)

        connection.close()
        return members
    except cx_Oracle.DatabaseError as ex:
        error, = ex.args
        print(str(error.code) + " :" + error.message)


def add_college(college_name):
    try:
        connection = Connection()
        connection.connect()
        cur = connection.cursor
        cur.callproc('SP_Validate_College', [college_name])
        connection.close()
    except cx_Oracle.DatabaseError:
        print('Failed to call SP_Validate_College')
