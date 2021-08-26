subreddits_300_file = open("list_of_subreddits 300.txt", "r");
Subreddits = subreddits_300_file.readlines();
for i in range(0, len(Subreddits)):
    Subreddits[i] = Subreddits[i].replace("\n", "");
# print(Subreddits)


original_data_file = open("reddit-user-posting-behavior.csv", "r");
original_data_records = original_data_file.readlines();

modified_data_file = open("reddit-user-posting-behavior-300-limited.txt", "a"); # write to this

b = 0
for line in original_data_records:
    user_following_subs = line.split(",");
    following_subs = user_following_subs[1:]; # removed user id
    following_subs[len(following_subs)-1] = following_subs[len(following_subs)-1].replace("\n", "");
    # print(following_subs);

   
    for sub in following_subs:
       if sub not in Subreddits:
           following_subs.remove(sub);

    modified_line = "";
    modified_line += str(user_following_subs[0]);
    for sub in following_subs:
        modified_line += "," + str(sub);
    modified_line += "\n";
    
    modified_data_file.write(modified_line);
    
    if b%100==0:
        print(b);
    b+=1;

