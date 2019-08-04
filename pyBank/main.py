import os
import csv
file = './budget_data.csv'

with open(file,newline="") as csv_file:
    csv_data= csv.reader(csv_file,delimiter=",")
    head = next(csv_data)
    print(head)
    row_cnt = sum(1 for row in csv_data)
    print(f"Total Months: {row_cnt}")

prof_loss = 0
prv_bal = 0
run_diff = 0
prv_diff = 0
tot_avg = 0
revenue_avg_list = [0]
dic_data={}

with open(file,newline="") as csv_file:
    csv_data= csv.reader(csv_file,delimiter=",")
    head = next(csv_data)
    for row in csv_data:
        prof_loss = prof_loss + int(row[1])
        run_diff = run_diff + (float(row[1]) - prv_bal) 
        # Get the running average in a list
        revenue_avg_list = revenue_avg_list + [float(row[1]) - prv_bal]
        #arrange the running difference and date to dictionary 
        dic_data[float(row[1]) - prv_bal] = [row[0]] 
        #Get the greatest profit
        prv_bal = float(row[1])
        prv_diff = run_diff

    
    print(f"The net total amount of Profit/Losses: ${prof_loss}")
    #find the average
    tot_avg = round(run_diff/row_cnt,2)
    print(f"The average of the changes in Profit/Losses :${tot_avg}")
    # ''.join(dic_data) will remove the quotes and brackets
    print (f"The greatest increase in profits (date and amount) over the entire period: {''.join(dic_data[max(revenue_avg_list)])} -- ${max(revenue_avg_list)}")
    print (f"The greatest decrease in losses (date and amount) over the entire period: {''.join(dic_data[min(revenue_avg_list)])} -- ${min(revenue_avg_list)}")

    # Write to a file
out_file = './analyzed_data.txt'

with open(out_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("********************\n")
    file.write("Total Months: %d\n" % row_cnt)
    file.write("Total Revenue: $%d\n" % prof_loss)
    file.write("Average Revenue Change $%d\n" % tot_avg)
    file.write("Greatest Increase in Revenue: %s ($%s)\n" % (''.join(dic_data[max(revenue_avg_list)]), max(revenue_avg_list)))
    file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (''.join(dic_data[min(revenue_avg_list)]), min(revenue_avg_list)))
