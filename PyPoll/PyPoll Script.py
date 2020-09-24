#!/usr/bin/env python
# coding: utf-8

# In[9]:


import csv

#VARIABLES
total_votes = 0
candidates= []
candidate_votes= {}
winner_count=0
name=[]
winner_no_votes = 0
winner = ""

#SCRIPT
with open("Resources/PyPoll_Resources_election_data.csv") as csv_file:
    csv_reader=csv.reader(csv_file,delimiter = ",")
    csv_header=next(csv_reader)
    
    for row in csv_reader:
            total_votes += 1
            name = str(row[2])
            
            if name not in candidates:
                candidates.append(name)
                candidate_votes[name]=1
                
            else: 
                candidate_votes[name]= candidate_votes[name] + 1
                
    candidate_vote_percentage={}
    for i in candidate_votes:
            candidate_vote_percentage [i] = "{:.3%}".format((candidate_votes [i]/total_votes)), candidate_votes [i]
            
            if (candidate_votes [i] > winner_no_votes):
                winner_no_votes = candidate_votes [i]
                winner = i


#PRINT TO TXT

url="../PyPoll/PyPoll.txt"

a=f"Election Results\n"
b='------------------\n'
c=f"Total Votes: {str(total_votes)}\n"
d=f"{candidate_vote_percentage}\n"
e=f"Winner: {winner}\n"
z=[a,b,c,b,d,b,e,b]

with open(url,'w') as data_text:
    data_text.writelines(z)

