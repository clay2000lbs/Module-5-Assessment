log_file = open("um-server-01.txt")
#this line is opening a txt file and setting it to a variable


def sales_reports(log_file): 
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)

#this block is defining a function that takes in one param: log_file. it reads every line of the txt file and removes white space
#it also  defines the first section of the file as the day, and prints the line where the day is Tuesday.


sales_reports(log_file)
