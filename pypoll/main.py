# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
csvpath = os.path.join("resources", "election_data.csv")  # Input file path
print(csvpath)

# Initialize variables to track the election data
total_votes =[]
charles_votes = 0
diana_votes = 0
raymon_votes = 0

# Open the CSV file and process it
with open(csvpath,encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    # Skip the header row
    csv_header = next(csvreader)
    
    # Loop through each row of the dataset and process it
    for row in csvreader:
        total_votes.append(row[0])

        if row[2] == "Charles Casper Stockham":
            charles_votes +=1
        elif row[2] == "Diana DeGette":
            diana_votes +=1
        elif row[2] == "Raymon Anthony Doane":
            raymon_votes +=1

# Define lists and dictionaries to track candidate names and vote counts
canidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
canidate_votes = [charles_votes, diana_votes, raymon_votes]

# Winning Candidate and Winning Count Tracker
votes_dict = dict(zip(canidates, canidate_votes))
winner = max(votes_dict, key = votes_dict.get)

total_vote_count = len(total_votes)
charles_percent = (charles_votes/total_vote_count)*100
diana_percent = (diana_votes/total_vote_count)*100
raymon_percent = (raymon_votes/total_vote_count)*100

print("Election Results")
print("---------------")
print(f"Total Votes : {len(total_votes)}")
print("---------------")
print(f"Charles Casper Stockham: {charles_percent:.3f}% ({charles_votes})")
print(f"Diana Degette: {diana_percent:.3f}% ({diana_votes})")
print(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon_votes})")
print("---------------")
print(f"Winner: {winner}")
print("---------------")

analysis = os.path.join("analysis", "election_analysis.txt")
# Open a text file to save the output
with open(analysis, "w") as file:

   file.write("Election Results")
   file.write("\n")
   file.write("--------------------")
   file.write("\n")
   file.write(f"Total Votes : {len(total_votes)}")
   file.write("\n")
   file.write("--------------------")
   file.write("\n")
   file.write(f"Charles Casper Stockham : {charles_percent:.3f}% ({charles_votes})")
   file.write("\n")
   file.write(f"Diana DeGette : {diana_percent:.3f}% ({diana_votes})")
   file.write("\n")
   file.write(f"Raymon Anthony Doane : {raymon_percent:.3f}% ({raymon_votes})")
   file.write("\n")
   file.write("--------------------")
   file.write("\n")
   file.write(f"Winner: {winner}")
   file.write("\n")
   file.write("--------------------")
