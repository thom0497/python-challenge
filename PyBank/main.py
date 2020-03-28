import os
import csv
profit = 0
months = 0
maximum = 0
max_month = ""
minimum = 100000000
min_month = ""
previous = 0
sum = 0
average = ""


csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:  
        months +=1
        profit += int(row[1])
        change = int(row[1]) - previous
        previous = int(row[1])
        if months > 1:
            sum = sum + change
        if int(row[1]) > maximum:
            maximum = int(row[1])
            max_month = str(row[0])
        if int(row[1]) < minimum:
            minimum = int(row[1])
            min_month = str(row[0])
        
average = sum/(months - 1)
print("Financial Analysis")
print("Total Months:" + str(months))
print("Total: $" +str(profit))
print("Average change: $" + "{:.2f}".format(average))
print("Greatest increase in profits: " + str(max_month) + " ($" + str(maximum) + ")")
print("Greatest decrease in profits: " + str(min_month) + " ($" + str(minimum) + ")")


        
        
        
        