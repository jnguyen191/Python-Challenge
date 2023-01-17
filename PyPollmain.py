import os

import csv

# path to csv file
PyPoll_path = os.path.join("election_data.csv")

# setting variables
voters = []
candidates = []
candidate_options = []
candidate_votes = []
winner_candidate = ""
candidate_index = []
vote_percentage = []

# setting initial values
totalcast_count = 0
winning_count = 0
winning_percentage = 0

# open file with file path
with open(PyPoll_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    for row in csvreader:
        voter_id = row[0]
        voters.append(voter_id)
        
        candidates = row[2]

    # The total number of votes cast
        
        totalcast_count = len(voters)

       # A complete list of candidates who received votes
        # pull each unique candidate name to candidate_options list. Use If - only pull name if it does not match any name in the candidate_options list. 
        if row[2] not in candidate_options:
            candidate_options.append(row[2])
            candidate_index = candidate_options.index(row[2])
            candidate_votes.append(1)

        else:
            candidate_index = candidate_options.index(row[2])
            candidate_votes.append(1)
            candidate_votes[candidate_index] +=1

       
    # The total number of votes each candidate won
    for candidate in candidate_votes:
        votes = candidate_votes[candidate_index]
        vote_percentage = float(votes) / float(totalcast_count) *100
        candidate_results = f"{candidates}: {vote_percentage:.3f}% ({votes:,})\n"
    

    # The winner of the election based on popular vote
    if (votes > winning_count):
            winning_count = votes
            winner_candidate = candidates
            winning_percentage = vote_percentage

    

    

print("Election Results")
print("---------------------")
print(f"Total Votes: {totalcast_count}")
print("---------------------")
print(candidate_results)
print("---------------------")
print(f"Winner: {winner_candidate}")


PyPoll_analysis = os.path.join("PyPoll_analysis.txt")
with open(PyPoll_analysis, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("---------------------\n")
    outfile.write(f"Total Votes: {totalcast_count}\n")
    outfile.write(f"---------------------\n")
    outfile.write(f"{candidate_results}\n")
    outfile.write(f"---------------------\n")
    outfile.write(f"winner:{winner_candidate}\n")