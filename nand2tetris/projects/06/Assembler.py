#============================================================
# PROGRAMMER:........ William H. Weiskopf
# USERID:............ WWEISKOP
# COURSE:............ CSCI-410
# TERM............... FALL 2013
# ASIGNMENT:......... ECS 06
# FILENAME:.......... assembler.py
# PYTHON VERSION:.... 3.3.0
#============================================================

import sys
import os

class asm:
    instructions = []
    labels = {'SP': '0',
              'LCL': '1',
              'ARG': '2',
              'THIS': '3',
              'THAT': '4',
              'SCREEN': '16384',
              'KBD': '24576',}
    pseudo_inst = {}
    operations = {}
    count = -1
    label_count = 15

    def __init__(self, in_file):
        for i in range(16):
            self.labels.update({("R"+str(i)): str(i)})

        self.in_file = open(in_file, 'r')
        for count, line in enumerate(self.in_file):
            instruction = self.parse(line)
        self.label_cleanup()
        self.in_file.seek(0)
        for line in self.in_file: 
            instruction = self.converter(line)
            if instruction != None: self.instructions.append(instruction)

    def __str__(self):
        output = ''
        for instruction in self.instructions:
            output += str(instruction) + '\n'
        return output

    def write(self, out_file):
        out_file = open(out_file, 'w')
        out_file.write(str(self))

    def parse(self, line):
        instruction_signs = ['A', 'D', 'M', '0', '(', '@']

        line = line.strip()
        line = line.split(' ', 1)[0]
        if line == '': return
        if line[0] in instruction_signs: 
            self.count += 1
        if line[0] == '@':
            if line[1:] not in self.labels:
                self.labels.update({line[1:]: None})
        elif line[0] == '(':
            self.pseudo_inst.update({line[1:-1]: self.count})
            self.count -= 1
        return

    def label_cleanup(self):
        for inst in self.pseudo_inst:
            if inst in self.labels:
                del self.labels[inst]
        for label in self.labels:
            if label.isdigit():
                self.labels[label] = label

    def label_assignment(self, request):
        while str(self.label_count) in self.labels.values(): 
            self.label_count += 1
        self.labels[request] = str(self.label_count)

    def converter(self, line):
        operator_signs = ['A', 'D', 'M', '0']
        output = None
        line = line.strip()
        line = line.split(' ', 1)[0]
        if line == '': return
        elif line[0] == '@' and line[1:] in self.labels:
            if self.labels[line[1:]] is None:
                self.label_assignment(line[1:])
            output = '{0:b}'.format(int(self.labels[line[1:]])).zfill(16)
        elif line[0] == '@' and line[1:] in self.pseudo_inst:
            output = '{0:b}'.format(int(self.pseudo_inst[line[1:]])).zfill(16)
        elif line[0] in operator_signs:
            output = self.c_instruction(line)
        return output

    def c_instruction(self, line):
        dest = '000'
        comp = '0101010'
        jump = '000'
        if '=' in line:
            dest =  self.dest_dict[line.split('=')[0]]
            temp = line.replace('=', ';')
            comp =  self.comp_dict[temp.split(';')[1]]
        if ';' in line:
            jump = self.jump_dict[line.split(';')[1]]
            if '=' not in line:
                comp = self.comp_dict[line.split(';')[0]]
        return '111' + comp + dest + jump

    dest_dict = {'null': '000', 
                 'M':    '001', 
                 'D':    '010', 
                 'MD':   '011', 
                 'A':    '100', 
                 'AM':   '101', 
                 'AD':   '110', 
                 'AMD':  '111',
                 '0':    '000', }

    jump_dict = {'null': '000', 
                 'JGT': '001', 
                 'JEQ': '010', 
                 'JGE': '011', 
                 'JLT': '100', 
                 'JNE': '101', 
                 'JLE': '110', 
                 'JMP': '111',}

    comp_dict = {'0':   '0101010', 
                 '1':   '0111111', 
                 '-1':  '0111010', 
                 'D':   '0001100', 
                 'A':   '0110000', 
                 '!D':  '0001101', 
                 '!A':  '0110011', 
                 '-D':  '0001111', 
                 '-A':  '0110011', 
                 'D+1': '0011111', 
                 'A+1': '0110111', 
                 'D-1': '0001110', 
                 'A-1': '0110010', 
                 'D+A': '0000010', 
                 'D-A': '0010011', 
                 'A-D': '0000111', 
                 'D&A': '0000000', 
                 'D|A': '0010101', 
                 'M':   '1110000', 
                 '!M':  '1110001', 
                 '-M':  '1110011', 
                 'M+1': '1110111', 
                 'M-1': '1110010', 
                 'D+M': '1000010', 
                 'D-M': '1010011', 
                 'M-D': '1000111', 
                 'D&M': '1000000', 
                 'D|M': '1010101', }
class fileSet:
    files = []
    dir_name = ""
    
    def __init__(self):
        argument = sys.argv
        if(len(argument) == 1):
            self.files = 'Prog.asm'
        else:
            argument = argument[1]
            if(os.path.isfile(argument)):
                self.files = argument
            else:
                print("Error parsing given folder or file")

    def getFile(self):
        return self.files

# MAIN
files = fileSet()
assembly = asm(files.getFile())
assembly.write(files.getFile()[:-4] + '.hack')
