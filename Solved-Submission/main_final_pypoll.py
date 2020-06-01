import os
import csv

csvpath = os.path.join('..', 'Resources', 'Election_data.csv')

#set variables
Total_Votes = 0
candidate_votecount = [0, 0, 0, 0]
candidate_namelist = []
percentage_Khan = 0
percentage_Correy = 0
percentage_Li = 0
percentage_Otooley = 0
percentage = [0, 0, 0, 0]

#open the file and read the file
with open(csvpath,"r") as election:
    csv_reader = csv.reader(election,delimiter = ",")
    csv_header = next(csv_reader)
    for row in csv_reader:
        candidate_name = row[2]
        Total_Votes += 1
        
        if candidate_name not in candidate_namelist:
            candidate_namelist.append(row[2])
        else:
            pass
        if row[2] == "Khan":
            candidate_votecount[0] += 1
        elif row[2] == "Correy":
            candidate_votecount[1] += 1
        elif row[2] == "Li":
            candidate_votecount[2] += 1
        elif row[2] =="O'Tooley":
            candidate_votecount[3] += 1

print(candidate_namelist)
print(f"Total Votes cast : {Total_Votes}")
print(f'candidate vote count : {candidate_votecount}')
#percentage of votes cast for each candidate
percentage[0] = round((int(candidate_votecount[0]) / Total_Votes) * 100, 3)
percentage[1] = round( (int(candidate_votecount[1]) / Total_Votes) * 100, 3)
percentage[2] = round((int(candidate_votecount[2]) / Total_Votes) * 100, 3)
percentage[3] = round((int(candidate_votecount[3]) / Total_Votes) * 100, 3)
print(f' Percentage : {percentage}')
Winner = percentage[0]
if Winner < percentage[1]:
    Winner = percentage[1]
if Winner < percentage[2]:
    Winner = percentage[2]
if Winner < percentage[3]:
    Winner = percentage[3]

    # CREATE REPORT FILE
# Specify the file to write to
output_path = os.path.join('..','Pypoll','PyPoll.txt')

# Open the txt file, and write report in it
with open(output_path, "w", newline = '') as txt_file:
    txt_file.write("Election Results \n") 
    txt_file.write("---------------------------- \n") 
    txt_file.write(f"Total Votes: {Total_Votes} \n")
    txt_file.write("---------------------------- \n") 
    txt_file.write(f'Khan: {percentage[0]}% ({candidate_votecount[0]})\n')
    txt_file.write(f'Correy: {percentage[1]}% ({candidate_votecount[1]})\n')
    txt_file.write(f'Li: {percentage[2]}% ({candidate_votecount[2]})\n')
    txt_file.write(f'OTooley: {percentage[3]}% ({candidate_votecount[3]})\n')

    for i in range(len(percentage)):
        if Winner == percentage[i]:
            winner_name = candidate_namelist[i]

    txt_file.write("---------------------------- \n") 
    txt_file.write(f"Winner: {winner_name} \n")
    txt_file.write("---------------------------- \n") 
    
print(" Analysis")
print("------------------------------------------------------")
print(f'Khan: {percentage[0]}% ({candidate_votecount[0]})')
print(f'Correy: {percentage[1]}% ({candidate_votecount[1]})')
print(f'Li: {percentage[2]}% ({candidate_votecount[2]})')
print(f'OTooley: {percentage[3]}% ({candidate_votecount[3]})')
print("------------------------------------------------------")
print(f'The Winner is: {winner_name}')
