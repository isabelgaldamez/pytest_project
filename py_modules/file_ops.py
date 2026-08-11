print("**** Option 1 ****")
try :
    f = open("myfile.txt", 'r')
    # print(f.read()) # reads the whole document and returns it into a str
    line = f.readline() # returns one line from the file and you can loop through the document
    while line:
        print(line)
        line = f.readline()
    # print(f.readlines()) # returns a list with all the lines
finally:
    f.close()

    # Option #2
print("**** Option 2 ****")
with open("myfile.txt", 'r') as file:
    # f = file.read()
    print(file.readline())#
    list2 = file.read().split('\n')
    print(list2)

# Option 3 : Read line by line
print("**** Option 3 ****")
with open("myfile.txt", 'r') as file:
    for line in file:
        print(line.strip())

