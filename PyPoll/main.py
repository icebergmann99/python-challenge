#import modules
import os
import csv

#import csv
csvpath = os.path.join("c:/","MWB","DATA COURSE","python-challenge","PyPoll","election_data.csv")
with open(csvpath, newline='') as csvfile:
    election = csv.reader(csvfile, delimiter=',')

    #skipping the header
    next(election)

     #variables
    votes = 0
    candidates = []
    #votefor = [0,0,0,0,0,0,0,0,0,0] #limits num of candidates to 10
    votefor = []
    #votepercent = [0,0,0,0,0,0,0,0,0,0]
    votepercent = []

    #calculations
    for row in election:
        if row[0] != "":
            votes = votes +1

        if row[2] not in candidates:
            candidates.append(row[2])
            c = len(candidates)
            votefor = [0] * c
            votepercent = [0] * c

        for i in range(0,c):
            if row[2] == candidates[i]:
                votefor[i] = votefor[i] + 1
    
    for j in range(0,c):
        votepercent[j] = round(((votefor[j]/votes)*100))

    w = votepercent.index(max(votepercent))
    winner = candidates[w]
                            
   
    #output
    print("\n")
    print("Election Results")
    print("---------------------------")
    print(f"Total Votes:  {votes}")
    print("---------------------------")
    for k in range (0,c):
        print(candidates[k] + ": " + str(votepercent[k]) + "% (" + str(votefor[k]) + ")")
    #print(candidates)
    #print(votefor)
    #print(votepercent)
    print("---------------------------")
    print(f"Winner:  {winner}")
    print("---------------------------")
    print("\n")
    
    #print to file
    with open("pypoll.txt", "w") as file:
        file.write("Election Results\n")
        file.write("---------------------------\n")
        file.write(f"Total Votes:  {votes}\n")
        file.write("---------------------------\n")
        for k in range (0,c):
            file.write(candidates[k] + ": " + str(votepercent[k]) + "% (" + str(votefor[k]) + ")\n")
        file.write("---------------------------\n")
        file.write(f"Winner:  {winner}\n")
        file.write("---------------------------\n")

    print("Results saved in pypoll.txt")