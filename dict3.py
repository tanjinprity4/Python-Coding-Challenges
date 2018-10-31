"""Add code to the above program to figure out who has the most messages in the file.
    After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Section ??) to find who has the most messages and print how many messages the person has.
    
    Enter a file name: mbox-short.txt
    cwen@iupui.edu 5
    
    Enter a file name: mbox.txt
    zqian@umich.edu 195
"""


fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print ("File cannot be opened: " + fname)
    exit()

emails = {}
for line in fhand:
    line = line.lower()
    words = list(line.split())
    if "from" in words:
        emails[words[1]] = emails.get(words[1], 0) + 1
print(emails)

maximum = max(zip(emails.keys(), emails. values()))
print(maximum)

max = 0
for user in emails:
    if emails[user] > max:
        max = emails[user]

for user in emails:
    if emails[user] == max:
        print(user + " " + str(max))

#learnt maximum = max(zip(emails.keys(), emails. values()))
