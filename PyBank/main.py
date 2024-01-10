#Your task is to create a Python script that analyzes the records to calculate each of the following values:

# The total number of months included in the dataset
 
#The net total amount of "Profit/Losses" over the entire period

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period


#First, set up the CSV Reader and have the script read the values in the document.

import os

import csv

csvpath = os.path.join('C:\\', 'Users', 'danrk', 'Desktop', 'Data Bootcamp', 'Module 3', 
                       'Module 3 Challenge', 'python-challenge', 'PyBank', 
                       'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #The file has a header, so we need the read the header row first.

    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')

    #Create a counter to sum the months.
    total_months = 0
    #Create a counter to sum the net Profit/Loss.
    net_total = 0

    for row in csvreader:
        total_months = total_months + 1
        
        net_total = net_total + int(row[1])

    

    #Print the Analysis in the format requested!
        
    print("Financial Analysis")

    print("----------------------------")    
    
    print(f'Total Months: {total_months}')

    print(f'total ${net_total}')
