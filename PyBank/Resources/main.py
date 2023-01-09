#Import os module
import os

#Import module to read csv file
import csv

csvpath=os.path.join('budget_data.csv')

#print header


#read csv file
with open(csvpath) as csvfile:
    #csvreader specifies delimiter and variable 
    csvreader=csv.reader(csvfile,delimiter=",")

    #read the header first 
    csv_header=next(csvreader)

    #declare variables
    total=0
    date=[]
    profits=[]
    profitchange=[]

    #begin first loop
    for row in csvreader:
        # total months
        date.append(row[0])
        daterange=len(date)

        #total value
        profits.append(int(row[1]))



 
   
        
        
        
    

#find average

#print everything
print("Financial Analysis")
print("------------------------------------")
print("Total Months: "+str(daterange))
print(f"Total: ${sum(profits)}")
# print(f"Average Change: $ ")
# print(f"Greatest Increase in Profits: ")
# print(f"Greatest Decrease in Profits: ")
        