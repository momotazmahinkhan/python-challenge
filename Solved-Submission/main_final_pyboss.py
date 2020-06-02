import os
import csv
import USstateabv

pyboss_csv = os.path.join("..", "Resources", "employee_data.csv")

# Lists to store data

Emp_ID= []
First_Name = []
Last_Name = []
Date_of_Birth = []
New_SSN = []
State = []

# with open(pyboss_csv, encoding='utf-8') as csvfile:
with open(pyboss_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_Header =next(csvreader)  
    for row in csvreader:
       # Add Emp_ID
        Emp_ID.append(row[1])

        #Split name
        name_split = row[1].split(" ")
        First_Name.append(name_split[0])
        Last_Name.append(name_split[1])
        #print(name_split)
        
       # DOB.append(row[0])
        DOB = (row[2])
        converted_Birth = str(DOB[5:7]) + "/" + str (DOB[9:]) + "/"+ str(DOB[:4])
        Date_of_Birth.append(converted_Birth)
        
        SSN = (row[3])
        converted_SSN =  "*** - **" + str(SSN[7:])
        New_SSN.append(converted_SSN)

        # Add States
        s = row[4]
        abv = (USstateabv.USstateabv[s])
        State.append(abv)
        # Zip lists together
NewEmployee_csv = zip(Emp_ID, First_Name, Last_Name, Date_of_Birth, New_SSN, State)

# Set variable for output file
output_file = os.path.join("Mahin_final.csv")

#  Open the output file
with open(output_file, "w", newline= '') as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Emp_ID", "First_Name", "Last_Name", "Date of Birth","SSN", "State"])

    # Write in zipped rows
    writer.writerows(NewEmployee_csv)