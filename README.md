# Description


In this program, a GUI will mimic the function of the compare tables in Ablebits. Once the program is run, a tkinter will be used to prompt a user to choose two CSV files. 
One file will contain the primary keys and another column with values for commparison. The second value will contain the values we are comparing with the first CSV file. 
The resulting output file will contain only the rows that had a matching value and save to a folder with a timestamp. 
In order to reduce the time complexity, an array is used to hold the values of the bounced emails. This addition makes it so that a nesting loop is no longer needed.

*Note: The bounced_emails is a varaition of the compare_two_tables program with the purpose of finding household ID's with emails that need to be deleted from a database. 
