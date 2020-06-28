# Dependencies
import os
import csv
# Set path to file
input_file = os.path.join("Resources", "budget_data.csv")

# Lists to store data
month = []
revenue = []
change_revenue = []

# Open as csv file
with open(input_file, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip headers
    header = next(csvreader)
    # Append to lists
    for row in csvreader:
        month.append(row[0])
        revenue.append(int(row[1]))

        # Calculate total months
        total_month = len(month)

        # Calculate total revenue
        total_revenue = sum(revenue)

        # Calculate change in revenue
        for i in range(len(revenue)-1):
            change_revenue.append(int(revenue[i+1]) - int(revenue[i]))
            # Calculate average change in revenue
            average_change = round(sum(change_revenue) / len(change_revenue), 2)

            # Calculate the greatest
            max_change_revenue = max(change_revenue)
            min_change_revenue = min(change_revenue)
            max_change_month = month[change_revenue.index(max_change_revenue)+1]
            min_change_month = month[change_revenue.index(min_change_revenue)+1]

# Retrieve result
analysis = (
    f'Financial Analysis \n'
    f'------------------------------ \n'
    f'Total number of months: {total_month} \n'
    f'Total: ${total_revenue} \n'
    f'Average Change: ${average_change} \n'
    f'Greatest Increase in Profits: {max_change_month} (${max_change_revenue}) \n'
    f'Greatest Decrease in Profits: {min_change_month} (${min_change_revenue}) \n'
)

# Print analysis
print(analysis)

# Export the file
output_file = os.path.join("Analysis", "Financial_Analysis.txt")

# Write to text file
with open(output_file, "w") as txtfile:
    txtfile.write(analysis)
