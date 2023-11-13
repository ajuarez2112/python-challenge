# Importing libraries
import os
import csv

# Creating path for the budget data csv file
budget_csv = os.path.join("Resources", "budget_data.csv")

# Create lists for storing data
date = []
profit_losses = []

# Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)  # Read the header row first

    for row in csv_reader:
        # Add date
        date.append(row[0])

        # Add profit_losses
        if float(row[1]):
            profit_losses.append(row[1])


# Use len function to calculate total months in list "date"
total_months = len(date)


total_profit = 0  # Add variable

# Use for loop to calculate the sum of "profit_losses" list
for num in profit_losses:
    total_profit = int(total_profit) + int(num)


# Add new list for Increase/Decrease in profits
changes = []

change = 0  # Add variable

# Add Increase/Decease in profits to "changes" list
for i in profit_losses:
    a = int(i) - int(change)
    changes.append(a)
    change = 0
    change = int(change) + int(i)

# Remove first item in "changes" list since it is not an actual change in profits/losses
changes.pop(0)

# Insert "0" at the beginning of "changes" list since there was no change in the first month
changes.insert(0, 0)

sum_changes = 0  # Add variable

# Use for loop to calculate the sum of "changes" list
for num in changes:
    sum_changes = int(sum_changes) + int(num)

# Add variable
total_changes = len(changes)

# Calculate the average of "changes" list by diving the sum of "changes" by "total_changes" - 1 so the "0" will not affect the average
avg_changes = round(int(sum_changes) / int(total_changes - 1), 2)


# Calculate greatest increase in profits by using max function
greatest_increase = max(changes)

# Find the index for "greatest_increase"
greatest_increase_index = changes.index(greatest_increase)

# Calculate greatest decrease in profits by using min function
greatest_decrease = min(changes)

# Find the index for "greatest_decrease"
greatest_decrease_index = changes.index(greatest_decrease)

# Create variables for the dates of the greatest increase and greatest decrease values
greatest_increase_date = date[greatest_increase_index]
greatest_decrease_date = date[greatest_decrease_index]


# Set output path
output_path = os.path.join("analysis", "financial_analysis.txt")

# Print analysis into terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_profit))
print("Average Change: $" + str(avg_changes))
print(
    "Greatest Increase in Profits: "
    + str(greatest_increase_date)
    + " ($"
    + str(greatest_increase)
    + ")"
)
print(
    "Greatest Decrease in Profits: "
    + str(greatest_decrease_date)
    + " ($"
    + str(greatest_decrease)
    + ")"
)


# Open txt file using "write mode" and print the analysis into it.
with open(output_path, "w") as output:
    output.write("Financial Analysis" + "\n")
    output.write("----------------------------" + "\n")
    output.write("Total Months: " + str(total_months) + "\n")
    output.write("Total: $" + str(total_profit) + "\n")
    output.write("Average Change: $" + str(avg_changes) + "\n")
    output.write(
        "Greatest Increase in Profits: "
        + str(greatest_increase_date)
        + " ($"
        + str(greatest_increase)
        + ")"
        + "\n"
    )
    output.write(
        "Greatest Decrease in Profits: "
        + str(greatest_decrease_date)
        + " ($"
        + str(greatest_decrease)
        + ")"
    )
