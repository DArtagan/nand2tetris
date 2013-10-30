#============================================================
# PROGRAMMER:........ William H. Weiskopf
# USERID:............ WWEISKOP
# COURSE:............ CSCI-410
# TERM............... FALL 2013
# ASIGNMENT:......... PY02
# FILENAME:.......... py02.py
# PYTHON VERSION:.... 3.3.0
#============================================================

import os
import sys

class reader:
    def __init__(self, in_file):
        self.file = open((in_file + ".txt"), 'r')
        self.line_count = sum(1 for line in self.file)
        self.file.seek(0)
    
    def get_line_count(self):
        return self.line_count
        
    def readLine(self):
        self.current_line = self.file.readline().strip()

    def LineType(self):
        if self.current_line:
            line = int(self.current_line)
            if(line == 0):
                output = "V_ZERO"
            elif(line > 0):
                output = "V_POS"
            elif(line < 0):
                output = "V_NEG"
            else:
                output = None
        else:
            output = None
        return output
    
    def value(self):
        return abs(int(self.current_line))


class writer:
    local_array = [0]*5      # count_NEG, count_ZERO, count_POS, total_NEG, total_POS
    global_array = [0]*5
    in_file = ""

    def __init__(self, out_file):
        self.file = open((out_file + ".tot"), 'w')
        self.file.write('FILENAME\tNEG\tZERO\tPOS\tAVG NEG\tAVG POS\tAVERAGE\n')
        self.file.write('=========================================================\n')

    def setFileName(self, in_file):
        if(self.in_file != ""):
            output = self.in_file + '.txt\t' + str(self.local_array[0]) + "\t\t" + str(self.local_array[1]) + "\t\t" + str(self.local_array[2]) + "\t\t"
            if(self.local_array[0]): 
                output += str(self.local_array[3] / self.local_array[0]) + "\t\t"
            else:
                output += '0' + "\t\t"
            if(self.local_array[2]):
                output += str(self.local_array[4] / self.local_array[2]) + "\t\t\t"
            else:
                output += '0' + "\t\t\t"
            if(self.local_array[0] + self.local_array
                    [1] + self.local_array[2]):
                output += str((-1*self.local_array[3] + self.local_array[4]) / (self.local_array[0] + self.local_array[1] + self.local_array[2]))
            else:
                output += '0'
            self.file.write(output + '\n') 
            
            for i in range(0, len(self.local_array)):
                self.global_array[i] += self.local_array[i]

        self.in_file = in_file
        self.local_array = [0]*5

    def writeNEG(self, value):
        self.local_array[0] += 1
        self.local_array[3] += value

    def writeZERO(self):
        self.local_array[1] += 1

    def writePOS(self, value):
        self.local_array[2] += 1
        self.local_array[4] += value

    def close(self):
        self.file.write("=========================================================\n")
        output = "Total\t\t\t\t" + str(self.global_array[0]) + "\t\t" + str(self.global_array[1]) + "\t\t" + str(self.global_array[2]) + "\t\t"
        if(self.global_array[0]): 
            output += str(-1*self.global_array[3] / self.global_array[0]) + "\t\t"
        else:
            output += '0' + "\t\t"
        if(self.global_array[2]):
            output += str(self.global_array[4] / self.global_array[2]) + "\t\t\t"
        else:
            output += '0' + "\t\t\t"
        if(self.global_array[0] + self.global_array
                [1] + self.global_array[2]):
            output += str((-1*self.global_array[3] + self.global_array[4]) / (self.global_array[0] + self.global_array[1] + self.global_array[2]))
        else:
            output += '0'

        self.file.write(output)


class fileSet:
    files = []
    dir_name = ""
    
    def __init__(self):
        argument = sys.argv
        if(len(argument) == 1):
            self.files = 'test.txt'
        else:
            argument = argument[1]
            if(os.path.isfile(argument)):
                self.files.append(argument[:-4])
            elif(os.path.isdir(argument)):
                os.chdir(argument)
                dir_name = argument
                for name in os.listdir('.'):
                    if os.path.isfile(name) & (".txt" in name):
                        self.files.append(name[:-4] )
            else:
                print("Error parsing given folder or file")
        print(self.files)

    def getFiles(self):
        return self.files

    def getDir(self):
        return self.dir_name


# MAIN
files = fileSet()
if(files.getDir() != ""):
    current_out = writer(files.getDir())
else:
    current_out = writer(files.getFiles()[0])

for file in files.getFiles():
    current_in = reader(file)
    current_out.setFileName(file)
    for i in range(0,current_in.get_line_count()):
        current_in.readLine()
        line_type = current_in.LineType()
        if line_type == 'V_POS':
            current_out.writePOS(current_in.value())
        elif line_type == 'ZERO':
            current_out.writeZERO()
        elif line_type == 'V_NEG':
            current_out.writeNEG(current_in.value())
current_out.setFileName("")
current_out.close()
