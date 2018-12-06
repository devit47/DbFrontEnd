from webapp.dbconnect import Connection
import cx_Oracle


def get_all_listings():
    members = []
    test = []
    try:
        connection = Connection()
        connection.connect()
        cur = connection.cursor
        cur.execute('select * from VIEW_LISTINGS')
        for line in cur:
            for data in line:
                test.append(data)
            members.append(line)

        connection.close()
        return members
    except cx_Oracle.DatabaseError as ex:
        error, = ex.args
        print(str(error.code) + " :" + error.message)
