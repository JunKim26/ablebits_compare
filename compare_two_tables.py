
import pandas as pd                                                        
import os                                                                   # used to create relative path to write file
import tkinter as tk                                                        # used as a user friendly tool for the program
from tkinter import *                                                    
from tkinter.filedialog import askopenfilename
from datetime import datetime                                             


# =======================================================================================================================================================
#                                                           Script lines for Tkinter GUI
# =======================================================================================================================================================

window = tk.Tk()                                                            # creates a tkinter object
window.geometry('200x200')                                                  # set size of tkinter window

label = tk.Label(text='CSV Campaign')                                       # sets the text to be dipslayed by tkinter
label.pack()

def csv_opener():
    """ this function is used for the button to open the csv file """
    global csv_name
    global csv_file
    global csv_df

    csv_name = askopenfilename()                                            # show an "Open" dialog box and return the path to the selected file
    csv_file = open(csv_name, 'r')		                                    # opens the csv file to read
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

# =======================================================================================================================================================
#                                                           Main Function Section
# =======================================================================================================================================================

def main():
                                                                            # Buttons that will show up on the tkinter window for user
    csv_button = Button(window, text = 'Open CSV File', command = csv_opener).pack() 
    ids_button = Button(window, text = 'Open Comparison File', command = comparison_opener).pack()

    window.mainloop()

    dt = datetime.now().strftime('%Y_%m_%d-%I_%M_%S_%p')                    # year_month_day-hours_minutes_seconds_AM/PM ; used in Title                                                            

    input_file = os.path.basename(csv_name)
    file_name = str(dt) +" Matches from " + input_file                      # sets the file name 

    script_dir = os.path.dirname(__file__)                                  # absolute directory the script is in
    rel_path = 'Output'
    abs_file_path = os.path.join(script_dir, rel_path)                      # this joins the absolute path of current script with wanted relative path

    comparison_values = []
    matched_IDs = []

    csv_second_column = csv_df.columns[1]

    for i in ids_df['Comparison Values']:                               # The name of the column that contains the comparison values
        comparison_values.append(i)

    for i in range(len(csv_df['ID'])):                                      # Primary ID 
        if csv_df[csv_second_column][i] in comparison_values:
            
            new_data = csv_df['ID'][i]
            matched_IDs.append(new_data)

    matched_IDs_df = pd.DataFrame(matched_IDs, columns=['ID'])

    matched_IDs_df[csv_second_column] = ''

    with open(abs_file_path+'/'+file_name, 'w',newline='') as new_file:	    # creates csv to write in

        matched_IDs_df.to_csv(new_file, index=False)                        # writes the dataframe into the new file without the indices

        csv_file.close()
        ids_file.close()

if __name__ == '__main__':
    main()

