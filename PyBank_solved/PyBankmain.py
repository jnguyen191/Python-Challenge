import os

import csv

#Path to PyBank csv file
PyBank_path = os.path.join("budget_data.csv")

#list to store the names of columns
months = []
profit_Loss = []
monthly_changes = []

#setting initial value
total_months = 0
net_revenues = 0
currentRevenue = 0
previousRevenue = 0
total_change = 0

# open file with the file path
with open (PyBank_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Include the header
    header = next(csvreader)
    print(header)

    #calculate Total Months and print
    for row in csvreader:
        print(row)

        # count months calculations
        months.append(row[0])
        total_months = len(months)

        # calculate Net Profit/Loss
        profit_Loss.append(int(row[1]))
        net_revenues = net_revenues + int(row[1])
        
        # calculate total changes and average changes
        currentRevenue = int(row[1])
        for i in range(len(profit_Loss)):
            currentRevenue = float(profit_Loss[i])
            previousRevenue = float(profit_Loss[i-1])

        monthly_change = currentRevenue - previousRevenue

        #put each monthly_change value in monthly_changes pile
        monthly_changes.append(monthly_change)

        total_change = sum(monthly_changes)

        #calculate how many count of changes in profit/loss
        change_count = len(monthly_changes) - 1
        
        if change_count == 0:
            average = 0
        else:
            average = round(total_change/change_count, 2)


        # calculate greatest increase/decrease in revenue

        greatest_increase = profit_Loss[profit_Loss.index(max(profit_Loss))] - profit_Loss[profit_Loss.index(max(profit_Loss))-1]
        best_month = months[profit_Loss.index(max(profit_Loss))]

        greatest_decrease = profit_Loss[profit_Loss.index(min(profit_Loss))] - profit_Loss[profit_Loss.index(min(profit_Loss))-1]
        worst_month = months[profit_Loss.index(min(profit_Loss))]

       


# print Analysis
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {total_months}")
print(f"Net Profit/Loss: $ {net_revenues} ")
print(f"Average Change: $ {average}")
print(f"Greatest Increase in Profits: {best_month} (${greatest_increase})")
print(f"Greatest Descrease in Profits: {worst_month} (${greatest_decrease})")

#create output text file for analysis

PyBank_analysis = os.path.join("PyBank_analysis.txt")
with open(PyBank_analysis, "w") as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("---------------------\n")
    outfile.write(f"Total Months: {total_months}\n")
    outfile.write(f"Net Profit/Loss: $ {net_revenues}\n")
    outfile.write(f"Average Change: $ {average}\n")
    outfile.write(f"Greatest Increase in Profits: {months[profit_Loss.index(max(profit_Loss))]} (${greatest_increase})\n")
    outfile.write(f"Greatest Descrease in Profits: {months[profit_Loss.index(min(profit_Loss))]} (${greatest_decrease})\n")

