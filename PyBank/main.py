import os
import csv

# create file path
csvpath = os.path.join("..","Desktop", "budget_data.csv")

# open file wih reader and create object and pointer
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# skip header
    next(csvreader)

    # create empty lists
    monthList = []
    pLlist = []
    differenceList = []
    
    # append "column" values in the series into their designated lists
    for row in csvreader:  
        monthList.append(row[0])
        pLlist.append(int(row[1]))

    # iterate through pList, starting on the second value (index 1), ending at the length of the list
    # subtract the number in the list from the previous number 
    # append in differenceList
    for number in range(1,len(pLlist)):
        differenceList.append((int(pLlist[number])-int(pLlist[number-1])))


    print ("Financial Analysis:")
    

    length = len(monthList)
    print("Total months:" + str(length))

    netAmount = sum(pLlist)
    print("Net amount:" + str(netAmount) + " dollars")

    averageDifference = sum(differenceList) / len(differenceList) 
    print("Average change:" + str(averageDifference))

    greatestIncrease = max(differenceList)
    print("Greatest increase in profits:" + str(greatestIncrease))

    greatestDeacrease = min(differenceList)
    print("Greatest decrease in profits:" + str(greatestDeacrease))
    
