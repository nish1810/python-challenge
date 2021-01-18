import os
import csv
import sys




# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    budget = csv.reader(csvfile, delimiter=',')
    header = next(budget)
    
    months = []
    total_amount = []
    revenue_change = []
    
    #loop through the file
    for x in budget:
       
       months.append(x[0])
       total_months = len(months)

       total_amount.append(x[1])
       total_amount = [int(x) for x in total_amount]
       net = sum(total_amount)



    for x in range(1, len(total_amount)):
        revenue_change.append((int(total_amount[x]) - int(total_amount[x-1])))
        
    
    
    # calculate average revenue change
    average = sum(revenue_change) / len(revenue_change)
    greatest_increase = max(revenue_change) 
    greatest_decrease = min(revenue_change)

    

   
    print(f'Total Months: {total_months}')
    print(f'Total: ${net}')
    print(f'Average: ${average}')
    print(f'Greatest Increase in Profits: ${greatest_increase}')
    print(f'Greatest Decrease in Profits: ${greatest_decrease}')

    with open('budget_data.txt', 'w') as f:
        print(f'Financial Analysis\n-----------------------\nTotal Months: {total_months}\nTotal: {net}\nAverage Change: ${average}\nGreatest Increase in Profits: (${greatest_increase})\nGreatest Decrease in Profits: (${greatest_decrease})' ,file=f)