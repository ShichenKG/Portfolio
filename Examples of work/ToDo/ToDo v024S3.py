##############################################
#    Manager        GUI        Database
# Shane Donivan, Lucas Dyer, Zach Townsend
# PM Class
# Seniors
# 10/13/21
# To Do List Program
# Creates a Table and loads info from a
# Database, can Add, Edit, & Delete Tasks
##############################################


# imports
import PySimpleGUI as sg
import ToDo_DBase as ToDo
import time
import io
from mysql.connector import Error

No_SelTask = True
table1 = False
table2 = False
table3 = False


# Functions
def AddTask():
    sg.theme('JRTI2')
    addT = [[sg.Text("Task Name:", justification='left'),
                      sg.Text("", size=11),
                      sg.Text("Due"),
                      sg.Text("", size=4),
                      sg.Text("Status")],
                     [sg.InputText("", size=25, key='-enterName-',background_color='#448ccf'),
                      sg.Input("", key='-timeAssign-', size=(10, 1), readonly=True,disabled_readonly_background_color='#448ccf'),
                      sg.Combo(Add_Status, key="-StatusComb-", size=10, readonly=True,background_color='#448ccf')],
                     [sg.Text("Description:")],
                     [sg.MLine("", size=(23, 5), key='-enterDesc-',background_color='#448ccf'),
                      sg.CalendarButton('', image_filename=calIcon, button_color=(('#38668f', '#38668f')), target='-timeAssign-', format='%m-%d-%y',
                                        default_date_m_d_y=(11, None, 2021), no_titlebar=False, key="-Calendar-"),
                      sg.Image(submitIcon, key="-Submission-", enable_events=True)]]
    win2 = sg.Window("Add Submission", addT, finalize=True)

    while True:
        event, values = win2.read()
        if event == sg.WINDOW_CLOSED or mainClose == True:
            break
        elif event == "-Submission-":
            try:
                Task_Name = values['-enterName-']
                Task_Desc = values['-enterDesc-']
                Task_Status = values['-StatusComb-']
                Task_Due_Date = values['-timeAssign-']
                print(Task_Name)
                Task_Start_Date = time.strftime("%Y-%d-%b")
                ToDo.Add_Task(Task_Name, Task_Desc, Task_Status, Task_Due_Date, Task_Start_Date)

                win2.close()
            except Error as e:
                print(e)
        # elif event == '-veryDescriptive-':
        elif event == '-enterDesc-':
            values['-enterDesc-'] = ""
        elif event == '-timeAssign-':
            event = "-Calendar-"
        else:
            sg.popup("Sorry user, I can't give functioning windows.\nCome back when you're a little... MMMM... richer!")

    # Updates the edit icon to appear disabled. Also disables it
    No_SelTask = True
    table1 = False
    table2 = False
    table3 = False
    window['-edit-'].update(editIcon)
    window['-edit2-'].update(editIcon)
    window['-edit3-'].update(editIcon)
    window['-subTask-'].update(sTaskIcon)
    window['-subTask2-'].update(sTaskIcon)
    window['-subTask3-'].update(sTaskIcon)
    window['-del-'].update(deleteIcon)
    window['-del2-'].update(deleteIcon)
    window['-del3-'].update(deleteIcon)

    window['-SystemOfATable-'].update(ToDo.GetTask_Active())
    window['-SystemOfATable2-'].update(ToDo.GetTask_Waiting())
    window['-SystemOfATable3-'].update(ToDo.GetTask_Completed())
    window['-descBox-'].update('')
    window['-subTable-'].update('')
    win2.close()


