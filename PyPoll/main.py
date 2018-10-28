import os
import csv

# create file path
csvpath = os.path.join("..","Desktop", "election_data.csv")

# open file wih reader and create object and pointer
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# skip header
    header = next(csvreader)

    candidateDict = {}
    candidateDict2 = {}
    totalVotes = 0

    for row in csvreader:
        totalVotes += 1
        if row[2] in candidateDict:
            candidateDict[row[2]]+= 1 # figure out else first
        else:
            candidateDict[row[2]] = 1
    print("Total votes of all candidates: "+ str(totalVotes))
    print("Total votes for each individual candidate:")
    print(candidateDict)
    
    # percentageVotes = /totalVotes
    
    for i in candidateDict:
        candidateDict[i] = float((candidateDict[i]/totalVotes)*100)
        # candidateDict.append(candidateDict[1])
        
    print("Percentage of votes for each candidate:")
    print(candidateDict)

    large = 0
    for value in candidateDict:
        if candidateDict[value] > large:
            large = candidateDict[value]
    print("Winner is Khan at " + str(large))
    











    # appendix trials:


        # # candidateList = (row for row[2] in csvreader)
        # # # if row[2] = row[2]
        # candidateList.append(row[2])

       
    # print(candidateList)

    # print(len(candidateList))

        # if row[2] in candidateDict:
        #     candidateDict[row[2]].append(row[1])
          
    # for candidate in range(1,len(candidateList)):
    #     count = candidateList.count(candidate)

    # print(count)

    
    # print(candidateList)

    # for candidate in candidateList:
    #    if candidate in candidateDict:
    #        candidateDict[candidate] += 1
           #  totalVotes = candidateList.count(candidateList[candidate])
    

    # for candidate in candidateList:
    #     if candidate in candidateDict:
    #         candidateDict[candidate] += 1
    #     else:
    #         candidateDict[candidate] = 1

    #     print(candidateDict)
    
    # for candidate in range(len(candidateList)): 
    #     candidateDict[candidateList[candidate]] = candidateList.count(candidateList[candidate])
    # print(candidateDict)
