#Import os module
import os

#Import module to read csv file
import csv

csvpath=os.path.join('budget_data.csv')

#read csv file
with open(csvpath) as csvfile:
    #csvreader specifies delimiter and variable 
    csvreader=csv.reader(csvfile,delimiter=",")

    #read the header first 
    csv_header=next(csvreader)

    #make empty lists to populate later
    date=[]
    profits=[]
    profitchange=[]

    #begin first loop
    for row in csvreader:
        #calculate total months by adding date column to list then calculate length
        date.append(row[0])
        daterange=len(date)

        #add profit values to list to sum later
        profits.append(int(row[1]))

    #calculate average change- loop row by row to calculate month-to-month changes
    for i in range(len(profits)-1):
        profitchange.append(profits[i+1]-profits[i])

        #average new list and round 2 decimal places
        average=round(sum(profitchange)/len(profitchange),2)

    #find max and min from new list
    increase=max(profitchange)
    decrease=min(profitchange)

    #index to find month of max/min
    max_month=profitchange.index(max(profitchange))+1
    min_month=profitchange.index(min(profitchange))+1
   
#print summary
print("Financial Analysis")
print("------------------------------------")
print(f"Total Months: {str(daterange)}")
print(f"Total: ${sum(profits)}")
print(f"Average Change: ${average}")
print(f"Greatest Increase in Profits: {date[max_month]} ${(str(increase))}")
print(f"Greatest Decrease in Profits: {date[min_month]} ${(str(decrease))}")
        
#write summary to txt file
txtpath=os.path.join('pybank.txt')
with open(txtpath,"w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------------------------\n")
    txtfile.write(f"Total Months: {str(daterange)}\n")
    txtfile.write(f"Total: ${sum(profits)}\n")
    txtfile.write(f"Average Change: ${average}\n")
    txtfile.write(f"Greatest Increase in Profits: {date[max_month]} ${(str(increase))}\n")
    txtfile.write(f"Greatest Decrease in Profits: {date[min_month]} ${(str(decrease))}\n")
