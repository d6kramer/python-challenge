#Your task is to create a Python script that analyzes the votes and calculates each of the following values:

    #The total number of votes cast

    #A complete list of candidates who received votes

    #The percentage of votes each candidate won

    #The total number of votes each candidate won

    #The winner of the election based on popular vote

# First, set up CSV Reader and have the script read the document.

import os

import csv

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # This file has a header, so I need to move past the first row when reading.

    csv_header = next(csvreader)

    # Create a counter that will tally up all of the votes during the loop.
    total_votes = 0

    # I can only read through the CSV file once, so now I will create shorter variables for
    # each candidate, along with a list that will hold each vote per candidate when the loop runs.
    ccs = "Charles Casper Stockham"

    ccs_vote = []

    dd = "Diana DeGette"

    dd_vote = []

    rad = "Raymon Anthony Doane"

    rad_vote = []

    # Now run the loop:
    for row in csvreader:

        # This is the counter tallying each vote.
        total_votes = total_votes + 1

        # This set of conditional statements functions as counters for each of the
        # candidates. Instead of an integer like total_vote, I am keeping the 
        # values in lists.
        if row[2] == dd:

            dd_vote.append(row[2])

        elif row[2] == ccs:

            ccs_vote.append(row[2])

        else:

            rad_vote.append(row[2])


    # These variables yield each candidate's performance in relation to the total vote.
    ccs_percent = (len(ccs_vote) / total_votes *100)

    dd_percent = (len(dd_vote) / total_votes *100)

    rad_percent = (len(rad_vote) / total_votes *100) 


    print("Election Results")

    print("-------------------------")

    print(f'Total Votes: {total_votes}')

    print("-------------------------")

    # The shorter variables for the candidates made earlier allows me to make
    # shorter f strings. The round function allows me to take the percentage result
    # to the 3rd decimal place. Calculating the length of each list yields the number 
    # of votes each candidate recieved.

    print(f'{ccs}: {round(ccs_percent, 3)}% ({len(ccs_vote)})')

    print(f'{dd}: {round(dd_percent, 3)}% ({len(dd_vote)})')

    print(f'{rad}: {round(rad_percent, 3)}% ({len(rad_vote)})')

    # Because the program is inteded to yield the winner (it isn't pre-programmed),
    # I need a set of conditional statements for the program to evaluate which candidate
    # recieved the most votes. These statements will cause the correct winning candidate
    # to print.
    
    print("-------------------------")

    if len(ccs_vote) > (len(dd_vote) + len(rad_vote)):

        print(f'Winner: {ccs}')

    elif len(dd_vote) > (len(ccs_vote) + len(rad_vote)):

        print(f'Winner: {dd}')

    elif len(rad_vote) > (len(dd_vote) + len(ccs_vote)):

        print(f'Winner: {rad}')

    print("-------------------------")

    # Lastly, I need to print the results to a new .txt file in
    # the analysis folder. I define the file first with the correct
    # filepath.
    
    file = 'analysis/analysis.txt'

    # This is a write-only operation, so I use w on the new file I created.
    # I also will ID this new file as "election," which will let the program
    # know I want to write each line to that file.
   
    election = open(file, "w")

    # The remaining lines of code are identical to the lines I printed
    # in the program results, with two main differences: 1. Instead of
    # printing, it uses the write command in relation to the election file.
    # 2. To assist with making the resulting file legible, I added \n to
    # each string, which tells the program to write a new line during each 
    # write command.

    election.write("Election Results\n")

    election.write("-------------------------\n")

    election.write(f'Total Votes: {total_votes}\n')

    election.write("-------------------------\n")

    election.write(f'{ccs}: {round(ccs_percent, 3)}% ({len(ccs_vote)})\n')

    election.write(f'{dd}: {round(dd_percent, 3)}% ({len(dd_vote)})\n')

    election.write(f'{rad}: {round(rad_percent, 3)}% ({len(rad_vote)})\n')
    
    election.write("-------------------------\n")

    if len(ccs_vote) > (len(dd_vote) + len(rad_vote)):

        election.write(f'Winner: {ccs}\n')

    elif len(dd_vote) > (len(ccs_vote) + len(rad_vote)):

        election.write(f'Winner: {dd}\n')

    elif len(rad_vote) > (len(dd_vote) + len(ccs_vote)):

        election.write(f'Winner: {rad}\n')

    election.write("-------------------------\n")