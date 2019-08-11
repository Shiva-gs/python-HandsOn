import os
import csv
import datetime
file = './employee_data.csv'
States = './50States.csv'
split_name = []
states_dict={} 
data_list=[] 
row_lst = [] 
str_rp= ''
 
with open(States,newline="") as states_file:
    csv_data= csv.reader(states_file,delimiter=",")
    head = next(csv_data)
    for row in csv_data:
        states_dict[row[0]] = [row[1]]
 
 
with open(file,newline="") as csv_file:
    csv_data= csv.reader(csv_file,delimiter=",")
    head = next(csv_data)
    for row in csv_data:
        #The `Name` column should be split into separate `First Name` and `Last Name` columns
        #replace name if any special char like dot are present with space
        split_name = row[1].replace('.',' ')
        split_name = split_name.split(' ') 
        row_lst.append(row[0]) 
        row_lst.append(split_name[0]) 
        row_lst.append(split_name[1])
        split_name = []
        #convert the date format 
        row_lst.append(datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%Y'))
        #Str replace to mask SSN 
        #Get the substring of first 6 character to mask
        str_chg = row[3]
        str_rp = str_chg[0:6]
        str_chg = str_chg.replace(str_rp,'***-**')
        row_lst.append(str_chg)
      
        # Get STATE code from the list 
        #remove quotes 
        row_lst.append(''.join(states_dict[row[4]]))
        # Assign row_lst to 
        data_list.append(row_lst)
        #reset row_lst
        row_lst = []


# Write to a file
out_file = './modified_HR_data.csv'

#  Open the output file
with open(out_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    # Write in zipped rows 
    writer.writerow(["EmpID", "First Name", "Last Name", "DOB",
                     "SSN", "State"])
    writer.writerows(data_list)

