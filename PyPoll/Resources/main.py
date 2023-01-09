# Import modules
import os
import csv

csvpath=os.path.join('election_data.csv')

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
  






#print summary
print("Election Results")
print("------------------------\n")
print(f"Total Votes: {str(totalvotes)}")
print("------------------------\n")


#write summary to txt file
txtpath=os.path.join('pypoll.txt')
with open(txtpath,"w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("------------------------------------\n")
    txtfile.write(f"Total Votes: {str(totalvotes)}\n")
    txtfile.write("------------------------\n")
    
