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

    #declare variables
    vote_list=[]


    #set header first**If you skip header, total votes is one off :(
    csv_header=next(csvreader)
   
    for row in csvreader:

        #find total votes
        vote_list.append(row[0])
        totalvotes=len(vote_list)
        







    print("Total Votes: "+str(totalvotes))
    print("------------------------\n")