def EditTask(tName, dDate, Stats, Desc):
    sg.theme('JRTI2')
    editT = [[sg.Text("Task Name:", justification='left'),
                      sg.Text("", size=11),
                      sg.Text("Due"),
                      sg.Text("", size=4),
                      sg.Text("Status")],
                     [sg.InputText(tName, size=25, key='-enterName-', background_color='#448ccf'),
                      sg.Input(dDate, key='-timeAssign-', size=(10, 1), readonly=True, disabled_readonly_background_color='#448ccf'),
                      sg.Combo(Edit_Status, key="-StatusComb-", size=10, default_value=Stats, readonly=True, background_color='#448ccf')],
                     [sg.Text("Description:")],
                     [sg.MLine(Desc, size=(23, 5), key='-enterDesc-', background_color='#448ccf'),
                      sg.CalendarButton('', image_filename=calIcon, button_color=(('#2E75A6', '#2E75A6')), target='-timeAssign-', format='%m-%d-%y',
                                        default_date_m_d_y=(11, None, 2021), no_titlebar=False, key="-Calendar-"),
                      sg.Image(submitIcon, key="-Submission-", enable_events=True)]]
    win3 = sg.Window("Edit Submission", editT, finalize=True)

    while True:
        event, values = win3.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == "-Submission-":
            try:
                Task_Name = values['-enterName-']
                Task_Desc = values['-enterDesc-']
                Task_Status = values['-StatusComb-']
                Task_Due_Date = values['-timeAssign-']
                Task_Start_Date = time.strftime("%Y-%d-%b")

                ToDo.Edit_Task(tName, Task_Name, dDate, Task_Due_Date, Stats, Task_Status)
            except Error as e:
                print(e)

            break

        else:
            sg.popup("Sorry user, I can't give functioning windows.\nCome back when you're a little... MMMM... richer!")

    # Updates the edit icon to appear disabled. Also disables it
    No_SelTask = True
    table1 = False
    table2 = False
    table3 = False
    window['-edit-'].update(editIcon)
    window['-edit2-'].update(editIcon)
    window['-edit3-'].update(editIcon)
    window['-subTask-'].update(sTaskIcon)
    window['-subTask2-'].update(sTaskIcon)
    window['-subTask3-'].update(sTaskIcon)
    window['-del-'].update(deleteIcon)
    window['-del2-'].update(deleteIcon)
    window['-del3-'].update(deleteIcon)

    window['-SystemOfATable-'].update(ToDo.GetTask_Active())
    window['-SystemOfATable2-'].update(ToDo.GetTask_Waiting())
    window['-SystemOfATable3-'].update(ToDo.GetTask_Completed())
    window['-descBox-'].update('')
    window['-subTable-'].update('')

    win3.close()

    print("E")


def AddSubTask(T_Name):
    sg.theme('JRTI2')
    addSubT = [[sg.Text("SubTask", justification='left'),
                      sg.Text("", size=14),
                      sg.Text("Due"),
                      sg.Text("", size=4),
                      sg.Text("Status")],
                     [sg.InputText("Task", size=25, key='-enterName-', background_color='#448ccf'),
                      sg.Input(key='-timeAssign-', size=(10, 1), readonly=True,disabled_readonly_background_color='#448ccf'),
                      sg.Combo(Add_Status, key="-StatusComb-", size=10, readonly=True, background_color='#448ccf')],
                     [sg.MLine("Description", size=(23, 5), key='-enterDesc-', background_color='#448ccf'),
                      sg.CalendarButton('', image_filename=calIcon, button_color=(('#2E75A6', '#2E75A6')), target='-timeAssign-', format='%m-%d-%y',
                                        default_date_m_d_y=(11, None, 2021), no_titlebar=False, key="-Calendar-"),
                      sg.Image(submitIcon, enable_events=True, key="-Submit-")]]
    winsub = sg.Window("Add Subtask", addSubT, finalize=True)

    while True:
        event, values = winsub.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == "-Submit-":
            print("Sup")
            print(T_Name)
            Task_Name = T_Name
            print(Task_Name)
            Sub_Name = values['-enterName-']
            Sub_Desc = values['-enterDesc-']
            Sub_Status = values['-StatusComb-']
            Task_Due_Date = values['-timeAssign-']
            Task_Start_Date = time.strftime("%Y-%d-%b")
            ToDo.Add_SubTask(Task_Name, Sub_Name, Sub_Desc, Sub_Status)
            break
        # elif event == '-veryDescriptive-':
        elif event == '-enterDesc-':
            values['-enterDesc-'] = ""
        elif event == '-timeAssign-':
            event = "-Calendar-"
        else:
            sg.popup("Sorry user, I can't give functioning windows.\nCome back when you're a little... MMMM... richer!")
    No_SelTask = True
    table1 = False
    table2 = False
    table3 = False
    window['-edit-'].update(editIcon)
    window['-edit2-'].update(editIcon)
    window['-edit3-'].update(editIcon)
    window['-subTask-'].update(sTaskIcon)
    window['-subTask2-'].update(sTaskIcon)
    window['-subTask3-'].update(sTaskIcon)
    window['-del-'].update(deleteIcon)
    window['-del2-'].update(deleteIcon)
    window['-del3-'].update(deleteIcon)

    window['-SystemOfATable-'].update(ToDo.GetTask_Active())
    window['-SystemOfATable2-'].update(ToDo.GetTask_Waiting())
    window['-SystemOfATable3-'].update(ToDo.GetTask_Completed())
    window['-descBox-'].update('')
    window['-subTable-'].update('')

    winsub.close()



