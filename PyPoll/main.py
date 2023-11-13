# Importing libraries
import os
import csv

# Creating path for the election data csv file
election_csv = os.path.join("Resources", "election_data.csv")

# Create lists for storing data
candidate = []

# Open and read the csv
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)  # Read the header row first

    for row in csv_reader:
        # Add candidate
        candidate.append(row[2])

# Use len function to calculate the total number of votes
total_votes = len(candidate)


# Create a dictionary to store the votes for each candidate
candidate_votes = {}

# Create for loop to find the number of votes for each candidate and store in "candidate_votes" dictionary
for i in candidate:
    if i in candidate_votes:
        candidate_votes[i] = candidate_votes[i] + 1
    else:
        candidate_votes[i] = 1

# Create new lists to store cleaned data from "candidate_votes" dictionary
all_candidates = []
votes = []
averages = []


# Create for loop to find all candidates, votes for each candidate and average of each candidates votes
# And append the data into the new lists that were created
for key, value in candidate_votes.items():
    avg = round(((value / total_votes) * 100), 3)
    all_candidates.append(key)
    votes.append(value)
    averages.append(avg)

# Zip together new lists that were created
candidate_results = list(zip(all_candidates, averages, votes))

# Create variable for winning number of votes
winning_count = 0
# Create variable for the winning candidate
winning_candidate = ""

# Create for loop to find the winning number of votes and the winning candidate
for key, value in candidate_votes.items():
    if value > winning_count:
        winning_count = value
        winning_candidate = key


# Add variables to print to terminal and txt file easier
election_results_1 = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)
election_results_2 = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"-------------------------"
)

# Print analysis into the terminal
print(election_results_1)

# Create a for loop to print all information from the "candidate_results" list
for a, b, c in candidate_results:
    print(f"{a}: {b}% ({c})\n")

print(election_results_2)

# Set output path
output_path = os.path.join("analysis", "election_results.txt")

# Open txt file using "write mode" and print the analysis into it.
with open(output_path, "w") as output:
    output.write(election_results_1)
    # Create a for loop to print all information from the "candidate_results" list
    for a, b, c in candidate_results:
        output.write(f"{a}: {b}% ({c})\n")
    output.write(election_results_2)
