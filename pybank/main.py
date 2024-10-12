# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
csvpath = os.path.join("resources", "budget_data.csv")  # Input file path
print(csvpath)


# Add more variables to track other necessary financial data
total_amount = []
average_change = []
total_months = []

# Open and read the csv
with open(csvpath,encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvpath)

    # Skip the header row
    csv_header = next(csvreader)

    for row in csvreader:
        total_months.append(row[0])
        total_amount.append(int(row[1]))

for i in range(len(total_amount)-1):
    average_change.append(total_amount[i+1]-total_amount[i])

        # Calculate the greatest increase in profits (month and amount)
        # Calculate the greatest decrease in losses (month and amount)
greatest_increase = max(average_change)
greatest_decrease = min(average_change)
greatest_increase_month = average_change.index(max(average_change))+1
greatest_decrease_month = average_change.index(min(average_change))+1

# Generate the output summary
analysis = os.path.join("analysis", "budget_analysis.txt")  # Output file path

print("Financial Analysis")
print("------------------")
print(f"Total Months : {len(total_months)}" )
print(f"Total: ${sum(total_amount)}")
print(f"Average Change: ${round(sum(average_change)/len(average_change),2)}")
print(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase))})")
print(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease))})")

# Write the results to a text file
with open(analysis, "w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("------------------")
    file.write("\n")
    file.write(f"Total Months : {len(total_months)}" )
    file.write("\n")
    file.write(f"Total: ${sum(total_amount)}")
    file.write("\n")
    file.write(f"Average Change: ${round(sum(average_change)/len(average_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[greatest_increase_month]} (${(str(greatest_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[greatest_decrease_month]} (${(str(greatest_decrease))})")