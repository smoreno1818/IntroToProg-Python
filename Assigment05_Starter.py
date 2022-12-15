# ------------------------------------------------------------------------ #
# Title: Starterwithcommentary.py
# Description: Working with Dictionaries and Lists.
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Sebastian Moreno,2022-11-16,Updated from original script provided):
# MMoreno,11.16.2022,Created file with script provided
# MMoreno,11.16.2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
table = []

File = open(objFile, "r")
for row in File:
    lstRow = row.split(",")  # returns a list
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1]}
    table.append(dicRow)
File.close()

print(table)




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
        for dicRow in table:
            print(dicRow['Task'] + "," + dicRow['Priority'].strip("\n"))
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        newtaskrequest = input("Add a new task to the List/Table: ")
        newpriorityrequest = input("Add a new priority to the List/Table: ")
        table.append({"Task": newtaskrequest, "Priority": newpriorityrequest})


    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        for i in range(len(table)):
            print(str(i) + '. ' + str(table[i]).strip("\n"))

        userinput = input("Which item do you want to remove from the list: ")

        del table[int(userinput)]
        print("Removed Item Number is: " + userinput)


    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        savingdata = input("Do you want to save the tasks to the ToDoToDoList.txt file? [y, n]: ")
        if savingdata == "y":
            file = open(objFile, 'w')
            for row in table:
                file.write(row['Task'] + ',' + row['Priority'])
            file.close()

        elif savingdata == "n":
            break




    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Exiting")
        break  # and Exit the program
