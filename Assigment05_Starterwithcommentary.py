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

#The first step was to declare variables and constants that may be used within the program.
#Since I was utilizing my Professors file I made sure to only leave and include the varaibles and
#constants that I was actually using. The ones I was not I ended up deleting.

#The first variable ObjFile was referencing the text file ToDoList. The second variable dicRow was referencing
# a dictionary which included a task and priority. And the third variable within this section was referencing
#which string or option would be selected.


# -- Data -- #
# declare variables and constant
objFile = "ToDoList.txt"   # An object that represents a file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
strChoice = "" # A Capture the user option selection

#The first step that I did was to create an empty list called table.
#This table was where I would enter user entries in the form of rows with our dictionaries containing tasks
#and priorities.

#For the next part of step one, I created a variable that opened the text file with the intent to read.


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# Added code below
table = []

File = open(objFile, "r")


#The next section of code iterates over each row in the file and then grabs the lstrow and splits it at the
#comma. The dicRow is created from the two pieces of the split and show the respective task and priority.
#The table.append(dicRow) command adds the dictionary to the table. The remaining command closes the file
#and we then print the table or as a result the various dictionaries.

for row in File:
    lstRow = row.split(",")  # returns a list
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1]}
    table.append(dicRow)
File.close()

print(table)



#For step two I used a while loop that was equal to true which as a result would run until a
#condition stated it was broken occured. This While loop statement printed out our menu options.

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

    #Afterward, we used the variable which we had used in the past known as strChoice which helped us save the
    #user response which was either 1,2,3,4, or 5 in order for the program to function properly.

    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table

    #For the next section, I was tasked with creating an action that would occur based on the user's
    #input.

    #If the user inputted 1 then I would show the current data in the table or various dictionaries through a
    #print function. These values would be shown separately (the task and priority) and were conncatenated by a comma.
    #I made sure to include a strip function in order to ensure the new lines appearing when the program ran dissappeared.


    if (strChoice.strip() == '1'):
        for dicRow in table:
            print(dicRow['Task'] + "," + dicRow['Priority'].strip("\n"))
    # Step 4 - Add a new item to the list/Table

    # If the user did not enter one, I used an else if function which would search for a two as the input from the user.
    #This would add a new option through two input functions requesting a new task and new priority to the table.
    #Through table.append I would add the new task and priority inputted by the user to the respective table.

    elif (strChoice.strip() == '2'):
        newtaskrequest = input("Add a new task to the List/Table: ")
        newpriorityrequest = input("Add a new priority to the List/Table")
        table.append({"Task": newtaskrequest, "Priority": newpriorityrequest})


#If the user did not input two and inputted three, thye would be looking to remove an existing item.
    #I was able to do this by identifying there number three as what they inputted through an else if function.



    # Step 5 - Remove a new item from the list/Table

    #The first section of this code to remove a list or table began with the unique variable I chose called "i"
    #or index in order to iterate over each item of the table while also keeping track of the index of the table.
    #I would then print the index or "i" which is conncatenated by the row in the table at index "i". I also
    #made sure to include a strip in order to remove the extra empty line shown.

    elif (strChoice.strip() == '3'):
        for i in range(len(table)):
            print(str(i) + '. ' + str(table[i]).strip("\n"))

#After asking the user which item they would like to remove from the list through an input function assigning
        #this value to a varaible caled userinput I would then take that number inputted and delete the row from
        #the table which has the same index value as the number.


        userinput = input("Which item do you want to remove from the list: ")

        del table[int(userinput)]

        #The user would then also receive a message stating which item number was removed which referenced the
        #userinput variable.

        print("Removed Item Number is: " + userinput)


#The next option in the menu was to save the data to the text file if the user inputted a four.

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):

      #I did this by asking if the user wanted to save the tasks to the respective text file through a y or n input.
      #Through using an if statement referencing savingdata wich was the user inputted value if it was equal
      #to y then the name of the text file stored in objFile would be opened to write as dictated by the
      #w shown.

        savingdata = input("Do you want to save the tasks to the ToDoToDoList.txt file? [y, n]: ")
        if savingdata == "y":
            file = open(objFile, 'w')

           #I then used a for loop to iterate over each row in the table. For each row in the table the task and
            # prioritiy were conncatenated and written to the file.

            for row in table:
                file.write(row['Task'] + ',' + row['Priority'])

            #The file was then closed.

            file.close()

#If the user inputted an n, I simply used an else if function that checked the condition on
        # if savingdata was equal to n which then broke the while loop so it would not be true and would
        #stop running.



        elif savingdata == "n":
            break



#The final step in the program was to exit the program. This was done through an else if statement which
    #checked if the string choice was equal to 5 and if this was the case then the program would print
    # "Exiting" and the while loop would break.

    #I included a strip function in case the user happened to write extra white spaces so that they would be removed

    #This was the end of the program.

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Exiting")
        break  # and Exit the program

