#============================================================
# PROGRAMMER:........ William H. Weiskopf
# USERID:............ WWEISKOP
# COURSE:............ CSCI-410
# TERM............... FALL 2013
# ASIGNMENT:......... PY01
# FILENAME:.......... py01.py
# PYTHON VERSION:.... 3.3.0
#============================================================

output = "";
type = {'a': [4], 'c': [1, 2, 1, 6, 3, 3]}

for count, line in enumerate(open('machine.hack', 'r')):
    output += "// " + '{0:05d}'.format(count) + ": "
    if line[0] == '0':
        for i in range(0, len(line)-1, type['a'][0]):
            output += line[i:i+4] + ' '
    elif line[0] == '1':
        j = 0
        for i in range(0, len(type['c'])):
            output += line[j:j+type['c'][i]] + ' '
            j += type['c'][i]
    output = output.strip()
    output += '\n'
output = output.strip()
print(output)
open('assembly.asm', 'w').write(output);
