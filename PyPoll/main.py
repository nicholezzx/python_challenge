# Dependencies
import os
import csv
# Set path to file
input_file = os.path.join("Resources", "election_data.csv")

# Lists to store data
vote_count = []
candidate = []
election = []
candidate_percentage = []
total_votes = 0

# Open as csv file
with open(input_file, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip headers
    header = next(csvreader)
    
    # Loop
    for row in csvreader:
        # Count total votes
        total_votes = total_votes + 1
        
        # If another candidate
        if row[2] not in election:
            election.append(row[2])
            candidate = election.index(row[2])
            vote_count.append(1)
        
        # If same candidate
        else:
            candidate = election.index(row[2])
            vote_count[candidate] = vote_count[candidate] + 1

# Calculate percentage
for votes in vote_count:
    percentage = "{:.2%}".format(votes / total_votes)
    candidate_percentage.append(percentage)

# Find winner
candidate = vote_count.index(max(vote_count))
winner = election[candidate]

# Result summaries
election_summary = (
    f'Election Results \n'
    f'------------------------ \n'
    f'Total Votes: {total_votes} \n'
    f'------------------------ \n'
)
winner_summary = (    
    f'------------------------ \n'
    f'Winner: {winner} \n'
    f'------------------------ \n'
)

# Print election
print(election_summary)

# Print candidate summary
for candidate in range(len(election)):
    print(f'{election[candidate]}: {candidate_percentage[candidate]} ({vote_count[candidate]}) \n')

# Print winner
print(winner_summary)

# Export the file
output_file = os.path.join("Analysis", "Election_Result.txt")

# Write to text file
with open(output_file, "w") as txtfile:
    txtfile.write(election_summary)
    for candidate in range(len(election)):
        txtfile.write(f"{election[candidate]}: {candidate_percentage[candidate]} ({vote_count[candidate]}) \n")
    txtfile.write(winner_summary)
