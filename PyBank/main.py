#import modules
import os
import csv

#import csv
csvpath = os.path.join("c:/","MWB","DATA COURSE","python-challenge","PyBank","budget_data.csv")
with open(csvpath, newline='') as csvfile:
    budget = csv.reader(csvfile, delimiter=',')

    #skipping the header
    next(budget)

    #variables
    months = 0
    total = 0.00
    maxpl = 1000.00
    minpl = 0.00
    change = 0.00

    #calculations
    for row in budget:
        if row[0] != "":
            months = months +1

        total += round(float(row[1]), 2)

        change = round((total / float(months)),2)
        
        if float(row[1]) >= maxpl:
            maxpl = round(float(row[1]),2)

        if float(row[1]) <= minpl:
            minpl = round(float(row[1]),2)

    
    #output
    print("\n")
    print("Financial Analysis")
    print("---------------------------------")
    print(f"Total Months:  {months}")
    print(f"Total:  ${total}")
    print(f"Average Change:  ${change}")
    print(f"Greatest Increase in Profits:  ${maxpl}")
    print(f"Greatest Decrease in Profits:  ${minpl}")
    print("\n")

    #print to file
    with open("pybank.txt", "w") as file:
        file.write("Financial Analysis\n")
        file.write("---------------------------------\n")
        file.write(f"Total Months:  {months}\n")
        file.write(f"Total:  ${total}\n")
        file.write(f"Average Change:  ${change}\n")
        file.write(f"Greatest Increase in Profits:  ${maxpl}\n")
        file.write(f"Greatest Decrease in Profits:  ${minpl}\n")

    print("Analysis report saved as pybank.txt")