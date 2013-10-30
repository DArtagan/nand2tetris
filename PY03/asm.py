import re
from CS410_inst_py import io_files
from instruction import a_instruction, c_instruction

class asm:
    instruction_list = []

    def __init__(self, in_file, out_file):
        self.in_file = open(in_file, 'r')
        self.out_file = open(out_file, 'w')
        for line in self.in_file:
            tag = self.parse_line(line)
            if tag == '<A-Instruction>':
                next(self.in_file)
                self.instruction_list.append(a_instruction(self.parse_line(next(self.in_file))))
            elif tag == '<C-Instruction>':
                next(self.in_file)
                comp = self.parse_line(next(self.in_file))
                dest = self.parse_line(next(self.in_file))
                jump = self.parse_line(next(self.in_file))
                self.instruction_list.append(c_instruction(comp, dest, jump))

    def __str__(self):
        contents = ''
        for instruction in self.instruction_list:
            if instruction.binary != '':
                contents += str(instruction)
                contents += '\n'
        return contents[:-1]

    def write(self):
        self.out_file.write(str(self))

    def parse_line(self, line):
        return line.strip()
