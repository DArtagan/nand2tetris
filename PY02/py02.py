#============================================================
# PROGRAMMER:........ William H. Weiskopf
# USERID:............ WWEISKOP
# COURSE:............ CSCI-410
# TERM............... FALL 2013
# ASIGNMENT:......... PY02
# FILENAME:.......... py02.py
# PYTHON VERSION:.... 3.3.0
#============================================================

state = 'open'
counter = 0
address = 0
temp = ''

fileOut = open('machine.xml', 'w')

fileOut.write('<hack>\n');


with open('machine.hack') as fileIn:
    while state != 'end':
        while state == 'open':
            c = fileIn.read(1)
            if c == '0':
                fileOut.write('<A-Instruction>\n')
                fileOut.write('<address>' + str(address) + '</address>\n')
                counter += 1
                state = 'aType'
            elif c == '1':
                fileOut.write('<C-Instruction>\n')
                fileOut.write('<address>' + str(address) + '</address>\n')
                counter += 1
                state = 'cType'
            elif not c:
                state = 'end'
                break

        while state == 'aType':
            c = fileIn.read(1)
            if not c.isspace():
                temp += c
                counter += 1
            if counter == 16:
                fileOut.write('<constant>' + str(int(temp,2)) + '</constant>\n</A-Instruction>\n')
                counter = 0
                temp = ''
                state = 'close'

        while state == 'cType':
            c = fileIn.read(1)
            if not c.isspace():
                temp += c
                counter += 1
            if counter == 16:
                fileOut.write('<comp>' + '0x%02X' % int(temp[3:9],2) + '</comp>\n<dest>' + "%03d" % int(temp[10:12]) + '</dest>\n<jump>' + "%03d" % int(temp[13:15]) + '</jump>\n</C-Instruction>\n')
                counter = 0
                temp = ''
                state = 'close'

        while state == 'close':
            c = fileIn.read(1)
            if c == '\n':
                state = 'open'
                address += 1

fileOut.write('</hack>')

fileIn2 = open('machine.xml')
fileOut2 = open('assembly.asm', 'w')

