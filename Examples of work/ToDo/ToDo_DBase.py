from mysql.connector import connect, Error
import mysql.connector
from mysql.connector import errorcode
from mysql.connector import Error


###################################
# Other
###################################
def get_Connection():
    try:
        connection = mysql.connector.connect(
            host="10.227.160.116",
            user="student",
            password="5249",
            database="jrti-todo",
            port="3306"
        )
        return connection
    except Error as e:
        print(e)


def Get_Current_Date():
    task_Sql = f"select current_date();"
    connection = get_Connection()
    cursor = connection.cursor()
    try:
        cursor.execute(task_Sql)
        task_List = cursor.fetchall()
        cursor.close()
        return task_List

    except Error as e:
        print(e)


###################################
# Sub Tasks
###################################
def Add_SubTask(Task_Name, Sub_Name, Sub_DDate, Sub_Desc, Sub_Status):
    task_Sql = f"insert into sub_task (Name, Sub_Name, Sub_DDate, Sub_Desc, Sub_Status) values('{Task_Name}','{Sub_Name}', '{Sub_DDate}', '{Sub_Desc}', '{Sub_Status}')"
    connection = get_Connection()
    cursor = connection.cursor()
    cursor.execute(task_Sql)
    connection.commit()
    cursor.close()
    return True


def Add_SubTask_NoDDate(Task_Name, Sub_Name, Sub_Desc, Sub_Status):
    task_Sql = f"insert into sub_task (Name, Sub_Name, Sub_Desc, Sub_Status) values('{Task_Name}','{Sub_Name}', '{Sub_Desc}', '{Sub_Status}')"
    connection = get_Connection()
    cursor = connection.cursor()
    cursor.execute(task_Sql)
    cursor.close()
    return True


def Get_SubTask_Data():
    try:
        connection = mysql.connector.connect(
            host="10.227.160.116",
            user="student",
            password="5249",
            database="jrti-todo",
            port="3306"
        )
        connected = True
    except Error as e:
        print(e)

    task_Sql = f"select * from sub_task;"

    if connected:
        try:
            cursor = connection.cursor()
            cursor.execute(task_Sql)
            sInfo = cursor.fetchall()
            if len(sInfo) == 0:
                print("Nothing Found")
            else:
                print(sInfo)
                return sInfo

        except Error as e:
            print(e)
            return e


def Edit_Subs_FromTask(Task_Name):
    task_Sql = f"update sub_task set Name = '{Task_Name}'"
    connection = get_Connection()
    cursor = connection.cursor()
    cursor.execute(task_Sql)
    connection.commit()
    cursor.close()


def Delete_Subs_FromTask(Delete):
    task_Sql = f"delete from sub_task where Name = '{Delete}'"
    connection = get_Connection()
    cursor = connection.cursor()
    cursor.execute(task_Sql)
    connection.commit()
    cursor.close()


def Delete_Sub_Task(Delete):
    task_Sql = f"delete from sub_task where Sub_Name = '{Delete}'"
    connection = get_Connection()
    cursor = connection.cursor()
    cursor.execute(task_Sql)
    connection.commit()
    cursor.close()


def Get_SubTasks(Task_Name):
    task_Sql = f"select Sub_Name,Sub_DDate,Sub_Status from sub_task where Name = '{Task_Name}';"
    connection = get_Connection()
    cursor = connection.cursor()
    try:
        cursor.execute(task_Sql)
        task_List = cursor.fetchall()
        cursor.close()
        return task_List

    except Error as e:
        print(e)


def Edit_SubTask(tName, Task_Name, dDate, Task_DDate, status, Task_Status):
    task_Sql = f"update sub_task set Sub_Name='{Task_Name}', Sub_DDate='{Task_DDate}', Sub_Status='{Task_Status}' where Sub_Name='{tName}' and Sub_DDate='{dDate}' and Sub_Status='{status}'"
    connection = get_Connection()
    cursor = connection.cursor()
    cursor.execute(task_Sql)
    connection.commit()
    cursor.close()


def Get_Sub_Desc(Task_Name):
    task_Sql = f"select Sub_Desc from sub_task where Sub_Name = '{Task_Name}';"
    connection = get_Connection()
    cursor = connection.cursor()
    try:
        cursor.execute(task_Sql)
        task_List = cursor.fetchall()
        cursor.close()
        return task_List

    except Error as e:
        print(e)


def Edit_Sub_Late(Current_Date):
    task_Sql = f"update sub_task set Sub_Status='Overdue' where '{Current_Date}'>Sub_DDate"
    connection = get_Connection()
    cursor = connection.cursor()
    cursor.execute(task_Sql)
    connection.commit()
    cursor.close()


