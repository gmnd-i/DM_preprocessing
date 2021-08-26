import pandas as pd
import numpy as np


#############################################################################
'''i=0 # progress indicator'''
columns = set();
with open("reddit-user-posting-behavior.csv", mode="r") as file:
    Lines = file.readlines()
    
    for line in Lines:
        line = line.replace("\n", "");
        words = line.split(',');
        subreddits_following = words[1:]
        
        for subreddit in subreddits_following:
            columns.add(subreddit);
        
        # progress indicator
        '''
        if i%100==0:
            print(i);
        i+=1;
        '''

# print(columns);
# print(len(columns))
############################################################################

header = list();
header.append("user id");
for s in columns:
    header.append(s);
    
# df = list();
new_file = open("new_file_small(2).csv", "w");
new_file.write(str(header));
# df.append(header);

# Filling the dataframe
with open("reddit-user-posting-behavior.csv", mode="r") as file:
    Lines = file.readlines()
    
    i = 0;
    for line in Lines:
        line = line.replace("\n", "");
        words = line.split(',');
        subreddits_following = words[1:]
        user_id = (words[0]);

        row = [0]*len(header);
        row[0] = user_id;

        for subreddit in subreddits_following:
            index = header.index(subreddit);
            row[index] = 1;

        for i in range(0, len(row)):
            if row[i] == 0:
                row[i] = '?'
        # df.append(row);
        new_file.write(str(row));
        new_file.write("\n");

        if i==1000:
            break;
        i+=1;
        if i%100==0:
            print(i)

# print(len(df));
# print(df[0]);
# print(df[1]);
# print(df[100]);
# print(df[len(df) - 1]);










'''
# Get the columns and rows count -----------------------------------------
nCols = len(columns) + 1; # 1 for user id                               #|
nRows = 0;                                                              #|
with open("reddit-user-posting-behavior.csv", mode="r") as file:        #|
    Lines = file.readlines()                                            #|
    nRows = len(Lines);                                                 #|
# -------------------------------------------------------------------------
'''