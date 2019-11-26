# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Nicholas Goodwin, 11/12/2019, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionary.
# TODO: Add Code Here
objFile = open("ToDoList.txt", "r")
for line in objFile:
    strData = line.split(",")
    dicRow = {"Task": strData[0], "Priority": strData[1]}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for row in lstTable:
            print(row["Task"] + ', ' + row["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = str(input("What is your task?: "))
        strPriority = str(input("What is the level of Priority?: "))
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        for dicRow in lstTable:
            print(dicRow)
        continue
    # Step 5 - Remove a new item to the list/Table
    elif (strChoice.strip() == '3'):
        task = input("What task do you want me to delete?: ")
        if (any(i['Task'] == task for i in lstTable)):
            lstTable = [i for i in lstTable if not (i['Task'] == task)]
        #if Task in objFile:
        #    del objFile[Task]
        #    print("\nThat task has been deleted" - Task)
        else:
            print("\nI was unable to delete", Task, "since it doesn't exist in the dictionary.")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        for row in lstTable:
            print(row["Task"] + ", " + row["Priority"])
        if("y" == str(input("Save this data? (y/n) "))):
            objFile = open("ToDoList.txt", "w")
            for dicRow in lstTable:
                objFile.write(dicRow["Task"] + ", " + dicRow["Priority"] + "\n")
            objFile.close()
            print("Data has been saved.")
        else:
            input("Data was not saved.")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        break  # and Exit the program