# Colors the window our colors
sg.LOOK_AND_FEEL_TABLE['JRTI'] = {'BACKGROUND': '#2E75B6',
                                  'TEXT': 'black',
                                  'INPUT': '#FFFFFF',
                                  'TEXT_INPUT': '#000000',
                                  'SCROLL': '#41719C',
                                  'BUTTON': ('white', '#345878'),
                                  'PROGRESS': ('#003058', '#FFFFFF'),
                                  'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 1,
                                  'TABLE': ''}

sg.LOOK_AND_FEEL_TABLE['JRTI2'] = {'BACKGROUND': '#2769a3',
                                  'TEXT': 'white',
                                  'INPUT': '#FFFFFF',
                                  'TEXT_INPUT': '#000000',
                                  'SCROLL': '#41719C',
                                  'BUTTON': ('white', '#2E75B6'),
                                  'PROGRESS': ('#003058', '#FFFFFF'),
                                  'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 1,
                                  'TABLE': ''}

sg.theme('JRTI')

# Image Variables
editIcon = ".//image/edit-icon_deactivate.png"
addIcon = ".//image/icon-add.png"
deleteIcon = ".//image/icon-delete_deactivate.png"
calIcon = ".//image/icon-calendar3.png"
submitIcon = ".//image/icon-submit5.png"
sTaskIcon = ".//image/subTask-icon_deactivate.png"

# Setup Variables for the Table
user = ""
description = ""
headers = ["   Assignment   ", "   Due Date   ", "    Status    "]
tableData = [["", "", ""]]
waitData = [["", "", ""]]
completeData = [["", "", ""]]
columnWidth = [50, 50, 25]
subHeaders = ["  Sub Assignment  ", "   Description   ", "    Status    "]
subtaskData = [["", "", ""]]
editDisable = True


# Tables for each section
Table1 = [[sg.Text("Assignments"),
            sg.Text("", size=40),
            sg.Text("Sub Tasks")],
           [sg.Table(tableData,
                     headings=headers,
                     row_height=17,
                     col_widths=columnWidth,
                     justification='left',
                     key='-SystemOfATable-',
                     enable_events=True,
                     background_color='#448ccf'),
            sg.Table(subtaskData,
                     headings=subHeaders,
                     row_height=17,
                     col_widths=columnWidth,
                     justification='left',
                     key='-subTable-',
                     enable_events=True,
                     background_color='#448ccf')],
           [sg.Text("Task Description: ", justification='left')],
           [sg.MLine(description, size=(57, 5), key='-descBox-', enable_events=True,disabled=True,background_color='#448ccf'),
            sg.Image(addIcon, enable_events=True, key='-add-'),  # Replace Image Buttons
            sg.Image(editIcon, enable_events=True, key='-edit-'),
            sg.Image(deleteIcon, enable_events=True, key='-del-'),
            sg.Image(sTaskIcon, enable_events=True, key='-subTask-')]]

Table2 = [[sg.Text("Assignments"),
            sg.Text("", size=40),
            sg.Text("Sub Tasks")],
           [sg.Table(waitData,
                     headings=headers,
                     row_height=17,
                     col_widths=columnWidth,
                     justification='left',
                     key='-SystemOfATable2-',
                     enable_events=True,
                     background_color='#448ccf'),
            sg.Table(tableData,
                     headings=subHeaders,
                     row_height=17,
                     col_widths=columnWidth,
                     justification='left',
                     key='-subTable2-',
                     enable_events=True,
                     background_color='#448ccf')],
           [sg.Text("Task Description: ", justification='left')],
           [sg.MLine(description, size=(57, 5),key='-descBox2-', enable_events=True,disabled=True,background_color='#448ccf'),
            sg.Image(addIcon, enable_events=True, key='-add2-'),  # Replace Image Buttons
            sg.Image(editIcon, enable_events=True, key='-edit2-'),
            sg.Image(deleteIcon, enable_events=True, key='-del2-'),
            sg.Image(sTaskIcon, enable_events=True, key='-subTask2-')]]

