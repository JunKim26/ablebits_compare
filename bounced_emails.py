# Title : Bounced Emails
# Author: Jun Kim
# Date: 12/22/2021
# Description: This program is a variation of the compare_two_tables program. A tkinter will be used to prompt a user to choose a csv file to retrieve data from.
# The user will then be prompted to choose a second file to compare the email addresses from entries in the first file.
# If the email addresses match, respective IDs will be written in to the new file.

import pandas as pd                                                        
import os                                                                   
import tkinter as tk                                                        
from tkinter import *                                                    
from tkinter.filedialog import askopenfilename
from datetime import datetime                                             


window = tk.Tk()                                                            
window.geometry('200x200')                                                  

label = tk.Label(text='CSV Campaign')                                       
label.pack()

def csv_opener():
    """ this function is used for the button to open the csv file """
    global csv_name
    global csv_file
    global csv_df

    csv_name = askopenfilename()                                            
    csv_file = open(csv_name, 'r')		                                    
    csv_data = pd.read_csv(csv_file) 
    csv_df = pd.DataFrame(csv_data)  

    return None

def comparison_opener():
    """ this function is used for the button to open the ids file """
    global ids_name
    global ids_file
    global ids_df
    

    ids_name = askopenfilename()
    ids_file = open(ids_name,'r')                                                                      
    ids_data = pd.read_csv(ids_file)
    ids_df = pd.DataFrame(ids_data)    

    end_button = Button(window, text = 'Create', command =window.destroy).pack()

    return None


def main():
    
    # Buttons that will show up on the tkinter window for user
    csv_button = Button(window, text = 'Open CSV File', command = csv_opener).pack() 
    ids_button = Button(window, text = 'Open Comparison File', command = comparison_opener).pack()

    window.mainloop()
    
    # year_month_day-hours_minutes_seconds_AM/PM ; used in Title    
    dt = datetime.now().strftime('%Y_%m_%d-%I_%M_%S_%p')                                                                        

    input_file = os.path.basename(csv_name)
    file_name = str(dt) +" Matches from " + input_file                      

    script_dir = os.path.dirname(__file__)                                  
    rel_path = 'Output'
    
    # this joins the absolute path of current script with wanted relative path
    abs_file_path = os.path.join(script_dir, rel_path)                      

    bounced_emails = []
    bad_household_ID = []

    csv_second_column = csv_df.columns[1]
    
    # for loop to find the matching household id to the email
    for email in ids_df['Bounced Emails']:                                  
        bounced_emails.append(email)

    for i in range(len(csv_df['Household ID'])):
        if csv_df[csv_second_column][i] in bounced_emails:
            
            new_data = csv_df['Household ID'][i]
            bad_household_ID.append(new_data)

    bounced_emails_match_ids = pd.DataFrame(bad_household_ID,
                                            columns=['Household ID'])

    bounced_emails_match_ids[csv_second_column] = ''

    with open(abs_file_path+'/'+file_name, 'w',newline='') as new_file:	    

        bounced_emails_match_ids.to_csv(new_file, index=False)              

        csv_file.close()
        ids_file.close()

        
if __name__ == '__main__':
    main()



