file_read = open("header for supermarket subreddit fake.txt", "r");
file_write = open("header for supermarket subreddit fake modified.txt", "w");
file_subreddits = open("list_of_subreddits.txt", "r");

Lines = file_read.readlines();
Subreddits = file_subreddits.readlines();
i = 0;


for line in Lines:
    start = 11; # 11 for all lines
    end = line.find("'",12);
    
    text_to_replace = line[start+1:end];
    subreddit = Subreddits[i];
    subreddit = subreddit.replace("\n", "");
    modified_line = line.replace(text_to_replace, subreddit);
    i+=1;

    
    file_write.write(modified_line);
    # print(line[start+1:end])
    
