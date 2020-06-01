import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#set variables
No_of_month = 0
Total_Profit = 0
Total_Change = 0
last_month_profit = 0
first_month = 0
index = 1
Max = 0
Min = 0
previous_month = 0

#Opens the CSV file
with open(csvpath,"r") as budget:
    csv_reader = csv.reader(budget,delimiter = ",")
# separates the header row
    csv_header = next(csv_reader)
    for row in csv_reader:
    #Count the number of month
        No_of_month += 1
    #Sum the average change per month
        this_month_profit = int (row[1])
        if previous_month != 0:
            change = this_month_profit - previous_month
        else:
            change = 0
        previous_month = int(this_month_profit)
        Total_Change = change + Total_Change
        Total_Profit = Total_Profit + this_month_profit
       # determine the Max and Min
        if change > Max:
            Max = change
            Max_Month = str(row[0]) 
            Max_change = int(change)    
        elif change < Min:
            Min = change
            Min_Month = str(row[0])  
            Min_change = int(change)
                 
#Average change per month
Average = float(Total_Change / (No_of_month-1))
# Open the txt file, and write report in it
output_path = os.path.join('..','PyBank','PyBank.txt')

with open(output_path, "w", newline = '') as txt_file:
    txt_file.write("Financial Analysis \n") 
    txt_file.write("---------------------------- \n") 
    txt_file.write(f"Total Months: {No_of_month} \n")
    txt_file.write(f"Total : {Total_Profit} \n")
    txt_file.write(f"Average Change : {Average} \n")
    txt_file.write(f"Greatest Increase in Profits : {Max_Month} ($ {Max_change} \n")  
    txt_file.write(f'Greatest Decrease in Profits : {Min_Month} ($ {Min_change})')

#Print the results on GitBash
       
print("Financial Analysis")
print("----------------------------------")
print(f'Total Months : {No_of_month}')
print(f'Total : $ {Total_Profit}')
print(f'Average Change : {Average}')
print(f'Greatest Increase in Profits : {Max_Month} ($ {Max_change})')
print(f'Greatest Decrease in Profits : {Min_Month} ($ {Min_change})')
# Specify the file to write to

