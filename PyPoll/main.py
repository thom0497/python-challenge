import os
import csv
VoterID = 0
County = 0 
Candidate = []
Khan_Vote = 0
Correy_Vote = 0
Li_Vote = 0
O_Tooley_Vote = 0
Pct = []
Winner_Name = 0



csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:  
        VoterID +=1
        Candidate.append(row[2])
        if row[2]=="O'Tooley":
            O_Tooley_Vote +=1
        elif row[2]=="Khan":
            Khan_Vote +=1
        elif row[2]=="Li":
            Li_Vote +=1
        else:
            Correy_Vote +=1

Khan_Pct = round(Khan_Vote/VoterID*100,2)
Li_Pct = round(Li_Vote/VoterID*100,2)  
Correy_Pct = round(Correy_Vote/VoterID*100,2)  
O_Tooley_Pct = round(O_Tooley_Vote/VoterID*100,2)
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(VoterID))
print("-------------------------")
print("Khan: " + str(Khan_Pct) + "% " + "(" + str(Khan_Vote) + ")")
print("Li: " + str(Li_Pct) + "% " + "(" + str(Li_Vote) + ")")
print("Correy: " + str(Correy_Pct) + "% " + "(" + str(Correy_Vote) + ")")
print("O'Tooley: " + str(O_Tooley_Pct) + "% " + "(" + str(O_Tooley_Vote) + ")")
print("-------------------------")
Winner = max(Khan_Vote, Li_Vote, Correy_Vote, O_Tooley_Vote)
if Winner == Khan_Vote:
    print("Winner: Khan")
elif Winner == Li_Vote:
    print("Winner: Li")
elif Winner == Li_votes:
    print("Winner: Correy")
else:
    print("Winner: O'Tooley")