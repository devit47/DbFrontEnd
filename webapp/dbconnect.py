import cx_Oracle


class Connection:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = cx_Oracle.connect('project/pro@127.0.0.1/xe')
        self.cursor = self.connection.cursor()

    def close(self):
        self.cursor.close()
        self.connection.close()


# connect_string = 'project/pro@127.0.0.1/xe'
#
#
# def add_college(college_name):
#     try:
#         conn = cx_Oracle.connect(connect_string)
#         cur = conn.cursor()
#         cur.callproc('SP_Validate_College', [college_name])
#         cur.close()
#         conn.close()
#     except cx_Oracle.DatabaseError:
#         print('Failed to call SP_Validate_College')
#
#
# def check_for_premium():
#     try:
#         conn = cx_Oracle.connect(connect_string)
#         cur = conn.cursor()
#         cur.callproc('SP_Premium_Update_Check')
#         cur.close()
#         conn.close()
#     except cx_Oracle.DatabaseError:
#         print('Failed to call SP_Premium_Update_Check')
#
#
# def set_temp_to_standard():
#     try:
#         conn = cx_Oracle.connect(connect_string)
#         cur = conn.cursor()
#         cur.callproc('SP_Set_TempPremium_To_Std')
#         cur.close()
#         conn.close()
#     except cx_Oracle.DatabaseError:
#         print('Failed to call SP_Set_TempPremium_To_Std')
#
#
# def add_new_member():
#     try:
#         conn = cx_Oracle.connect(connect_string)
#         cur = conn.cursor()
#         cur.callproc('SP_Validate_Member')
#         cur.close()
#         conn.close()
#     except cx_Oracle.DatabaseError:
#         print('Failed to call SP_Validate_Member')
#
#
# def get_all_members():
#     members = []
#     test = []
#     try:
#         conn = cx_Oracle.connect(connect_string)
#         cur = conn.cursor()
#         cur.execute('select * from members')
#         for line in cur:
#             for data in line:
#                 test.append(data)
#             members.append(line)
#
#         cur.close()
#         conn.close()
#         return members
#     except cx_Oracle.DatabaseError:
#         print('Failed to call get members')
#
#
# def get_all_colleges():
#     members = []
#     test = []
#     try:
#         conn = cx_Oracle.connect(connect_string)
#         cur = conn.cursor()
#         cur.execute('select * from colleges')
#         for line in cur:
#             for data in line:
#                 test.append(data)
#             members.append(line)
#
#         cur.close()
#         conn.close()
#         return members
#     except cx_Oracle.DatabaseError:
#         print('Failed to call get colleges')
