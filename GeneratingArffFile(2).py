file = open("reddit-user-posting-behavior-300-limited.txt", "r");
Lines = file.readlines();
 
subreddits_300_file = open("list_of_subreddits 300.txt", "r");
Subreddits = subreddits_300_file.readlines();
for i in range(0, len(Subreddits)):
    Subreddits[i] = Subreddits[i].replace("\n", "");

arff_file_no_header = open("arf_file_no_header.arff", "a");

b = 0;
for line in Lines:
    splitted = line.split(",");
    subs = splitted[1:];

    # Ignore lines with no subreddits
    if len(subs) == 0: 
        continue;

    print(splitted) # for monitoring progress

    subs[len(subs)-1] = subs[len(subs)-1].replace("\n", ""); # remove the new line at the end
    
    modified_line = "";
    # modified_line += splitted[0]; # append user id

    for i in range(0, len(Subreddits)):
        if Subreddits[i] in subs:
            modified_line += "," + "t";
        else:
            modified_line += "," + "?";
    modified_line += "\n";

    modified_line =  modified_line.replace(",", "", 1); # remove the first ,
    
    arff_file_no_header.write(modified_line);
    
    # print(line);