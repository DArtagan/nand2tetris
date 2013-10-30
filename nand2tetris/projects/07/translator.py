#============================================================
# PROGRAMMER:........ William H. Weiskopf
# USERID:............ WWEISKOP
# COURSE:............ CSCI-410
# TERM............... FALL 2013
# ASIGNMENT:......... ECS 07
# FILENAME:.......... translator.py
# PYTHON VERSION:.... 3.3.0
#============================================================

import re
import sys
import os
from memory import *
from arithmetic import *
from boolean import *

class stack:
    bool_count = 0
    stack = ""

    dict_arithmetic = {"add": arithmetic.addition,
                       "sub": arithmetic.subtraction,
                       "neg": arithmetic.negative,
                       "and": arithmetic.and_arith,
                       "or":  arithmetic.or_arith,
                       "not": arithmetic.not_arith, 
                      }

    dict_boolean = {"eq":  boolean.equality,
                    "gt":  boolean.greater_than,
                    "lt":  boolean.less_than,
                   }

    dict_memory = {"push_constant": memory.push_constant,
                   "push_static":   memory.push_static,
                   "push_temp":     memory.push_temp,
                   "push_pointer":  memory.push_pointer,
                   "push_argument": memory.push_argument,
                   "push_local":    memory.push_local,
                   "push_this":     memory.push_this,
                   "push_that":     memory.push_that, 
                   "pop_constant":  memory.pop_constant,
                   "pop_static":    memory.pop_static,
                   "pop_temp":      memory.pop_temp,
                   "pop_pointer":   memory.pop_pointer,
                   "pop_argument":  memory.pop_argument,
                   "pop_local":     memory.pop_local,
                   "pop_this":      memory.pop_this,
                   "pop_that":      memory.pop_that, 
               }

    def __init__(self, in_file):
        self.in_file = open(in_file, 'r')
        self.parse()
        self.stack += "(END_LOOP)\n@END_LOOP\n0;JMP"

    def parse(self):
        for line in self.in_file:
            line = line.strip()
            if line.startswith("//") | (line == ""):
                continue
            line = line.split(' ')
            if line[0] in self.dict_arithmetic:
                self.arithmetic(line[0])
            elif line[0] in self.dict_boolean:
                self.boolean(line[0])
            elif (line[0] == "push") | (line[0] == "pop"):
                self.memory(line[0], line[1], line[2])

    def __str__(self):
        return self.stack

    def write(self, out_file):
        out_file = open(out_file, 'w')
        out_file.write(str(self))

    def memory(self, pushpop, segment, index):
        self.stack += self.dict_memory[pushpop + "_" + segment](index)

    def arithmetic(self, operation):
        self.stack += self.dict_arithmetic[operation]()

    def boolean(self, operation):
        self.stack += self.dict_boolean[operation](self.bool_count)
        self.bool_count += 1

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

in_file = fileSet()
newStack = stack(in_file.getFile())
newStack.write(in_file.getFile()[:-3] + '.asm')
print(newStack)