Table3 = [[sg.Text("Assignments"),
            sg.Text("", size=40),
            sg.Text("Sub Tasks")],
           [sg.Table(tableData,
                     headings=headers,
                     row_height=17,
                     col_widths=columnWidth,
                     justification='left',
                     key='-SystemOfATable3-',
                     enable_events=True,
                     background_color='#448ccf'),
            sg.Table(tableData,
                     headings=subHeaders,
                     row_height=17,
                     col_widths=columnWidth,
                     justification='left',
                     key='-subTable3-',
                     enable_events=True,
                     background_color='#448ccf')],
           [sg.Text("Task Description: ", justification='left')],
           [sg.MLine(description, size=(57, 5),key='-descBox3-', enable_events=True,disabled=True,background_color='#448ccf'),
            sg.Image(addIcon, enable_events=True, key='-add3-'),  # Replace Image Buttons
            sg.Image(editIcon, enable_events=True, key='-edit3-'),
            sg.Image(deleteIcon, enable_events=True, key='-del3-'),
            sg.Image(sTaskIcon, enable_events=True, key='-subTask3-')]]

tabbedLayout = [[sg.Image(".//image/todo9.png"),
                 sg.Text("", justification='left', expand_x=True),
                 sg.Image(".//image/logo_cropped.png")],
                [sg.TabGroup([[sg.Tab("Active", Table1, key='-Tab1-'),
                               sg.Tab("Waiting", Table2, key='-Tab2-'),
                               sg.Tab("Completed", Table3, key='-Tab3-')]],
                             key='-TabGroup-')],
                [sg.Text("", expand_x=True),
                 sg.Image(".//image/icon-exit3.png", key='-Exodus-', enable_events=True)]]

window = sg.Window("To-Do List", tabbedLayout, icon=".//image/list-icon.ico", finalize=True)

# Variables for Table part 2
late = True
onTime = False
add = False
edit = False

table1 = False
table2 = False
table3 = False

mainClose = False

Add_Status = ['Open', 'Started', 'Waiting on', 'Overdue']
Edit_Status = ['Open', 'Closed', 'Started', 'Waiting on', 'Overdue', 'Completed']
EditKeys = ['-edit-', '-edit2-', '-edit3-']

addKeys = ['-add-', '-add2-', '-add3-']
deleteKeys = ['-del-', '-del2-', '-del3-']
subTasks = ['-subTask-', '-subTask2-', '-subTask3-']

window['-SystemOfATable-'].update(ToDo.GetTask_Active())
window['-SystemOfATable2-'].update(ToDo.GetTask_Waiting())
window['-SystemOfATable3-'].update(ToDo.GetTask_Completed())


