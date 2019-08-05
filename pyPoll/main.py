import os
import csv
row_cnt = 0 
uniq_cand = []
cand_result_dict= {}
winner=""
vote_received=0

file ='./election_data.csv'

# Get the list of unique Candidates from csv
with open(file,newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)
    for row in csv_reader:
        row_cnt = row_cnt + 1
        if row[2] not in uniq_cand:
            uniq_cand = uniq_cand + [row[2]]

#print(uniq_cand)

#print(cand_result_dict)
# Set the candidate dictionary with name and count as zero
for i in range(len(uniq_cand)):   
    cand_result_dict[uniq_cand[i]] = [0]
# loop through the csv data for each candidate for count 
with open(file,newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)
    for row in csv_reader:
        if row[2] in cand_result_dict:
            cand_result_dict[row[2]] += [1]
            #cand_result_dict[row[2]] = [1]
print("***************************")
print("Election Results           ")
print("***************************")
print(f"  Total Votes: {row_cnt}")
print("***************************")
# get the total count and percentage for each candidate
# compare each candidate and announce the winner
for i in range(len(uniq_cand)):
    print(f"{uniq_cand[i]}   : {round(sum(cand_result_dict[uniq_cand[i]])/row_cnt*100,2)}% ({sum(cand_result_dict[uniq_cand[i]])})")
    if sum(cand_result_dict[uniq_cand[i]]) > vote_received:
        winner = uniq_cand[i]
        vote_received = sum(cand_result_dict[uniq_cand[i]])

print("***************************")
print(f"   Winner is {winner}")
print("***************************")

    # Write to a file
out_file = './election_result.txt'

with open(out_file, 'w') as file:
    file.write("***************************\n")
    file.write("     Election Result       \n")
    file.write("***************************\n")
    file.write("     Total Votes: %d\n" % row_cnt)
    file.write("***************************\n")
    for i in range(len(uniq_cand)):
        file.write("%s   : %d%s (%d)\n" % (uniq_cand[i], round(sum(cand_result_dict[uniq_cand[i]])/row_cnt*100,2), "%", sum(cand_result_dict[uniq_cand[i]])))
    file.write("***************************\n")
    file.write("     Winner is %s\n" % winner)
    file.write("***************************\n")