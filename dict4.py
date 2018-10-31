""" This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e. the whole e-mail address). At the end of the program print out the contents of your dictionary.
    python schoolcount.py
    Enter a file name: mbox-short.txt
    {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
    'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}"""

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
        domain = list(words[1].split("@"))
        emails[domain[1]] = emails.get(domain[1], 0) + 1
print(emails)




