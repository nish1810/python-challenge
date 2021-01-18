import os
import csv
import sys
# Path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')

# Read in the CSV file
with open(election_csv, 'r') as csvfile:
    
    # Split the data on commas
    election = csv.reader(csvfile, delimiter=',')
    header = next(election)
    total_votes = 0
    individual_vote = 0
    unique_vote = []
    candidate = []
    candidates = []
    num_votes = []
    vote_per =[]
    for row in election:
        total_votes += 1
        candidate.append(row[2])
    for x in set(candidate):
        unique_vote.append(x)
        y = candidate.count(x)
        num_votes.append(y)
        z = (y/total_votes)*100     # z is the percent of total votes per candidate
        vote_per.append(z)
        
    
    print(f'Election Results\n-------------------------\nTotal Votes:{total_votes}\n-------------------------\n')
    for a in range(len(num_votes)):
        print(f'{unique_vote[a]} : {vote_per[a]}% ({num_votes[a]})')
    print("-------------------------")
    print(f'Winner: {unique_vote[num_votes.index(max(num_votes))]}')
    print("-------------------------")

    with open('elecresult_data.txt', 'w') as f:
        print(f'Election Results\n-------------------------\nTotal Votes:{total_votes}\n-------------------------\n',file =f)
        for a in range(len(num_votes)):
            print(f'{unique_vote[a]} : {vote_per[a]}% ({num_votes[a]})', file =f)
        print("-------------------------",file=f)
        print(f'Winner: {unique_vote[num_votes.index(max(num_votes))]}',file=f)
        print("-------------------------",file=f)