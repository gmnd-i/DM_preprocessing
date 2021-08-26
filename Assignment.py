import pandas as pd
import numpy as np

#############################################################################
MAX_COLUMN_COUNT = 0;
with open("reddit-user-posting-behavior.csv", mode="r") as file:
    Lines = file.readlines()
    
    for line in Lines:
        column_count = len(line.split(",")) + 1;
        if column_count > MAX_COLUMN_COUNT:
            MAX_COLUMN_COUNT = column_count;

# print(MAX_COLUMN_COUNT)
############################################################################

column_names = [i for i in range(0, MAX_COLUMN_COUNT)]
df = pd.read_csv("reddit-user-posting-behavior.csv", names=column_names, low_memory=False);

npdf = df.to_numpy()
npdf = npdf[:50]

# -------------------------------------------------------------------------
# Get unique values (subreddits) from the array
# (1) remove the first column (numbers)
npdf_ = npdf[:,1:]
# (2) Get unique values
npdf__ = np.reshape(npdf_, (npdf_.shape[0]*npdf_.shape[1], 1) );
subreddits = list(); 
i=0;
for x in npdf__:
    if str(x) not in subreddits:
        subreddits.append(str(x));

    if i%100==0:
        print(i);
    i+=1;
# --------------------------------------------------------------------------

subreddits_with_frequency = dict.fromkeys(subreddits, 0);

# Get the number of occurences
for x in npdf__:
    subreddits_with_frequency[str(x)] += 1;

# print(subreddits_with_frequency);


SUPPORT_THRESHOLD = 5;


candidate_set = dict();

for k in subreddits_with_frequency:
    if subreddits_with_frequency[k] >= SUPPORT_THRESHOLD:
        candidate_set[k] = subreddits_with_frequency[k]

C = list();
C.append(candidate_set);

for i in range(2, len(subreddits)):
    pass;

    # (1) Generate subsets of subreddits of size 2,3,4,5,..... <- i
    #       {r1, r2} , {r1, r3} , {r1, r4} ....... {r10, r12} ..... 
    # (2) Count the occurences of the above generated sets
    # (3) Remove if below threshold
    # (4) Repeat

    considering_set = C[len(C)-1]; # last one
    next_set = 