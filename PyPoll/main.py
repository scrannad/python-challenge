# Import modules
import os
import csv

csvpath=os.path.join('election_data.csv')

#set dictionary
poll={}

#declare variables
total_votes=0
candidate_votes={}

#read csv file
with open(csvpath,'r') as csvfile:

    #set up csv reader with delimiter
    csvreader=csv.reader(csvfile,delimiter=',')

    #set header first
    csv_header=next(csvreader)

    #begin loop through data
    for row in csvreader:
        
        #gather total votes
        total_votes+=1

        #gather candidates in list
        if row[2] not in candidate_votes:
            candidate_votes[row[2]]=1
        else:
            candidate_votes[row[2]]+=1

#print results
print("Election Results")
print("------------------------")
print(f"Total Votes: {str(total_votes)}")
print("------------------------")

#find candidate name, percentage of votes, and vote count in dictionary, print result
for candidate,votes in candidate_votes.items():
        print(candidate+": "+"{:.3%}".format(votes/total_votes)+"  ("+str(votes)+")")
        txt_variable=(candidate+": "+"{:.3%}".format(votes/total_votes)+"  ("+str(votes)+")")

#find winner by popular vote
winner=max(candidate_votes,key=candidate_votes.get)
print("------------------------")
print(f"Winner: {winner}")
print("------------------------")


#write summary to txt file
txtpath=os.path.join('pypoll.txt')
txtfile=open(txtpath,'w')
txtfile.write("Election Results\n")
txtfile.write("------------------------\n")
txtfile.write(f"Total Votes: {str(total_votes)}\n")
txtfile.write("------------------------\n")

for candidate,votes in candidate_votes.items():
        txtfile.write(candidate+": "+"{:.3%}".format(votes/total_votes)+"  ("+str(votes)+")\n")
        
txtfile.write("------------------------\n")
txtfile.write(f"Winner: {winner}\n")
txtfile.write("------------------------")

txtfile.close()
