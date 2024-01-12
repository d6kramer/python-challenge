#Your task is to create a Python script that analyzes the votes and calculates each of the following values:

    #The total number of votes cast

    #A complete list of candidates who received votes

    #The percentage of votes each candidate won

    #The total number of votes each candidate won

    #The winner of the election based on popular vote

#First, set up CSV Reader and have the script read the document.

import os

import csv

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #This file has a header, so we need to move past the first row when reading.

    csv_header = next(csvreader)

    #csv_rows = list(csvreader)

    total_votes = 0

    ccs = "Charles Casper Stockham"

    ccs_vote = []

    dd = "Diana DeGette"

    dd_vote = []

    rad = "Raymon Anthony Doane"

    rad_vote = []

    for row in csvreader:

        total_votes = total_votes + 1

        if row[2] == dd:

            dd_vote.append(row[2])

        elif row[2] == ccs:

            ccs_vote.append(row[2])

        else:

            rad_vote.append(row[2])



    ccs_percent = (len(ccs_vote) / total_votes *100)

    dd_percent = (len(dd_vote) / total_votes *100)

    rad_percent = (len(rad_vote) / total_votes *100) 


    print("Election Results")

    print("-------------------------")

    print(f'Total Votes: {total_votes}')

    print("-------------------------")

    print(f'{ccs}: {round(ccs_percent, 3)}% ({len(ccs_vote)})')

    print(f'{dd}: {round(dd_percent, 3)}% ({len(dd_vote)})')

    print(f'{rad}: {round(rad_percent, 3)}% ({len(rad_vote)})')

    print("-------------------------")

    if len(ccs_vote) > (len(dd_vote) + len(rad_vote)):

        print(f'Winner: {ccs}')

    elif len(dd_vote) > (len(ccs_vote) + len(rad_vote)):

        print(f'Winner: {dd}')

    elif len(rad_vote) > (len(dd_vote) + len(ccs_vote)):

        print(f'Winner: {rad}')

    print("-------------------------")