#!/usr/bin/env python
# coding: utf-8

# In[101]:


import csv

#VARIABLES
total_months =0
total_profitloss= 0
previous_profitloss= 0
increase=0
increase_month= ""
decrease=0
decrease_month= ""
change=0
change_month=0
average=0
total_changemonth=0
average_changemonth=0


#CALCULATIONS/SCRIPT
with open("budget_data.csv") as csv_file:
    csv_reader= csv.reader(csv_file, delimiter = ",")
    csv_header=next(csv_reader)

    for row in csv_reader:
        
        total_months += 1    
        
        total_profitloss += int(row[1])
        
        if total_months > 1:
            change_month = int(row[1]) - previous_profitloss
            
        total_changemonth += change_month
        
        previous_profitloss = int (row[1])
        
        if change_month > increase:
            increase = change_month
            increase_month = row[0]
        
        if change_month < decrease:
            decrease = change_month
            decrease_month = row[0]
            
average_changemonth = total_changemonth / (total_months -1)

#PRINT TO TEXT

url= "../PyBank/PyBank.txt"

a=f"Financial Analysis\n"
b='------------------\n'
c= f"Total Months: {int(total_months)}\n"
d= f"Total: ${str(total_profitloss)}\n"
e=f"Average Change: ${str(average_changemonth)}\n"
f=f"Greatest Increase in Profits: {increase_month} (${str(increase)})\n"
g=f"Greatest Decrease in Profits: {decrease_month} (${str(decrease)})\n"
z=[a,b,c,d,e,f,g]

with open(url,'w') as data_text:
    data_text.writelines(z)


# In[ ]:




