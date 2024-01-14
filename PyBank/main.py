# Your task is to create a Python script that analyzes the records to calculate each of the following values:

# The total number of months included in the dataset
 
# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period


# First, set up the CSV Reader and have the script read the values in the document.

import os

import csv

csvpath = os.path.join('C:\\', 'Users', 'danrk', 'Desktop', 'Data Bootcamp', 'Module 3', 
                       'Module 3 Challenge', 'python-challenge', 'PyBank', 
                       'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # The file has a header, so we need the read the header row first.

    csv_header = next(csvreader)

    # Create a counter to sum the months.
    total_months = 0
    # Create a counter to sum the net Profit/Loss.
    net_total = 0
    # Create a variable to hold the change in Profit/Loss between each entry.
    pl_change = 0
    # Create an empty list to record each value of change during the loop.
    pl_list = []
    # These empty lists will be needed to capture the greatest increase and greatest decrease durinmg
    # the loop.
    greatest_increase = []

    greatest_decrease = []

    # Loop through the data to capture needed values:
    for row in csvreader:
    # This sums the total number of months (entries):
        total_months = total_months + 1
    # This keeps a running tally of the net total Profit/Loss:
        net_total = net_total + int(row[1])
    # This calculates the difference between the value of the current row and the previous row...
        pl_change = (int(row[1]) - int(pl_change))
    #...Which we can then add to our list of Profit/Loss changes!
        pl_list.append(pl_change)
    # Now we check to see whether this row contains the greatest increase/decrease in the data.
    # This is important, because we need to capture the date associated with the value.
        if max(pl_list) == pl_change:
            # If it ends up being the greatest value for either increase or decrease, we need to
            # first clear the list of any dates that were added earlier in the loop. Then we can
            # replace it with the new date. As the program checks the loop, once the
            # greatest values are found, they will not be replaced by lower values, meaning the
            # dates will also stay the same.
            greatest_increase.clear()
            
            greatest_increase.append(row[0])

        elif min(pl_list) == pl_change:

            greatest_decrease.clear()

            greatest_decrease.append(row[0])

    # After calculating the difference, reset the pl_change variable at the end of each loop to be
    # the correct value so the loop calculates an accurate difference from the next row.
        pl_change = (row[1])


    # After the loop completes, the first entry added to the list is technically inaccurate (it adds
    # a value that wasn't subtracted from anything), so it needs to be removed from the list via the pop function.
    pl_list.pop(0)


    # Create a variable that holds the average of the Profit/Loss values from the list.
    pl_total = sum(pl_list)/len(pl_list)

    # Print the Analysis in the format requested!
        
    print("Financial Analysis")

    print("----------------------------")    
    
    print(f'Total Months: {total_months}')

    print(f'Total: ${net_total}')

    
    # When printing the average Profit/Loss, the expected format is rounded to two decimal places, 
    # which requires the round function.
    print(f'Average Change: ${round(pl_total,2)}')

    # The max/min variables hold the greates increase and decrease numeric values from the banking
    # information. I re-define the first (and only) values of my greatest_increase/decrease lists to
    # give myself a way to reference the associated dates.
    max = max(pl_list)

    min = min(pl_list)

    increase = greatest_increase[0]

    decrease = greatest_decrease[0]

    # These statements use the above variables to properly print the requested values, and the days
    # associated with them.
    
    print(f'Greatest Increase in Profits: {increase} (${max})')

    print(f'Greatest Decrease in Profits: {decrease} (${min})')

    file = 'analysis/analysis.txt'

    # This is a write-only operation, so I use w on the new file I created.
    # I also will ID this new file as "banking," which will let the program
    # know I want to write each line to that file.
   
    banking = open(file, "w")

    # The remaining lines of code are identical to the lines I printed
    # in the program results, with two main differences: 1. Instead of
    # printing, it uses the write command in relation to the banking file.
    # 2. To assist with making the resulting file legible, I added \n to
    # each string, which tells the program to write a new line during each 
    # write command.
    
    banking.write("Financial Analysis\n")

    banking.write("----------------------------\n")    
    
    banking.write(f'Total Months: {total_months}\n')

    banking.write(f'Total: ${net_total}\n')

    banking.write(f'Average Change: ${round(pl_total,2)}\n')

    banking.write(f'Greatest Increase in Profits: {increase} (${max})\n')

    banking.write(f'Greatest Decrease in Profits: {decrease} (${min})\n')      