###################################
# Tasks
###################################
def Add_Task(Task_Name, Description, Status, Due_Date, Start_Date):
    task_Sql = f"insert into task (Name,Description,Status,Due_Date, Start_Date) values('{Task_Name}', '{Description}', '{Status}', '{Due_Date}', '{Start_Date}')"
    connection = get_Connection()
    cursor = connection.cursor()
    cursor.execute(task_Sql)
    connection.commit()
    cursor.close()
    return True


def Add_Task_NoDDate(Task_Name, Description, Status):
    task_Sql = f"insert into task (Name,Description,Status) values('{Task_Name}', '{Description}', '{Status}')"
    connection = get_Connection()
    cursor = connection.cursor()
    cursor.execute(task_Sql)
    connection.commit()
    cursor.close()
    return True


def Delete_Task(Delete):
    task_Sql = f"delete from task where Name = '{Delete}'"
    connection = get_Connection()
    cursor = connection.cursor()
    cursor.execute(task_Sql)
    connection.commit()
    cursor.close()


def Get_Task_Desc(Task_Name):
    task_Sql = f"select Description from task where Name = '{Task_Name}';"
    connection = get_Connection()
    cursor = connection.cursor()
    try:
        cursor.execute(task_Sql)
        task_List = cursor.fetchall()
        cursor.close()
        return task_List

    except Error as e:
        print(e)


def Get_Task_Date(Task_Name):
    task_Sql = f"select Due_Date from task where Name = '{Task_Name}';"
    connection = get_Connection()
    cursor = connection.cursor()
    try:
        cursor.execute(task_Sql)
        task_List = cursor.fetchall()
        cursor.close()
        return task_List
    except Error as e:
        print(e)


def GetTask_Active():
    task_Sql = f"select Name,Due_Date,Status from task where Status != 'Completed';"
    connection = get_Connection()
    cursor = connection.cursor()
    try:
        cursor.execute(task_Sql)
        task_List = cursor.fetchall()
        cursor.close()
        return task_List

    except Error as e:
        print(e)


def GetTask_Completed():
    task_Sql = f"select Name,Due_Date,Status from task where Status = 'Completed';"
    connection = get_Connection()
    cursor = connection.cursor()
    try:
        cursor.execute(task_Sql)
        task_List = cursor.fetchall()
        cursor.close()
        return task_List

    except Error as e:
        print(e)


def GetTask_Waiting():
    task_Sql = f"select Name,Due_Date,Status from task where Status = 'Waiting on';"
    connection = get_Connection()
    cursor = connection.cursor()
    try:
        cursor.execute(task_Sql)
        task_List = cursor.fetchall()
        cursor.close()
        return task_List

    except Error as e:
        print(e)


def GetTask_Data(Task_Name):
    try:
        connection = mysql.connector.connect(
            host="10.227.160.116",
            user="student",
            password="5249",
            database="jrti-todo",
            port="3306"
        )
        connected = True
    except Error as e:
        print(e)

    task_Sql = f"select Due_Date from task where Name = '{Task_Name}';"

    if connected:
        try:
            cursor = connection.cursor()
            cursor.execute(task_Sql)
            sInfo = cursor.fetchall()
            if len(sInfo) == 0:
                print("Nothing Found")
            else:
                return sInfo

        except Error as e:
            print(e)
            return e


def Edit_Task(tName, Task_Name, tDesc, Desc, dDate, Task_DDate, status, Task_Status):
    task_Sql = f"update task set Name='{Task_Name}', Description='{Desc}, Due_Date='{Task_DDate}', Status='{Task_Status}' where Name='{tName}' and Description='{tDesc}' and Due_Date='{dDate}' and Status='{status}'"
    connection = get_Connection()
    cursor = connection.cursor()
    cursor.execute(task_Sql)
    connection.commit()
    cursor.close()


def Edit_Task_Late(Current_Date):
    task_Sql = f"update task set Status='Overdue' where '{Current_Date}'>Due_Date;"
    connection = get_Connection()
    cursor = connection.cursor()
    cursor.execute(task_Sql)
    connection.commit()
    cursor.close()


def Edit_Task_NoDDate(tName, Task_Name, Desc, Task_Status):
    task_Sql = f"update task set Name='{Task_Name}', Description='{Desc}, Status='{Task_Status}' where Name='{tName}'"
    connection = get_Connection()
    cursor = connection.cursor()
    cursor.execute(task_Sql)
    connection.commit()
    cursor.close()
