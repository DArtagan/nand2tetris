import re

ifile = open('hexStuff', 'r')
ofile = open('hexOut', 'w')
for line in ifile:
    daMatch = re.match(r'(\d{7})', line)
    if daMatch != None:
        print(daMatch)
        output = line.replace(daMatch, ('X%02Xi' % int(str(daMatch[0]),2)))
        print(output)
        ofile.write(output) 
