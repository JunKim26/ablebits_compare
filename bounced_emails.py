# Title : Bounced Emails
# Author: Jun Kim
# Date: 12/22/2021
# Description: This program is a variation of the compare_two_tables program. A tkinter will be used to prompt a user to choose a csv file to retrieve data from.
# The user will then be prompted to choose a second file to compare the email addresses from entries in the first file.
# If the email addresses match, respective IDs will be written in to the new file.

import pandas as pd                                             # used to create dataframes
import numpy as np   
import os                                                       # used to create relative path to write file
from datetime import date                                       # used to get the current date
from datetime import datetime                                   # used to get date and time
import tkinter as tk                                            # used as a user friendly tool for the program
from tkinter.filedialog import askopenfilename
from tkinter import StringVar
from tkinter import *

window = tk.Tk()                                                # creates a tkinter object
window.geometry('200x200')                                      # set size of tkinter window

label = tk.Label(text='CSV Campaign')                           # sets the text to be dipslayed by tkinter
label.pack()

def csv_opener():
    """ this function is used for the button to open the csv file """
    global csv_name
    global csv_file
    global csv_df

    csv_name = askopenfilename()                                # show an "Open" dialog box and return the path to the selected file
    csv_file = open(csv_name, 'r')		                        # opens excel csv file to read
    csv_data = pd.read_csv(csv_file) 
    csv_df = pd.DataFrame(csv_data)  

    return None

def comparison_opener():
    """ this function is used for the button to open the ids file """
    global ids_name
    global ids_file
    global ids_df
    

    ids_name = askopenfilename()
    ids_file = open(ids_name,'r')                               # opens csv file of ids in specific campaign to read                            
    ids_data = pd.read_csv(ids_file)
    ids_df = pd.DataFrame(ids_data)    

    end_button = Button(window, text = 'Create', command =window.destroy).pack()

    return None

                                                                # Buttons that will show up on the tkinter window for user
csv_button = Button(window, text = 'Open CSV File', command = csv_opener).pack()

ids_button = Button(window, text = 'Open Comparison File', command = comparison_opener).pack()

window.mainloop()

dt = datetime.now().strftime('%Y_%m_%d-%I_%M_%S_%p')            # year_month_day-hours_minutes_seconds_AM/PM ; used in Title
current_date = date.today().strftime('%Y-%b-%d')                # year-month-day                             ; used in last column
dt_string = str(dt)                                             # string of date and time
today_string = str(current_date)                                # string of date

extension = '.csv'                                          

input_file = os.path.basename(csv_name)
file_name = dt_string +" Matches from " + input_file + extension         # sets the file name 

script_dir = os.path.dirname(__file__)                          # absolute directory the script is in
rel_path = 'Output'
abs_file_path = os.path.join(script_dir, rel_path)              # this joins the absolute path of current script with wanted relative path

bounced_emails = []
bad_household_ID = []

csv_second_column = csv_df.columns[1]

for email in ids_df['EmailAddress']:                                                                # for loop to find the mating household id to the email
    bounced_emails.append(email)

for i in range(len(csv_df['Household ID'])):
    if csv_df[csv_second_column][i] in bounced_emails:
        
        new_data = csv_df['Household ID'][i]
        bad_household_ID.append(new_data)

        #bounced_emails_match_ids.append(new_data, ignore_index = True)

bounced_emails_match_ids = pd.DataFrame(bad_household_ID,
                                        columns=['Household ID'])

bounced_emails_match_ids[csv_second_column] = ''

with open(abs_file_path+'/'+file_name, 'w',newline='') as new_file:	                    # creates csv to write in

    bounced_emails_match_ids.to_csv(new_file, index=False)                                                # writes the dataframe into the new file without the indices

    csv_file.close()
    ids_file.close()