# Events for the main window
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == '-Exodus-':
        mainClose = True
        break
    elif event == '-SystemOfATable-':
        No_SelTask = False
        RowNum = values['-SystemOfATable-']
        Rows = window['-SystemOfATable-'].get()
        Row = int(RowNum[0])
        SelRow = (Rows[Row])
        Sub_Tasks = ToDo.Get_SubTasks(SelRow[0])
        Description = ToDo.Get_Task_Desc(SelRow[0])
        Description = list(Description)

        window['-subTable-'].update(Sub_Tasks)
        window['-descBox-'].update(Description[0][0])
        window['-edit-'].update(filename=".//image/edit-icon2.png")
        window['-subTask-'].update(filename=".//image/subTask-icon.png")
        window['-del-'].update(filename=".//image/icon-delete.png")
        table1 = True

    elif event == '-SystemOfATable2-':
        No_SelTask = False
        RowNum = values['-SystemOfATable2-']
        Rows = window['-SystemOfATable2-'].get()
        Row = int(RowNum[0])
        SelRow = (Rows[Row])
        Sub_Tasks = ToDo.Get_SubTasks(SelRow[0])
        Description = ToDo.Get_Task_Desc(SelRow[0])
        Description = list(Description)

        window['-subTable2-'].update(Sub_Tasks)
        window['-descBox2-'].update(Description[0][0])
        window['-edit2-'].update(filename=".//image/edit-icon2.png")
        window['-subTask2-'].update(filename=".//image/subTask-icon.png")
        window['-del2-'].update(filename=".//image/icon-delete.png")
        table2 = True

    elif event == '-SystemOfATable3-':
        No_SelTask = False
        RowNum = values['-SystemOfATable3-']
        Rows = window['-SystemOfATable3-'].get()
        Row = int(RowNum[0])
        SelRow = (Rows[Row])
        Sub_Tasks = ToDo.Get_SubTasks(SelRow[0])
        Description = ToDo.Get_Task_Desc(SelRow[0])
        Description = list(Description)

        window['-subTable3-'].update(Sub_Tasks)
        window['-descBox3-'].update(Description[0][0])
        window['-edit3-'].update(filename=".//image/edit-icon2.png")
        window['-subTask3-'].update(filename=".//image/subTask-icon.png")
        window['-del3-'].update(filename=".//image/icon-delete.png")
        table3 = True

    elif event in EditKeys:
        if No_SelTask:
            sg.popup("You have not selected a task.", keep_on_top=True, grab_anywhere=False, non_blocking=False)
        else:
            if table1:
                No_SelTask = True
                RowNum = values['-SystemOfATable-']
                Rows = window['-SystemOfATable-'].get()
                Row = int(RowNum[0])
                SelRow = (Rows[Row])

                tName = SelRow[0]
                dDate = SelRow[1]
                eStat = SelRow[2]

                Desc = ToDo.Get_Task_Desc(SelRow[0])
                Desc = list(Desc)
                Desc = Desc[0][0]

                EditTask(tName, dDate, eStat, Desc)

            elif table2:
                No_SelTask = True
                RowNum = values['-SystemOfATable2-']
                Rows = window['-SystemOfATable2-'].get()
                Row = int(RowNum[0])
                SelRow = (Rows[Row])

                tName = SelRow[0]
                dDate = SelRow[1]
                eStat = SelRow[2]

                Desc = ToDo.Get_Task_Desc(SelRow[0])
                Desc = list(Desc)
                Desc = Desc[0][0]

                EditTask(tName, dDate, eStat, Desc)

            elif table3:
                No_SelTask = True
                RowNum = values['-SystemOfATable3-']
                Rows = window['-SystemOfATable3-'].get()
                Row = int(RowNum[0])
                SelRow = (Rows[Row])

                tName = SelRow[0]
                dDate = SelRow[1]
                eStat = SelRow[2]

                Desc = ToDo.Get_Task_Desc(SelRow[0])
                Desc = list(Desc)
                Desc = Desc[0][0]

                EditTask(tName, dDate, eStat, Desc)
            table1 = False
            table2 = False
            table3 = False


    elif event in addKeys:
        AddTask()
    elif event in deleteKeys:
        if No_SelTask:
            sg.popup("You have not selected a task.")
        else:
            answer = sg.popup_yes_no("Are you sure you want to delete the selected item?")
            window['-edit-'].update(editIcon)
            window['-edit2-'].update(editIcon)
            window['-edit3-'].update(editIcon)
            window['-subTask-'].update(sTaskIcon)
            window['-subTask2-'].update(sTaskIcon)
            window['-subTask3-'].update(sTaskIcon)
            window['-del-'].update(deleteIcon)
            window['-del2-'].update(deleteIcon)
            window['-del3-'].update(deleteIcon)
            No_SelTask = True


            if answer == "Yes":
                ToDo.Delete_Task(SelRow[0])
                window['-SystemOfATable-'].update(ToDo.GetTask_Active())
                window['-SystemOfATable2-'].update(ToDo.GetTask_Waiting())
                window['-SystemOfATable3-'].update(ToDo.GetTask_Completed())
                window['-descBox-'].update('')
                window['-subTable-'].update('')
        # Updates the edit icon to appear disabled. Also disables it
        No_SelTask = True
        window['-edit-'].update(editIcon)
        window['-edit2-'].update(editIcon)
        window['-edit3-'].update(editIcon)

    elif event in subTasks:
        if No_SelTask:
            sg.popup("You have not selected a task.", keep_on_top=True, grab_anywhere=False, non_blocking=False)
        elif not No_SelTask:
            if table1:
                RowNum = values['-SystemOfATable-']
                Rows = window['-SystemOfATable-'].get()
                Row = int(RowNum[0])
                SelRow = (Rows[Row])
                T_Name = SelRow[0]
                AddSubTask(T_Name)
                print(T_Name)

            elif table2:
                RowNum = values['-SystemOfATable2-']
                Rows = window['-SystemOfATable2-'].get()
                Row = int(RowNum[0])
                SelRow = (Rows[Row])
                T_Name = SelRow[0]
                AddSubTask(T_Name)
                print(T_Name)

            elif table3:
                RowNum = values['-SystemOfATable3-']
                Rows = window['-SystemOfATable3-'].get()
                Row = int(RowNum[0])
                SelRow = (Rows[Row])
                T_Name = SelRow[0]
                AddSubTask(T_Name)
                print(T_Name)

            table1 = False
            table2 = False
            table3 = False

    else:
        print(event, values)
        print("The selected option does not work.\nCome back when you're a little... richer!")
print("\nEnd")
