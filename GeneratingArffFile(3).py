large_arff_file = open("arf_file_no_header.arff", "r");
Lines = large_arff_file.readlines();

small_arff_file = open("arf_file_no_header_small.arff", "w");

p = 0
for line in Lines:
    if "t" in str(line):
        small_arff_file.write(str(line));
    if p%100 == 0:
        print(p);
    p += 1;