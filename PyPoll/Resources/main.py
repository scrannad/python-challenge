# Import modules
import os
import csv

csvpath=os.path.join('election_data.csv')

#Print Header
print("Election Results")
print("------------------------\n")

#read csv file
with open(csvpath) as csvfile:

    #set up csv reader with delimiter
    csvreader=csv.reader(csvfile,delimiter=',')

    #set header first
    csv_header=next(csvreader)

    #declare variables
    vote_list=[]

    #begin loop through data
    for row in csvreader:

        #find total votes
        vote_list.append(row[0])
        totalvotes=len(vote_list)








    print("Total Votes: "+str(totalvotes))
    print("------------------------\n")


