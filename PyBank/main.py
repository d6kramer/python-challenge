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

    date_list = []

    full_list = []

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
    # After calculating the difference, reset the pl_change variable at the end of each loop to be
    # the correct value so the loop calculates an accurate difference from the next row.
        pl_change = (row[1])

        date_list.append(row[0])

        full_list.append(row)


    # After the loop completes, the first entry added to the list is technically inaccurate (it adds
    # a value that wasn't subtracted from anything), so it needs to be removed from the list via the pop function.
    pl_list.pop(0)

    # Create a variable that holds the average of the Profit/Loss values from the list.
    pl_total = sum(pl_list)/len(pl_list)

    #Print the Analysis in the format requested!
        
    print("Financial Analysis")

    print("----------------------------")    
    
    print(f'Total Months: {total_months}')

    print(f'total ${net_total}')

    
    # When printing the average Profit/Loss, the expected format is rounded to two decimal places, 
    # which requires the round function.
    print(round(pl_total,2))


    max = int(max(pl_list))

    min = int(min(pl_list))

    print(max)

    print(min)

    print(date_list)

    for row in full_list:

        if row == (str(date_list), int(max)):
    
            print("Hello")

            
            #print(f'{1- (row[0])} (${row[1]})')
        
        #elif 

        #print(f'Greatest Decrease in Profits: {row[0]} (${row[1]})')
            