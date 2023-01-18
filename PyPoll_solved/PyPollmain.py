import os

import csv

# path to csv file
PyPoll_path = os.path.join("election_data.csv")

# setting variables
voters = []
candidates = {}
num_votes = []
winner_candidate = ""
vote_percentage = []

# setting initial values
totalcast_count = 0
winning_percentage = 0


print("Election Results")
print("---------------------")

# open file with file path
with open(PyPoll_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    for row in csvreader:
        voter_id = row[0]
        voters.append(voter_id)

    # The total number of votes cast
        totalcast_count = len(voters)

       # A complete list of candidates who received votes
        #dictionary candidate Row 2 into candidates
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] +=1
        else:
            candidates[candidate] = 1
        
    print(f"Total Votes: {totalcast_count}")
    print("---------------------")

PyPoll_analysis = os.path.join("PyPoll_analysis.txt")
with open(PyPoll_analysis, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("---------------------\n")
    outfile.write(f"Total Votes: {totalcast_count}\n")
    outfile.write(f"---------------------\n")

    for key, value in candidates.items():
        vote_percentage = round((value/totalcast_count)*100, 2)
        candidate_counts = key,value

        
        print(f"{candidate_counts} {vote_percentage:.3f}%")
        outfile.write(f"{candidate_counts} {vote_percentage:.3f}%\n")
        

        if vote_percentage > winning_percentage:
            winning_percentage = vote_percentage
            winner_candidate = [key]


    print("---------------------")
    print(f"Winner: {winner_candidate}")
    outfile.write(f"---------------------\n")
    outfile.write(f"winner:{winner_candidate}\n")
